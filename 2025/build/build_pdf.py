"""Typeset the PDF edition of Aikipedia 2025: Annual Collection.

Input: a collection draft directory (its editions/pdf.json lists the PDF edition's files in order).
Output: the 7 x 10 in PDF, with the editor's cover as the first page, continuous page numbers,
and page numbers in the two tables of contents and the index of terms.

Page numbers for cross-references are found in two passes. Pass 1 renders the volume with a
fixed-width placeholder beside every reference and an invisible marker at every anchor; the
markers are then read back from the PDF text to learn each anchor's page. Pass 2 renders again
with the real numbers. A check pass confirms the numbers did not move.
"""
import asyncio, html, json, pathlib, re, subprocess, sys
from pypdf import PdfReader, PdfWriter
from PIL import Image
from playwright.async_api import async_playwright

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
STEM = sys.argv[3] if len(sys.argv) > 3 else 'Aikipedia_2025_Annual_Collection'
TS = pathlib.Path(__file__).parent
FONTS = TS / 'node_modules/@fontsource'
WORK = OUT / 'work'; WORK.mkdir(parents=True, exist_ok=True)
CONTENT_PX = round((7 - 0.95 - 0.85) * 96)   # text column width in CSS px
REF_FILES = {'01_tables-of-contents.md', '23_index-of-terms.md'}   # files whose links get page numbers

def ff(fam, pkg, sub, w, st='normal'):
    f = FONTS / pkg / 'files' / f'{pkg}-{sub}-{w}-{st}.woff2'
    rng = 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD' if sub == 'latin' else 'U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF'
    return f"@font-face{{font-family:'{fam}';src:url('{f.as_uri()}') format('woff2');font-weight:{w};font-style:{st};unicode-range:{rng}}}"

FONTCSS = ''.join(
    [ff('Serif', 'source-serif-4', s, w, st) for s in ('latin', 'latin-ext') for w, st in ((400, 'normal'), (400, 'italic'), (600, 'normal'), (700, 'normal'), (600, 'italic'))]
    + [ff('Sans', 'inter', s, w) for s in ('latin', 'latin-ext') for w in (400, 500, 600, 700, 800)]
    + [ff('Mono', 'ibm-plex-mono', s, w) for s in ('latin', 'latin-ext') for w in (400, 500)])

CSS = FONTCSS + r'''
:root{--ink:#14213d;--muted:#5d6b78;--accent:#0b1f4d;--red:#d7161e;--rule:#cfd6dd}
@page{size:7in 10in;margin:0.95in 0.85in 0.95in 0.95in;
  @bottom-center{content:counter(page);font:500 9pt 'Mono';color:#55606b;vertical-align:top;padding-top:12pt}}
@page :right{@bottom-center{content:'Aikipedia 2025\00A0\00A0\00A0·\00A0\00A0\00A0' counter(page)}}
@page title{@bottom-center{content:none}}
html{font-family:'Serif','Noto Serif CJK SC','Noto Color Emoji',serif;font-size:11pt;line-height:1.5;color:var(--ink);-webkit-print-color-adjust:exact;font-kerning:normal}
body{margin:0}
h1,h2,h3,h4,h5,h6{font-family:'Sans','Noto Sans CJK SC',sans-serif;color:var(--ink);break-after:avoid;line-height:1.25}
h1{font-size:24pt;font-weight:800;letter-spacing:-.01em;margin:.35in 0 .3in;padding-top:.16in;border-top:2pt solid var(--accent);break-before:page}
h2{font-size:16pt;font-weight:700;margin:.36in 0 .14in}
h3{font-size:12.5pt;font-weight:700;margin:.28in 0 .1in}
h4,h5,h6{font-size:11pt;font-weight:600;margin:.22in 0 .08in}
section.f-10 h2,section.f-11 h2,section.f-12 h2,section.f-13 h2,section.f-14 h2,section.f-15 h2{font:700 17pt/1.2 'Sans';break-before:page;margin:0 0 .06in;padding-top:.12in}
.pbreak{break-before:page;height:0}
.opener+h2{margin-top:0!important;border-top:0!important;padding-top:0!important}
section.f-20 h2{break-before:page;margin-top:0;padding-top:.1in;font-size:14pt}
section.f-20 p{text-align:left;hyphens:manual}
.opener{break-before:page;break-after:page;padding-top:1.0in}
.opener h1.ptitle{border:0;break-before:auto;margin:0;padding:0}
.pnum{display:block;font:600 10pt 'Mono';letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
.pname{display:block;font:800 30pt/1.1 'Sans';color:var(--accent);margin-top:.14in;padding-bottom:.2in;border-bottom:1.6pt solid var(--accent)}
.olist{margin-top:.34in}
.orow{display:flex;align-items:baseline;gap:5pt;font:400 10pt/1.35 'Sans';margin:0 0 4.5pt;color:inherit}
.orow .ct{flex:0 1 auto;min-width:0}.orow .dots{flex:1;border-bottom:.6pt dotted #9aa5b1;transform:translateY(-3pt)}.orow .cn{font:500 9pt 'Mono';white-space:nowrap;flex:0 0 auto}.idp{white-space:nowrap}table td,table td strong,table td b{overflow-wrap:break-word}.idp code{overflow-wrap:normal}table.atoc{table-layout:fixed}li.thm{list-style:none;margin-left:-1.2em}
.cmeta{font:500 9pt 'Mono';color:var(--muted);letter-spacing:.03em;margin:0 0 .14in;text-align:left}
.recbar{border-left:2pt solid var(--accent);padding:.04in 0 .04in .12in;margin:.06in 0 .2in;font:400 9pt/1.55 'Sans';color:#2b3a4a;break-inside:avoid;break-after:avoid}
.recbar .rid{font:600 9pt 'Mono';color:var(--accent)}.recbar .rt{font:600 10pt 'Sans';color:var(--ink)}
.recbar .m{display:inline-block;margin-right:11pt}.recbar .k{color:var(--muted);font-size:9pt;text-transform:uppercase;letter-spacing:.06em}
h4.rlabel.dup{display:none}
h4.rlabel{font:600 9pt 'Mono';letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:.14in 0 .07in}
section.f-10 h5,section.f-11 h5,section.f-12 h5,section.f-13 h5,section.f-14 h5,section.f-15 h5{font:700 11.5pt 'Sans';color:var(--accent);margin:.22in 0 .06in}
table.edrec{font-size:9pt;margin-top:.04in}table.edrec thead{display:none}table.edrec td:first-child{width:1.5in;color:var(--muted)}table.edrec td:first-child strong{font-weight:600}
.arch{font:400 9pt/1.5 'Mono','DejaVu Sans Mono','Noto Color Emoji',monospace;margin:.12in 0 .22in}
.al{display:flex;break-inside:avoid}.ln{flex:0 0 .5in;font-size:7.6pt;color:#56626e;text-align:right;padding-right:.1in;padding-top:1.4pt;border-right:.5pt solid var(--rule);margin-right:.1in}
.tx{flex:1;min-width:0;white-space:break-spaces;overflow-wrap:anywhere}
section.f-23 ul{padding-left:0}
li.ix{list-style:none;margin:0 0 7pt;break-inside:avoid}.ixr{display:flex;align-items:baseline;gap:5pt;font:600 10pt 'Sans'}.ixr .ixt{flex:0 1 auto;min-width:0}.ixr .ixt strong{font-weight:600}
.ixr .dots{flex:1;border-bottom:.6pt dotted #9aa5b1;transform:translateY(-3pt)}.ixr .ixp{font:500 9pt 'Mono';white-space:nowrap;flex:0 0 auto;text-align:right}
.ixs{font:400 9pt/1.45 'Sans';color:var(--muted);padding-left:.22in;margin-top:1pt}.ixs code{font-size:1.05em}
li.ixsee{break-inside:avoid;list-style:none;font:italic 9.5pt 'Serif';color:#3a4856;margin:0 0 6pt;padding-left:.22in}
.alist{margin:.25in 0 .1in;break-after:page}
.csub{font:600 9pt 'Sans';color:var(--muted);margin:.12in 0 .05in;text-transform:uppercase;letter-spacing:.08em}
.crow.ap{padding-left:.22in;font-size:10.5pt}.crow.xr{color:#3a4856}.xref{font-size:.9em;color:var(--muted)}
ul.corr{margin:.04in 0 .06in;padding-left:.22in}ul.corr li{margin:0 0 .05in}
p:has(> em:first-child:last-child),.cmeta,section.f-21 li,section.f-22 li{text-align:left;hyphens:manual}
.cpn{display:inline-block;width:.42in;font:600 9pt 'Mono';color:var(--muted)}
p{margin:0 0 .13in;text-align:justify;hyphens:auto;orphans:3;widows:4}
ul,ol{margin:0 0 .14in;padding-left:.28in}li{margin:0 0 .06in}li>p{margin:0 0 .05in}
blockquote{margin:.12in 0 .16in .2in;padding-left:.14in;border-left:2pt solid var(--rule);color:#2b3a4a}
code{font-family:'Mono','DejaVu Sans Mono',monospace;font-size:.86em;overflow-wrap:anywhere}
pre{font-family:'Mono','DejaVu Sans Mono','Noto Color Emoji',monospace;font-size:9pt;line-height:1.5;max-width:100%;white-space:break-spaces;overflow-wrap:anywhere;margin:.1in 0 .16in;padding:0}
pre code{font-size:inherit}
table{border-collapse:collapse;width:100%;max-width:100%;margin:.12in 0 .22in;font:400 9.5pt/1.45 'Sans','Noto Sans CJK SC',sans-serif}
th{font-weight:600;text-align:left;border-bottom:1pt solid var(--ink);padding:5pt 7pt 5pt 0;vertical-align:bottom}
td{border-bottom:.5pt solid var(--rule);padding:5pt 7pt 5pt 0;vertical-align:top;overflow-wrap:anywhere;hyphens:auto}
tr{break-inside:avoid}
td code,th code{font-size:.92em}
a{color:inherit;text-decoration:none}
a[href^='http']{color:#1d3f8f;word-break:break-all}
p,li,td,dd,.v,.tx,.ixs{overflow-wrap:anywhere}
math[display='block']{display:block;max-width:100%;margin:.1in 0}
.cblock{margin:0 0 .2in;break-inside:auto}.cblock h4.cm{margin:.18in 0 .05in;font-size:11.5pt;border-bottom:.6pt solid var(--rule);padding-bottom:2pt}.lab{font:600 9.5pt 'Sans';color:var(--accent)}.cblock p{text-align:left;hyphens:manual}.cblock p.recs{font-size:9.5pt;text-align:left}.cblock p.recs code{font-size:.95em}
.rblock{margin:0 0 .14in;padding:.06in 0 .04in;border-top:.6pt solid var(--rule);break-inside:avoid;font:400 9.5pt/1.45 'Sans'}.rblock .rh{font-weight:600;margin-bottom:2pt}.rblock .f{display:flex;gap:8pt}.rblock .k{flex:0 0 1.55in;color:var(--muted)}.rblock .v{flex:1}
hr{border:0;border-top:.6pt solid var(--rule);margin:.24in 0}
img{max-width:100%}
sup{font-size:.7em;line-height:0}
.pg{font:500 .88em 'Mono';color:var(--muted);white-space:nowrap}
.mk{position:absolute;font-size:1px;line-height:1px;color:#fff;letter-spacing:0;white-space:nowrap}
.anc{break-after:avoid;height:0;margin:0}
section.titlepage{page:title;height:7.8in;display:flex;flex-direction:column;font-family:'Sans'}
.tp-series{font:500 8.5pt 'Mono';letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-top:.9in}
.tp-title{font:800 42pt/1 'Sans';color:var(--accent);margin-top:.35in;letter-spacing:-.02em}
.tp-sub2{font:600 19pt 'Sans';color:var(--accent);margin-top:.14in;padding-bottom:.2in;border-bottom:1.6pt solid var(--accent);width:60%}
.tp-ed{font:600 14pt 'Sans';margin-top:.55in}
.tp-with{font:400 12pt 'Sans';color:#2b3a4a;margin-top:.1in}
.tp-spacer{flex:1}
.tp-pub{font:italic 600 14pt 'Serif'}
.tp-proof{margin-top:.5in;font:500 8.5pt 'Mono';color:var(--red)}
section.copyright{page:title;break-before:page;break-after:page;font-size:8.6pt;line-height:1.45;padding-top:.2in}
section.copyright p{text-align:left;margin:0 0 .09in}
section.contents h1{break-before:page}
.cgrp{font:700 8.5pt 'Mono';letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:.34in 0 .1in;padding-bottom:3pt;border-bottom:.8pt solid var(--accent);break-after:avoid}
.crow{display:flex;align-items:baseline;gap:5pt;margin:0 0 3pt;break-inside:avoid;color:inherit}
.crow .ct{flex:0 1 auto;min-width:0}.crow .dots{flex:1;border-bottom:.6pt dotted #9aa5b1;transform:translateY(-3pt)}.crow .cn{font:500 9pt 'Mono';white-space:nowrap;flex:0 0 auto}
.crow.l1{font:500 11pt 'Sans';margin-top:6pt}.crow.l2{font:400 9.5pt 'Sans';padding-left:.22in;color:#2b3a4a}
.sign{text-align:left;font-style:italic;margin-top:.2in}
.placeholder{border:1pt dashed var(--red);padding:.06in .1in}
'''

from common import pandoc, recast_tables

def files_in_order():
    m = json.loads((SRC / 'editions' / 'pdf.json').read_text())
    return [f['file'] for f in m['files']]

def front_matter_split(md):
    """Replace the draft's title block (lines before the Series Preface) with typeset title, copyright and contents pages."""
    i = md.index('\n# Contributors') if '\n# Contributors' in md else md.index('\n# Series Preface')
    head, rest = md[:i], md[i:]
    cp = head[head.index('## Copyright page'):].split('\n', 1)[1]
    cp = re.sub(r'\n---\s*$', '', cp.strip())
    ver = re.search(r'edition: "([^"]+)"', head)
    return cp, (ver.group(1) if ver else ''), rest

TITLE = """<section class="titlepage"><div class="tp-series">Aikipedia · Annual Collections · Series Volume 1</div>
<div class="tp-title">Aikipedia 2025</div><div class="tp-sub2">Annual Collection</div>
<div class="tp-ed">Edited by W.H.L.</div><div class="tp-with">with Claude Opus 5.5, GPT-6 Astra, and Muse Spark 1.3</div>%PROOF%<div class="tp-spacer"></div><div class="tp-pub">Champaign Magazine</div></section>"""

ORDER = [  # (group label, title prefixes) in the order the volume is printed
    ('Opening', ['Series Preface', 'Volume Preface', 'Annual Introduction', 'Contributors']),
    ('Using the Collection', ['How to Use', 'Collection at a Glance', 'The 2025 Publications', 'Alphabetical Table of Contents', 'Thematic Table of Contents']),
    ('The Reference Collection', ['Part ']),
    ('The Historical Record', ['Historical Lexicon Archive']),
    ('Sources and Editorial Record', ['References', 'Corrections and Editorial', 'Editorial Method', 'AI Disclosure', 'Appendix', 'Alphabetical Index']),
]
ROMAN = {'I': 'I', 'II': 'II', 'III': 'III', 'IV': 'IV', 'V': 'V', 'VI': 'VI'}
plain = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()

def split_h1(h):
    out, pos = [], [m.start() for m in re.finditer(r'<h1[ >]', h)]
    if not pos: return [h]
    if h[:pos[0]].strip(): out.append(h[:pos[0]])
    for a, b in zip(pos, pos[1:] + [len(h)]): out.append(h[a:b])
    return out

def group_of(title):
    for gi, (g, prefixes) in enumerate(ORDER):
        for pi, p in enumerate(prefixes):
            if title.startswith(p): return gi, pi
    raise SystemExit(f'no group for section {title!r}')

def recbar(title_h3, table, concept, later=False):
    code = re.search(r'<code>(.*?)</code>', title_h3)
    rid = code.group(1) if code else ''
    ttl = plain(re.sub(r'\s*—\s*<code>.*?</code>', '', title_h3))
    cols = [plain(c) for c in re.findall(r'<th[^>]*>(.*?)</th>', table, re.S)]
    vals = re.findall(r'<td[^>]*>(.*?)</td>', table, re.S)
    meta = ''.join(f'<span class="m"><span class="k">{html.escape(c)}</span> {v}</span>' for c, v in zip(cols, vals))
    t2 = '' if (ttl == concept and not later) else f'<div class="rt">{html.escape(ttl)}</div>'
    return f'<div class="recbar"><div class="rid">{rid}</div>{t2}<div class="rm">{meta}</div></div>'

def split_corrections(h):
    """Give each correction ID its own line in the correction lists; the wording is unchanged."""
    def li(m):
        body = m.group(1)
        if not body.startswith('Correction IDs') or '<strong>AIK-' not in body: return m.group(0)
        i = body.index('<strong>AIK-')
        items = re.split(r' · (?=<strong>/?(?:C|ST|E)\d)', body[i:])
        return f'<li>{body[:i].rstrip()}<ul class="corr">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></li>'
    return re.sub(r'<li>(.*?)</li>', li, h, flags=re.S)

def entry_transform(h):
    """Reference-collection pages: one headword, a compact identification bar per record, then the entry."""
    out, concept = [], ''
    for seg in re.split(r'(?=<h2 )', h):
        m = re.match(r'<h2[^>]*>(.*?)</h2>', seg, re.S)
        if m: concept = plain(re.sub(r'<span class="mk">.*?</span>', '', m.group(1)))
        seg = re.sub(r'<p><em>(Internal Concept ID[^<]*)</em></p>', r'<p class="cmeta">\1</p>', seg)
        later = iter(range(10**6))
        seg = re.sub(r'<h3 id="[^"]*">(.*?)</h3>\s*<table[^>]*>(.*?)</table>', lambda x: recbar(x.group(1), x.group(2), concept, next(later) > 0), seg, flags=re.S)
        k = iter(range(10**6))
        seg = re.sub(r'<p><a id="aik-', lambda x: ('<div class="pbreak"></div>' if next(k) > 0 else '') + x.group(0), seg)
        seg = re.sub(r'<h4 id="([^"]*)">(.*?)</h4>', lambda x: f'<h4 id="{x.group(1)}" class="rlabel{" dup" if plain(x.group(2)) == concept else ""}">{x.group(2)}</h4>', seg, flags=re.S)
        seg = re.sub(r'<table[^>]*>(\s*<colgroup>.*?</colgroup>)?(\s*<thead>\s*<tr[^>]*>\s*<th[^>]*>Field</th>)', r'<table class="edrec">\1\2', seg, flags=re.S)
        out.append(seg)
    return ''.join(out)

def archive_transform(h):
    """Archive pages: line labels set in a margin column; the captured text is not changed."""
    def pre(m):
        lines = m.group(1).split('\n')
        rows = []
        for ln in lines:
            x = re.match(r'(A-\d{3,4})  (.*)$', ln)
            if x: rows.append(f'<div class="al"><span class="ln">{x.group(1)}</span><span class="tx">{x.group(2) or "&#8203;"}</span></div>')
            else: rows.append(f'<div class="al"><span class="ln"></span><span class="tx">{ln or "&#8203;"}</span></div>')
        return '<div class="arch">' + ''.join(rows) + '</div>'
    return re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', pre, h, flags=re.S)

def index_transform(h, pages):
    """Index: the term and its page numbers lead; IDs and related terms sit beneath; 'see' lines link to their target."""
    terms = {}
    for m in re.finditer(r'<li>(.*?)</li>', h, re.S):
        b = m.group(1); ids = re.findall(r'<a href="#(aik-[^"]+)"', b.split('<em>See also:</em>')[0])
        t = re.match(r'\s*<strong>(.*?)</strong>', b)
        if ids and t: terms[plain(t.group(1))] = ids[0]
    def li(m):
        body = m.group(1)
        ids = re.findall(r'<a href="#(aik-[^"]+)"', body.split('<em>See also:</em>')[0])
        if not ids:
            def link(x):
                tgt = terms.get(plain(x.group(1)))
                return f'<a href="#{tgt}"><strong>{x.group(1)}</strong></a>' if tgt else x.group(0)
            body = re.sub(r'<strong>(.*?)</strong>', link, body)
            return f'<li class="ixsee">{body}</li>'
        head = body.split(' — <a', 1)[0]
        rest = body[len(head):].lstrip(' —')
        first = {}
        for i in ids:
            if pages.get(i): first.setdefault(pages[i], i)
        pgl = ', '.join(f'<a href="#{first[n]}">{n}</a>' for n in sorted(first)) or f'<a href="#{ids[0]}">000</a>'
        return (f'<li class="ix"><div class="ixr"><span class="ixt">{head}</span><span class="dots"></span><span class="ixp">{pgl}</span></div>'
                f'<div class="ixs">{rest}</div></li>')
    return re.sub(r'<li>(.*?)</li>', li, h, flags=re.S)

def build_html(pages):
    """pages: dict key -> page number, from the previous pass (empty on pass 1)."""
    pages = pages or {}
    chunks, ids, pre = [], [], ''
    for fn in files_in_order():
        md = (SRC / fn).read_text(encoding='utf-8')
        if fn == '00_front-matter.md':
            cp, ver, md = front_matter_split(md)
            proof = f'<div class="tp-proof">{html.escape(ver)}</div>' if 'draft' in ver else ''
            pre = TITLE.replace('%PROOF%', proof) + f'<section class="copyright">{pandoc(cp)}</section>' + '<section class="contents"><h1 class="nob">Contents</h1>%CONTENTS%</section>'
        h = recast_tables(pandoc(md))
        if fn == '01_tables-of-contents.md':
            h = re.sub(r'<li><a href="#([^"]+)" class="thm">(.*?)</a></li>', lambda m: f'<li class="thm"><a class="orow" href="#{m.group(1)}"><span class="ct">{m.group(2)}</span><span class="dots"></span><span class="cn">{pages.get(m.group(1), "000")}</span></a></li>', h)
            h = re.sub(r'<a href="#([^"]+)"(?! class="orow")[^>]*>.*?</a>', lambda m: '<span class="idp">' + m.group(0) + f'<span class="pg"> p.&#160;{pages.get(m.group(1), "000")}</span></span>', h)
            h = re.sub(r'<table[^>]*>\s*(?:<colgroup>.*?</colgroup>)?', '<table class="atoc"><colgroup><col style="width:40%"><col style="width:7%"><col style="width:53%"></colgroup>', h, count=1, flags=re.S)
        if fn == '23_index-of-terms.md':
            h = index_transform(h, pages)
        if fn[0] == '1': h = entry_transform(h)
        if fn.startswith('20'): h = archive_transform(h)
        if fn[:2] in ('21', '22'): h = split_corrections(h)
        ids += re.findall(r'<a id="(aik-[^"]+)"', h)
        for c in split_h1(h):
            t = plain(re.sub(r'<span class="mk">.*?</span>', '', (re.search(r'<h1[^>]*>(.*?)</h1>', c, re.S) or [None, ''])[1]))
            chunks.append((group_of(t), fn[:2], t, c))
    chunks.sort(key=lambda x: x[0])          # stable: keeps source order within a group position
    idx = {a: i for i, a in enumerate(dict.fromkeys(ids))}
    toc, secs = [], []
    for ci, ((gi, _), fp, title, c) in enumerate(chunks):
        g = ORDER[gi][0]
        lv = ('1', '2') if fp[0] == '1' or fp == '20' or title == 'AI Disclosure' else ('1',)
        def mark(m, fp=fp, ci=ci, g=g):
            level, hid, inner = m.group(1), m.group(2), m.group(4)
            if level not in lv: return m.group(0)
            key = f'h:{ci}:{hid}'
            n = idx.setdefault(key, len(idx))
            toc.append((g, level, plain(inner), key, fp))
            return f'<h{level} id="{hid}"{m.group(3)}><a id="toc{n}"></a>{inner}<span class="mk">QQ{n:04d}QQ</span></h{level}>'
        c = re.sub(r'<h([12]) id="([^"]+)"([^>]*)>(.*?)</h\1>', mark, c, flags=re.S)
        if fp[0] == '1':     # part opener: numeral, title, and the part's concepts with their pages
            m = re.search(r'<h1 id="([^"]+)"[^>]*>(.*?)</h1>', c, re.S)
            pm = re.match(r'Part ([IVX]+)\.\s*(.*)', title)
            heads = [(t, k) for (gg, lvl, t, k, f2) in toc if lvl == '2' and k.startswith(f'h:{ci}:')]
            segs = re.split(r'(?=<h2 )', c); newk = set()
            for sgm in segs:
                mm = re.search(r'<a id="toc(\d+)"></a>', sgm)
                if mm and 'id="aik-2025-f-n-' in sgm: newk.add(int(mm.group(1)))
            rows = ''.join(f'<a class="orow" href="#toc{idx[k]}"><span class="ct">{html.escape(t)}{" ◆" if idx[k] in newk else ""}</span><span class="dots"></span><span class="cn">{pages.get(k, "000")}</span></a>' for t, k in heads)
            inner = re.search(r'(<a id="toc\d+"></a>).*?(<span class="mk">.*?</span>)', m.group(2), re.S)
            op = (f'<div class="opener"><h1 id="{m.group(1)}" class="ptitle">{inner.group(1)}<span class="pnum">Part {pm.group(1)}</span>'
                  f'<span class="pname">{html.escape(pm.group(2))}</span>{inner.group(2)}</h1><div class="olist">{rows}</div></div>')
            c = c[:m.start()] + op + c[m.end():]
        if fp == '20':
            heads = [(t, k) for (gg, lvl, t, k, f2) in toc if lvl == '2' and k.startswith(f'h:{ci}:')]
            rows = ''.join(f'<a class="orow" href="#toc{idx[k]}"><span class="ct">{html.escape(t)}</span><span class="dots"></span><span class="cn">{pages.get(k, "000")}</span></a>' for t, k in heads)
            j2 = c.find('<h2 ')
            c = c[:j2] + f'<div class="alist"><div class="cgrp">The sixteen posts</div>{rows}</div>' + c[j2:]
        secs.append(f'<section class="f-{fp} g{gi}">{c}</section>')
    body = pre + '\n'.join(secs)
    body = re.sub(r'<hr\s*/?>\s*(?=<h[12]|<div class="opener")', '', body)
    body = re.sub(r'<p>(<a id="aik-[^"]+"></a>)</p>', r'<div class="anc">\1</div>', body)
    body = re.sub(r'(<a id="(aik-[^"]+)"></a>)', lambda m: m.group(1) + f'<span class="mk">QQ{idx[m.group(2)]:04d}QQ</span>', body)
    # main contents: five groups, sections only
    rows, cur, apx = [], None, False
    appf = next((k for g, l, t, k, f in toc if l == '1' and t.startswith('Appendix F')), None)
    row = lambda key, label, cls='l1': f'<a class="crow {cls}" href="#toc{idx[key]}"><span class="ct">{label}</span><span class="dots"></span><span class="cn">{pages.get(key, "000")}</span></a>'
    for g, level, text, key, fp in toc:
        if level == '2' and fp == '00' and text.startswith('5.5'): rows.append(row(key, html.escape(text), 'l2')); continue
        if level != '1': continue
        if g != cur:
            if cur == 'The Historical Record' and appf:
                rows.append(f'<a class="crow l1 xr" href="#toc{idx[appf]}"><span class="ct">Related editorial material — see Appendix F</span></a>')
            rows.append(f'<div class="cgrp">{g}</div>'); cur = g
        label = html.escape(text)
        pm = re.match(r'Part ([IVX]+)\.\s*(.*)', text)
        am = re.match(r'Appendix ([A-G])\.\s*(.*)', text)
        if pm: label = f'<span class="cpn">{pm.group(1)}</span>{html.escape(pm.group(2))}'
        if am:
            if not apx: rows.append('<div class="csub">Appendices</div>'); apx = True
            rows.append(row(key, f'<span class="cpn">{am.group(1)}</span>{html.escape(am.group(2))}', 'l1 ap')); continue
        rows.append(row(key, label))
    body = body.replace('%CONTENTS%', ''.join(rows), 1)
    body = re.sub(r'<hr\s*/?>\s*(?=</section>|<div class="pbreak">)', '', body)  # no closing separator lines (editor, Nov 17, 14:28 CT)
    global LAST_TOC, HEADINGS; LAST_TOC = [(g, l, t, k) for g, l, t, k, f in toc]
    HEADINGS = [plain(re.sub(r'<span class="mk">.*?</span>', '', x)) for x in re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', body, re.S)]
    doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Aikipedia 2025: Annual Collection</title><style>{CSS}</style></head><body>{body}</body></html>'
    return doc, {i: a for a, i in idx.items()}

async def render(doc, pdf):
    f = WORK / 'volume.html'; f.write_text(doc, encoding='utf-8')
    async with async_playwright() as p:
        b = await p.chromium.launch(); ctx = await b.new_context(); ctx.set_default_timeout(0)
        pg = await ctx.new_page()
        await pg.goto(f.as_uri(), wait_until='load', timeout=600000)
        await pg.wait_for_timeout(1500)
        await pg.emulate_media(media='print')
        await pg.set_viewport_size({'width': CONTENT_PX, 'height': 1000})
        await pg.evaluate('''()=>{for(const m of document.querySelectorAll('math')){const box=m.parentElement.clientWidth; if(m.scrollWidth>box){m.style.fontSize=(Math.floor(1000*box/m.scrollWidth)/10)+'%';}}}''')
        over = await pg.evaluate('''()=>{const W=document.documentElement.clientWidth;const o=[];for(const e of document.querySelectorAll('body *')){if(e.classList.contains('mk')||e.closest('.mk'))continue;const r=e.getBoundingClientRect();if(r.right>W+0.5)o.push(e.tagName+' '+(e.textContent||'').slice(0,60).replace(/\\s+/g,' '));}return [document.documentElement.scrollWidth,W,o.slice(0,8),o.length];}''')
        if over[3]:
            print('OVERFLOW', over); raise SystemExit('content wider than the text column: Chrome would shrink the whole volume')
        await pg.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True, tagged=True, outline=True)
        await b.close()

def locate(pdf, rev):
    found = {}
    for n, page in enumerate(PdfReader(str(pdf)).pages, start=1):
        for m in re.finditer(r'QQ(\d{4})QQ', (page.extract_text() or '').replace(' ', '').replace('\n', '')):
            found.setdefault(rev[int(m.group(1))], n)
    return found

def cover_pdf():
    im = Image.open(SRC / 'assets' / 'cover.png').convert('RGB')
    W, H = 7 * 200, 10 * 200
    bg = im.getpixel((5, im.size[1] // 2))
    s = H / im.size[1]
    im2 = im.resize((round(im.size[0] * s), H))
    can = Image.new('RGB', (W, H), bg); can.paste(im2, ((W - im2.size[0]) // 2, 0))
    p = WORK / 'cover.pdf'; can.save(p, 'PDF', resolution=200); return p

def running_heads(src, dst, pages):
    """Stamp running heads: the current group or part on the left, the current section or entry on the right."""
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    import io
    rd = PdfReader(str(src)); n = len(rd.pages)
    marks = sorted(((pages[k], lvl, g, re.sub(r'<[^>]+>', '', t)) for g, lvl, t, k in LAST_TOC if k in pages), key=lambda x: (x[0], x[1]))
    left, right, cur1, cur2, cg = {}, {}, '', '', ''
    j = 0
    for pg in range(1, n + 1):
        while j < len(marks) and marks[j][0] <= pg:
            _, lvl, g, t = marks[j]; j += 1
            if lvl == '1': cur1, cur2, cg = t, '', g
            else: cur2 = t
        left[pg] = (cur1 if g_is_part(cur1) else cg) or 'Aikipedia 2025'
        right[pg] = cur2 or cur1
    starts = {p for p, lvl, g, t in marks if lvl == '1'}
    w = PdfWriter(clone_from=str(src))     # keeps Chrome's bookmarks, link annotations and named destinations
    fit = lambda t, k: (t if len(t) <= k else t[:k - 1].rstrip() + '…')
    for i, page in enumerate(w.pages, start=1):
        if i > 3 and i not in starts:      # no heads on the title, copyright and first contents pages, or on a section's opening page
            buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(7 * inch, 10 * inch))
            c.setFillColorRGB(.45, .5, .56); c.setFont('Helvetica', 7.2)
            y = 10 * inch - 0.62 * inch
            from reportlab.pdfbase.pdfmetrics import stringWidth as _sw
            room = (7 - 0.95 - 0.85) * inch
            def fitw(s):
                while s and _sw(s, 'Helvetica', 7.2) > room: s = s[:-2].rstrip() + '…' if not s.endswith('…') else s[:-2].rstrip() + '…'
                return s
            # facing pages (editor's ruling, November 18, 2026, 13:01 CT): the volume and the group or Part on the
            # left-hand (even-numbered) page, the current section or entry on the right-hand (odd-numbered) page
            printed = i                    # the page's printed number: the cover is added after this step, unnumbered
            if printed % 2 == 0:
                lp = left[i].upper(); lt = 'AIKIPEDIA 2025' if lp == 'AIKIPEDIA 2025' else 'AIKIPEDIA 2025  ·  ' + lp
                c.drawString(0.95 * inch, y, fitw(lt))
            else:
                c.drawRightString(7 * inch - 0.85 * inch, y, fitw(right[i] or left[i]))
            c.setStrokeColorRGB(.82, .85, .88); c.setLineWidth(.4); c.line(0.95 * inch, y - 5, 7 * inch - 0.85 * inch, y - 5)
            c.save(); buf.seek(0); page.merge_page(PdfReader(buf).pages[0])
            page.compress_content_streams()
    # bookmarks: Chrome joins a wrapped heading's lines without a space ("WeCould"); restore each title from the heading text
    # v1.0.1: matched without regard to case (Part titles and lexicon record heads are set in capitals by CSS, so the
    # bookmark's case differs from the heading text); the spaces are restored and the bookmark's own case is kept
    heads = {re.sub(r'\s+', '', t).lower(): t for t in HEADINGS}
    def respace(orig, head):
        chars = [c for c in orig if not c.isspace()]; out = []; j = 0
        for c in head:
            if c.isspace():
                if out and out[-1] != ' ': out.append(' ')
            else: out.append(chars[j]); j += 1
        return ''.join(out).strip()
    from pypdf.generic import NameObject, TextStringObject
    def walk(node):
        while node is not None:
            node = node.get_object(); t = node.get('/Title')
            if t is not None:
                k = re.sub(r'\s+', '', str(t)).lower()
                if k in heads:
                    new = respace(str(t), heads[k])
                    # a Part heading's numeral and title are separate elements with no space between them
                    new = re.sub(r'^(PART [IVX]+)(?=[A-Z][a-z])', r'\1 ', new)
                    if new != str(t): node[NameObject('/Title')] = TextStringObject(new); FIXED.append(new)
            if node.get('/First') is not None: walk(node['/First'])
            node = node.get('/Next')
    ol = w._root_object.get('/Outlines')
    if ol is not None and ol.get_object().get('/First') is not None: walk(ol.get_object()['/First'])
    # a trailing page with no text (the index's closing break) is dropped
    while len(w.pages) > 1 and not (w.pages[-1].extract_text() or '').strip(): w.remove_page(len(w.pages) - 1); FIXED.append('trailing blank page removed')
    w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    with open(dst, 'wb') as fh: w.write(fh)

def g_is_part(t): return t.startswith('Part ')
FIXED = []

def main():
    p1 = WORK / 'pass1.pdf'
    doc, rev = build_html(None); asyncio.run(render(doc, p1))
    pages = locate(p1, rev)
    print('pass 1:', len(PdfReader(str(p1)).pages), 'pages;', len(pages), 'of', len(rev), 'anchors located')
    p2 = WORK / 'pass2.pdf'
    doc, rev = build_html(pages); asyncio.run(render(doc, p2))
    pages2 = locate(p2, rev)
    moved = {a for a in pages if pages2.get(a) != pages[a]}
    print('pass 2:', len(PdfReader(str(p2)).pages), 'pages; moved anchors:', len(moved))
    if moved:
        doc, rev = build_html(pages2); asyncio.run(render(doc, p2)); pages = pages2
        pages3 = locate(p2, rev); print('pass 3: moved', sum(pages3.get(a) != pages2[a] for a in pages2))
    # final render without the locating markers, checked page by page against the marked render
    final_pages = pages if not moved else pages2
    doc, rev = build_html(final_pages); doc = re.sub(r'<span class="mk">QQ\d{4}QQ</span>', '', doc)
    p4 = WORK / 'final.pdf'; asyncio.run(render(doc, p4))
    A, B = PdfReader(str(p2)).pages, PdfReader(str(p4)).pages
    norm = lambda x: re.sub(r'QQ\d{4}QQ', '', re.sub(r'\s+', '', x.extract_text() or ''))
    diff = [i + 1 for i in range(min(len(A), len(B))) if norm(A[i])[:60] != norm(B[i])[:60]]
    print('final render:', len(B), 'pages; pages whose opening differs from the marked render:', diff[:10], len(diff))
    for i in diff[:3]: print('  p', i, '|', norm(A[i-1])[:60], '|', norm(B[i-1])[:60])
    assert len(A) == len(B), 'removing the markers changed the page count'
    p5 = WORK / 'final_heads.pdf'; running_heads(p4, p5, final_pages)
    w = PdfWriter(); w.append(str(cover_pdf())); w.append(str(p5))
    w.set_page_label(0, 0, prefix='Cover')
    w.set_page_label(1, len(w.pages) - 1, style='/D', start=1)
    w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    w.add_metadata({'/Title': 'Aikipedia 2025: Annual Collection', '/Author': 'Edited by W.H.L.', '/Subject': 'Aikipedia, Series Volume 1', '/Creator': 'Champaign Magazine'})
    print('heads step:', len([x for x in FIXED if x != 'trailing blank page removed']), 'bookmark titles restored;', [x for x in FIXED if x == 'trailing blank page removed'])
    out = OUT / f'{STEM}.pdf'
    with open(out, 'wb') as fh: w.write(fh)
    (OUT / 'anchor_pages.json').write_text(json.dumps(pages if not moved else pages2, indent=0))
    print('wrote', out, len(PdfReader(str(out)).pages), 'pages')

if __name__ == "__main__":
    main()

"""Shared conversion steps for the PDF and online editions of Aikipedia 2025.

Markdown repairs here change layout only, never wording: they make lists and headings parse as the source
intends (pandoc's Markdown needs a blank line before a list or after a raw HTML anchor), and they leave fenced
code blocks (the archive transcriptions) untouched.
"""
import html, re, subprocess

LIST = re.compile(r'^(\s{0,3}[-*+] |\s{0,3}\d+[.)] )')

def preprocess(md):
    out, fence = [], False
    lines = md.split('\n')
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith('```'):
            fence = not fence
        if not fence and i and LIST.match(ln):
            prev = lines[i - 1]
            if prev.strip() and not LIST.match(prev) and not prev.startswith((' ', '\t', '|', '>')):
                out.append('')
        out.append(ln)
    md = '\n'.join(out)
    md = fence_labelled_lines(md)
    # list items that quote a post's heading ("- ## Overview (A-003)") are list text, not headings (v0.21 review, M2)
    md = re.sub(r'^([-*] )(#{1,6} )', lambda m: m.group(1) + '\\' + m.group(2), md, flags=re.M)
    md = re.sub(r'^(<a id="[^"]+"></a>)\n(?=\S)', r'\1\n\n', md, flags=re.M)
    md = re.sub(r'^> \*\*\[PLACEHOLDER — index page numbers\]\*\*[^\n]*\n', '', md, flags=re.M)
    md = re.sub(r'^(W\.H\.L\.)\n(November 2026)\n([\w.]+@[\w.]+)$', r'<p class="sign">\1<br>\2<br><br><a href="mailto:\3">\3</a></p>', md, flags=re.M)
    md = re.sub(r'^(W\.H\.L\.)\n(November 2026)\n\[([\w.]+@[\w.]+)\]\(mailto:[\w.]+@[\w.]+\)$', r'<p class="sign">\1<br>\2<br><br><a href="mailto:\3">\3</a></p>', md, flags=re.M)
    md = re.sub(r'^(W\.H\.L\.)\n(November 2026)$', r'<p class="sign">\1<br>\2</p>', md, flags=re.M)
    return md

LABEL = re.compile(r'^A-\d{3,4}(  |$)')

def fence_labelled_lines(md):
    """Archive texts filed with A-nnn labelled lines outside a code fence would be re-flowed into paragraphs.
    Put each run of labelled lines in a fence, so every captured line is shown as captured. Consecutive
    '**Label:** value' header lines get hard line breaks so they are not run together."""
    out, run, fence = [], [], False
    def flush():
        if run:
            out.append('```text'); out.extend(run); out.append('```'); run.clear()
    lines = md.split('\n')
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith('```'):
            flush(); fence = not fence; out.append(ln); continue
        if not fence and LABEL.match(ln):
            run.append(ln); continue
        flush()
        if not fence and re.match(r'^\*\*[^*]+:\*\*', ln) and i + 1 < len(lines) and re.match(r'^\*\*[^*]+:\*\*', lines[i + 1]) and not ln.endswith('  '):
            ln += '  '
        out.append(ln)
    flush()
    return '\n'.join(out)

def pandoc(md):
    h = subprocess.run(['pandoc', '-f', 'markdown-yaml_metadata_block-smart-implicit_figures+raw_html+autolink_bare_uris',
                        '-t', 'html5', '--wrap=none', '--mathml'],
                       input=preprocess(md), capture_output=True, text=True, check=True).stdout
    # an automatic heading id must not collide with a record anchor (e.g. a heading that is itself a record ID)
    h = re.sub(r'(<h[1-6] id=")(aik-2025-[^"]+")', r'\1cr-\2', h)
    return subscripts(h)

# The two restored C06 formulas (Mixture of Experts; Test-Time Compute Scaling) are carried as plain text with TeX-style
# subscript markup. Set the subscripts as subscripts: the characters are unchanged, only their presentation (GPT audit 17).
SUBS = [('Σ_{i ∈ TopK(G(x))} G_i(x) · E_i(x)', 'Σ<sub>i ∈ TopK(G(x))</sub> G<sub>i</sub>(x) · E<sub>i</sub>(x)'),
        ('argmax_{y ∈ 𝒴(x, C)} R(y)', 'argmax<sub>y ∈ 𝒴(x, C)</sub> R(y)'),
        ('where E_i(x) is the output of expert i, and G_i(x) is the gating weight', 'where E<sub>i</sub>(x) is the output of expert i, and G<sub>i</sub>(x) is the gating weight')]

def subscripts(h):
    # outside <pre> and <code> only: the archive transcriptions are shown as captured
    parts = re.split(r'(<pre[\s>].*?</pre>|<code[\s>].*?</code>)', h, flags=re.S)
    for i in range(0, len(parts), 2):
        for a, b in SUBS: parts[i] = parts[i].replace(a, b)
    return ''.join(parts)

def _cells(row, tag):
    return re.findall(rf'<{tag}[^>]*>(.*?)</{tag}>', row, re.S)

def recast_tables(h):
    """Recast tables too wide for a book column as readable blocks, keeping every field.
    The contributor table becomes one block per model (Roles, Records); any table of seven or more
    columns becomes one record block per row, each field labelled with its column heading."""
    def fix(m):
        t = m.group(0)
        head = re.search(r'<thead>(.*?)</thead>', t, re.S)
        if not head: return t
        cols = [re.sub(r'<[^>]+>', '', c).strip() for c in _cells(head.group(1), 'th')]
        rows = [_cells(r, 'td') for r in re.findall(r'<tr[^>]*>(.*?)</tr>', re.search(r'<tbody>(.*?)</tbody>', t, re.S).group(1), re.S)]
        if cols[:1] == ['Model (as credited)']:
            return ''.join(f'<div class="cblock"><h4 class="cm">{r[0]}</h4><p><span class="lab">Roles.</span> {r[1]}</p>'
                           f'<p class="recs"><span class="lab">Records.</span> {r[2]}</p></div>' for r in rows if len(r) >= 3)
        if len(cols) >= 7:
            out = []
            for r in rows:
                title = ' · '.join(x for x in r[:3] if x.strip())
                fields = ''.join(f'<div class="f"><span class="k">{html.escape(c)}</span><span class="v">{v}</span></div>' for c, v in zip(cols[3:], r[3:]))
                out.append(f'<div class="rblock"><div class="rh">{title}</div>{fields}</div>')
            return '<div class="rblocks">' + ''.join(out) + '</div>'
        return t
    return re.sub(r'<table[^>]*>.*?</table>', fix, h, flags=re.S)


def split_corrections(h):
    """Give each correction ID its own line in the correction lists; the wording is unchanged."""
    def li(m):
        body = m.group(1)
        if not body.startswith('Correction IDs') or '<strong>AIK-' not in body: return m.group(0)
        i = body.index('<strong>AIK-')
        items = re.split(r' · (?=<strong>/?(?:C|ST|E)\d)', body[i:])
        return f'<li>{body[:i].rstrip()}<ul class="corr">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></li>'
    return re.sub(r'<li>(.*?)</li>', li, h, flags=re.S)


ORDER = [  # (group label, title prefixes) in the order the volume is presented
    ('Opening', ['Series Preface', 'Volume Preface', 'Annual Introduction', 'Contributors']),
    ('Using the Collection', ['How to Use', 'Collection at a Glance', 'The 2025 Publications', 'Alphabetical Table of Contents', 'Thematic Table of Contents']),
    ('The Reference Collection', ['Part ']),
    ('The Historical Record', ['Historical Lexicon Archive']),
    ('Sources and Editorial Record', ['References', 'Corrections and Editorial', 'Editorial Method', 'AI Disclosure', 'Appendix', 'Alphabetical Index']),
]

def group_of(title):
    for gi, (g, prefixes) in enumerate(ORDER):
        for pi, p in enumerate(prefixes):
            if title.startswith(p): return gi, pi
    return None

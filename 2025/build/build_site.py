"""Build the online edition of Aikipedia 2025: Annual Collection as static web pages.

Input: a collection draft directory (editions/online.json lists the online edition's files in order).
Output: <out>/ — one page per section (the archive split into one page per original post), a contents
page, a search page with its data file, the stylesheet and the cover. Internal links are rewritten to
point at the page that holds each anchor.
"""
import html, json, pathlib, re, shutil, subprocess, sys

SRC = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); PDFNAME = sys.argv[3] if len(sys.argv) > 3 else ''
TS = pathlib.Path(__file__).parent
E = lambda s: html.escape(s or '', quote=True)
OUT.mkdir(parents=True, exist_ok=True); (OUT / 'assets').mkdir(exist_ok=True); (OUT / 'data').mkdir(exist_ok=True)

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import pandoc, split_corrections, ORDER, group_of

def slug(s):
    s = re.sub(r'<[^>]+>', '', s).lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:60]

def split_h1(h):
    """Split an HTML fragment into (title, id, html) pieces at each h1."""
    out = []
    for m in re.finditer(r'<h1 id="([^"]*)"[^>]*>(.*?)</h1>(.*?)(?=<h1 |\Z)', h, re.S):
        out.append((re.sub(r'<[^>]+>', '', m.group(2)), m.group(1), m.group(0)))
    return out

meta = json.loads((SRC / 'editions' / 'online.json').read_text())
_ed = re.search(r'edition: "([^"]+)"', (SRC / '00_front-matter.md').read_text(encoding='utf-8'))
BANNER = f'<div class="banner">Proof: {E(_ed.group(1))}. This is not the released edition.</div>' if _ed and 'draft' in _ed.group(1) else ''
pages = []   # (filename, title, html, group)
for f in [x['file'] for x in meta['files']]:
    md = (SRC / f).read_text(encoding='utf-8')
    if f == '00_front-matter.md':
        md = re.sub(r'^---\n.*?\n---\n', '', md, count=1, flags=re.S)                 # build metadata block
        md = re.sub(r'^!\[Cover[^\n]*\n', '', md, flags=re.M)
        md = re.sub(r'^\*This revision applies the editor.s title-page decisions[^\n]*\n', '', md, flags=re.M)
        md = md.replace('## Title page', '## Title page {.tp}', 1)
    h = pandoc(md)
    if f[:2] in ('21', '22'): h = split_corrections(h)
    if f.startswith('20_'):
        top = h.split('<h2', 1)
        intro_title = re.search(r'<h1[^>]*>(.*?)</h1>', top[0]).group(1)
        pages.append(('archive.html', re.sub(r'<[^>]+>', '', intro_title), top[0], 'Archive'))
        for m in re.finditer(r'(<h2 id="([^"]*)"[^>]*>(.*?)</h2>.*?)(?=<h2 |\Z)', '<h2' + top[1], re.S):
            t = re.sub(r'<[^>]+>', '', m.group(3)); pid = re.search(r'post (\d+)', t)
            pages.append((f'archive-{pid.group(1) if pid else slug(t)}.html', t, m.group(1), 'Archive post'))
        continue
    for t, i, part in split_h1(h):
        name = 'front.html' if f == '00_front-matter.md' and not pages else f'{slug(t)}.html'
        pages.append((name, t, part, 'Section'))

# present the sections in the five-group order of the volume (archive posts stay with the archive)
keyed, last = [], (9, 9)
for n, pg in enumerate(pages):
    k = last if pg[3] == 'Archive post' else (group_of(pg[1]) or last)
    if pg[0] == 'front.html': k = (-1, 0)
    keyed.append((k, n, pg)); last = k
pages = [pg for k, n, pg in sorted(keyed, key=lambda x: (x[0], x[1]))]

# where every anchor lives
where = {}
for name, t, h, g in pages:
    for i in re.findall(r'\sid="([^"]+)"', h):
        where.setdefault(i, name)

def relink(name, h):
    def fix(m):
        tgt = m.group(1)
        if tgt in where and where[tgt] != name:
            return f'href="{where[tgt]}#{tgt}"'
        return m.group(0)
    return re.sub(r'href="#([^"]+)"', fix, h)

CSS = (TS / 'site' / 'style.css').read_text()
(OUT / 'assets' / 'style.css').write_text(CSS)
shutil.copy(SRC / 'assets' / 'cover.png', OUT / 'assets' / 'cover.png')
shutil.copy(TS / 'site' / 'search.js', OUT / 'assets' / 'search.js')

def page(title, body, prev=None, nxt=None):
    pn = ''
    if prev or nxt:
        pn = '<nav class="pn">' + (f'<a href="{prev[0]}">← {E(prev[1])}</a>' if prev else '<span></span>') + (f'<a href="{nxt[0]}">{E(nxt[1])} →</a>' if nxt else '<span></span>') + '</nav>'
    pdf = f'<a href="../pdf/{E(PDFNAME)}">PDF edition</a>' if PDFNAME else ''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} · Aikipedia 2025</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css"></head><body>
<header class="site"><div class="wrap"><div class="brand"><a href="../../index.html">Aikipedia</a><span class="sep">·</span><a class="sub" href="../index.html">2025</a><span class="sep">·</span><a class="sub" href="index.html">Online edition</a></div>
<nav><a href="index.html">Contents</a><a href="search.html">Search</a>{pdf}</nav></div></header>
<main class="wrap">{BANNER}<article class="doc">{pn}{body}{pn}</article></main>
<footer class="site"><div class="wrap">Online edition of <em>Aikipedia 2025: Annual Collection</em>, Series Volume 1. Edited by W.H.L. Champaign Magazine, November 2026. Text CC BY 4.0; code MIT. Report errors or omissions as <a href="https://github.com/champaignmagazine/aikipedia/issues">issues on GitHub</a>.</div></footer>
</body></html>'''

for k, (name, t, h, g) in enumerate(pages):
    prev = pages[k - 1][:2] if k else None
    nxt = pages[k + 1][:2] if k + 1 < len(pages) else None
    body = relink(name, h)
    if t in ('Thematic Table of Contents', 'Alphabetical Table of Contents'):
        body = re.sub(r'<colgroup>.*?</colgroup>', '<colgroup><col style="width:40%"><col style="width:7%"><col style="width:53%"></colgroup>', body, count=1, flags=re.S)
        # a filter box over the list (editor, Nov 17, 14:28 CT: the thematic contents searchable or clickable)
        body = re.sub(r'(</h1>)', r'\1<div class="search"><input class="tocf" type="search" placeholder="Filter terms" aria-label="Filter terms"></div>', body, count=1) + """<script>
document.querySelector('.tocf').addEventListener('input',e=>{const q=e.target.value.toLowerCase().trim();
document.querySelectorAll('main li, main tbody tr').forEach(r=>{r.style.display=!q||r.textContent.toLowerCase().includes(q)?'':'none'});
document.querySelectorAll('main p > strong:only-child').forEach(h=>{let u=h.parentElement.nextElementSibling;if(u&&u.tagName==='UL'){const any=[...u.children].some(li=>li.style.display!=='none');h.parentElement.style.display=any?'':'none';u.style.display=any?'':'none'}})});
</script>"""
    (OUT / name).write_text(page(t, body, prev, nxt), encoding='utf-8')

# contents page
rows, cur = [], None
for name, t, h, g in pages:
    gk = group_of(t)
    if g != 'Archive post' and gk and ORDER[gk[0]][0] != cur:
        cur = ORDER[gk[0]][0]; rows.append(f'</ul><h3 class="tocg">{E(cur)}</h3><ul class="toc">')
    if g == 'Archive post':
        rows.append(f'<li class="sub"><a href="{name}">{E(t)}</a></li>')
    else:
        rows.append(f'<li><a href="{name}">{E(t)}</a></li>')
pdfl = f'<a class="btn" href="../pdf/{E(PDFNAME)}">PDF edition</a>' if PDFNAME else ''
home = f'''<div class="home"><div><p class="kicker">Aikipedia · Series Volume 1</p><h1>Aikipedia 2025: Annual Collection</h1>
<p class="lede">Edited by W.H.L. · Champaign Magazine · First published November 2026</p>
<p>The sixteen Aikipedia publications of 2025 as corrected reference texts and as a historical archive, with six entries commissioned for the collection. This online edition carries the full-post transcriptions of all sixteen original posts.</p>
<p><a class="btn" href="search.html">Search the collection</a>{pdfl}</p>
<h2>Contents</h2><ul class="toc">{''.join(rows)}</ul></div><img class="cover" src="assets/cover.png" alt="Cover of Aikipedia 2025: Annual Collection"></div>'''
(OUT / 'index.html').write_text(page('Contents', home), encoding='utf-8')

# search data: one item per record (h3 with an AIK id in the parts), one per archive post, one per other section
items = []
def text_of(h): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()
for name, t, h, g in pages:
    if t.startswith('Part '):
        for m in re.finditer(r'<a id="(aik-[^"]+)"></a>(?:</p>)?\s*<h3[^>]*>(.*?)</h3>(.*?)(?=<p><a id="aik-|<h2 |\Z)', h, re.S):
            items.append({'t': text_of(m.group(2)), 'u': f'{name}#{m.group(1)}', 'k': 'Entry', 'x': text_of(m.group(3))[:20000]})
    else:
        items.append({'t': t, 'u': name, 'k': g if g != 'Section' else 'Section', 'x': text_of(h)[:60000]})
(OUT / 'data' / 'search.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
(OUT / 'search.html').write_text(page('Search', '''<h1>Search</h1><div class="search"><input id="q" type="search" placeholder="Words or &quot;a phrase&quot;" autofocus>
<div class="filters"><label>Kind <select id="k"><option value="">All</option><option>Entry</option><option>Archive post</option><option>Section</option></select></label></div></div>
<p id="count" class="small"></p><ol id="res" class="results"></ol><script src="assets/search.js"></script>'''), encoding='utf-8')
print(len(pages), 'pages;', len(items), 'search items;', len(where), 'anchors')

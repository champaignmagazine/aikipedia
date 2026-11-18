"""Assemble the aikipedia repository: root and year landing pages, licences, changelog, both editions, build sources.
Usage: assemble_repo.py <draft dir> <pdf file> <repo out dir>"""
import pathlib, shutil, subprocess, sys, json, re
SRC, PDF, R = map(pathlib.Path, sys.argv[1:4])
TS = pathlib.Path(__file__).parent; H = pathlib.Path('/home/claude')
if R.exists(): shutil.rmtree(R)
(R / '2025' / 'pdf').mkdir(parents=True); (R / '2025' / 'build').mkdir(parents=True)
subprocess.run(['python3', str(TS / 'build_site.py'), str(SRC), str(R / '2025' / 'online'), PDF.name], check=True)
shutil.copy(PDF, R / '2025' / 'pdf' / PDF.name)
ed = re.search(r'edition: "([^"]+)"', (SRC / '00_front-matter.md').read_text(encoding='utf-8')).group(1)
proof = 'draft' in ed
B = R / '2025' / 'build'
shutil.copytree(SRC, B / 'collection-sources', ignore=shutil.ignore_patterns('editions'))
for f in ['build_pdf.py', 'build_site.py', 'common.py', 'assemble_repo.py']: shutil.copy(TS / f, B / f)
shutil.copytree(TS / 'site', B / 'site')
shutil.copy(H / 'scripts' / 'build_volume.py', B / 'build_volume.py')
shutil.copy(SRC / 'editions' / 'pdf.json', B / 'pdf-edition-manifest.json'); shutil.copy(SRC / 'editions' / 'online.json', B / 'online-edition-manifest.json')
STY = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;1,8..60,400&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">'
BAN = f'<div class="banner">Proof: {ed}. Not yet released.</div>' if proof else ''
def land(title, css, body, up=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>{STY}<link rel="stylesheet" href="{css}"></head><body>
<header class="site"><div class="wrap"><div class="brand"><a href="{up}index.html">Aikipedia</a></div><nav><a href="https://champaignmagazine.com">Champaign Magazine</a></nav></div></header>
<main class="wrap">{BAN}{body}</main><footer class="site"><div class="wrap">Edited by W.H.L. Text CC BY 4.0; code MIT. <a href="https://github.com/champaignmagazine/aikipedia">Source on GitHub</a> · <a href="https://github.com/champaignmagazine/aikipedia/issues">Report an error</a>.</div></footer></body></html>'''
YEAR = '''<p class="kicker">Aikipedia · Series Volume 1</p><h1>Aikipedia 2025: Annual Collection</h1>
<p class="lede">The sixteen Aikipedia publications of 2025 as corrected reference texts and as a historical archive, with six entries commissioned for the collection. Edited by W.H.L.; Champaign Magazine, November 2026.</p>
<div class="two"><div class="box"><h3><a href="online/index.html">Online edition</a></h3><p>The complete collection as web pages, with search, and full-post transcriptions of all sixteen original posts in the Historical Lexicon Archive.</p></div>
<div class="box"><h3><a href="pdf/%s">PDF edition</a></h3><p>The collection as a 7 × 10 in book, with selected transcriptions in the archive for four posts. The two editions differ only there.</p></div></div>''' % PDF.name
(R / '2025' / 'index.html').write_text(land('Aikipedia 2025: Annual Collection', 'online/assets/style.css', YEAR, '../'), encoding='utf-8')
ROOT = '''<p class="kicker">Champaign Magazine</p><h1>Aikipedia</h1>
<p class="lede">A knowledge repository devoted to emerging AI terms and concepts, written by leading AI models and edited by W.H.L., collected each year in an annual volume.</p>
<h2><a href="2025/index.html">2025 · Series Volume 1</a></h2>
<div class="two"><div class="box"><h3><a href="2025/online/index.html">Online edition</a></h3><p>All entries, the historical archive and search.</p></div>
<div class="box"><h3><a href="2025/pdf/%s">PDF edition</a></h3><p>The annual collection as a book.</p></div></div>''' % PDF.name
(R / 'index.html').write_text(land('Aikipedia · Annual Collections', '2025/online/assets/style.css', ROOT), encoding='utf-8')
(R / 'LICENSE').write_text('''MIT License

Copyright (c) 2026 Champaign Magazine

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''')
(R / 'LICENSE-CONTENT.md').write_text('''# License for text and data

To the extent they are protected by copyright, the text and data in this repository (the collection's text, the historical archive transcriptions, the register and records, the review and ruling records, and the indexes) are licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

Full legal code: <https://creativecommons.org/licenses/by/4.0/legalcode>

Attribute as: *Aikipedia 2025: Annual Collection*, edited by W.H.L., Champaign Magazine, 2026.

Material quoted from third-party sources remains subject to its own terms. Code (the build scripts, stylesheets and site scripts) is licensed separately under the MIT License; see `LICENSE`.
''')
(R / 'CHANGELOG.md').write_text(f'''# Changelog

## 2025 collection, Series Volume 1 · {"proof, " + ed if proof else "first release · November 2026"}

*Aikipedia 2025: Annual Collection* is published in two editions, built from the same sources:

- **PDF edition** (`2025/pdf/`), 7 × 10 in, with the editor's cover, continuous page numbers and page references in the tables of contents and the index of terms;
- **online edition** (`2025/online/`), with search and the full-post transcriptions of all sixteen original posts.

Both are built from the collection sources in `2025/build/collection-sources/` by the scripts in `2025/build/`. Corrections after release will be listed here, by version.
''')
(R / 'README.md').write_text(f'''# Aikipedia

The annual collections of *Aikipedia*, the feature in [Champaign Magazine](https://champaignmagazine.com) in which leading AI models write encyclopedia-style entries on emerging AI terms and concepts. The series is edited by W.H.L.

## Layout

```
index.html      landing page for the collections
2025/
  online/       the online edition: web pages, search, and the historical archive
  pdf/          the PDF edition
  build/        the collection sources and the scripts that built both editions
```

Later years get their own folders when their collections are prepared.

## Status

*Aikipedia 2025: Annual Collection* (Series Volume 1). {"This is a proof (" + ed + "); it is not the released edition." if proof else "Released November 2026."} See [CHANGELOG.md](CHANGELOG.md).

- [Online edition](https://champaignmagazine.github.io/aikipedia/2025/online/)
- [PDF edition](https://champaignmagazine.github.io/aikipedia/2025/pdf/{PDF.name})

## Report an error

Please [open an issue](https://github.com/champaignmagazine/aikipedia/issues) naming the record's Public Entry ID (for example `AIK-2025-F-P-MOD`), or the archive post and line range (for example post 13982, A-120 to A-125), and what is wrong.

## Licence

Text and data: CC BY 4.0 (see `LICENSE-CONTENT.md`). Code: MIT (see `LICENSE`).
''')
(R / '.nojekyll').write_text('')
print('repo assembled at', R)

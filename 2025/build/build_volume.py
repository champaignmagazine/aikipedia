#!/usr/bin/env python3
"""Assemble the Aikipedia 2025 collection draft (v0.2) from the live Master
Register (2026-11-14, after the 11:55 CT rulings), the AES v1.0 header revision,
the register §1-§2 extract, and the metadata-only versions of November 14, 2026.
Texts held under Claude's recusal, and Muse-held archive texts, are placeholders
for Muse's assembly handoff."""
import re, json, os, hashlib, datetime

H = '/home/claude'
U = '/mnt/user-data/uploads'
MR = f'{H}/in_mr'                 # Muse's metadata-round package (b22181eb…d3e8)
SUP = f'{H}/in_1203'              # Muse's 11:55 supplement (676a20ef…fbe9)
V = f'{MR}/versions'
AH = f'{H}/in_ah'                 # Muse's assembly handoff (1c74801b…5498)
REG = f'{H}/reg/aikipedia-master-register_COPY-2026-11-16-after-closing-checks.md'  # Muse's copy after the 14:32 CT rulings (a55b87b4…b1c5); §1–§3 identical to b88270ea
CT = f'{H}/in_ct'                 # Muse's cleared-tasks package (4e0ea828…96c7)
FPT = f'{H}/in_fpt'               # Muse's four full-post transcriptions (online edition only)
FPT_FILES = {  # key -> (file, file SHA-256 per Muse's rebuilt-transcriptions manifest, 2026-11-14, and S-MOE v0.3)
 'S-CAI': ('S-CAI_full-post-transcription_post13958_v0.3_header-rev-2026-11-16.md', '4a52a7fb5f008c33fe81a1cf763bca9186d631a0f4e0c6b9a5b168c01abeb837'),
 'S-MOE': ('S-MOE_full-post-transcription_post13998_v0.3_header-rev-2026-11-16.md', 'b40293c680bbf89ba1d242badd9a2fc269ba81675991498d82dcfd9cef87920b'),
 'L3': ('L3_full-post-transcription_post14221_v0.2_header-rev-2026-11-16.md', '381255671c7ea03ac87c3d8d0333be4dc30acae5ed87002fff6558dcff3f81cf'),
 'S-CSP': ('S-CSP_full-post-transcription_post14343_v0.2_header-rev-2026-11-16.md', 'ca5dbf3ca06cc648d8212fce7940037130e7a816a9d9e21e9d140b349bcec948'),
}
AES = f'{SUP}/aikipedia-editorial-format-standard-AES-v1.0-header-rev-2026-11-14.md'
S12 = f'{SUP}/register-sections-1-2_2026-11-14.md'
VER = 'v0.22'
OUT = f'{H}/draft/aikipedia-2025-collection-draft-{VER}'
# Date of Appearance rulings not yet in the build register copy (editor, November 17, 2026, 23:41 CT)
DOA_OVERRIDE = {'AIK-2025-S-P-LEXI': 'September 2, 2025 (Chitty-Venkata et al., arXiv:2509.02753v1)'}
os.makedirs(OUT, exist_ok=True)
reg = open(REG, encoding='utf-8').read()
REG_SHA = hashlib.sha256(open(REG, 'rb').read()).hexdigest()

# ---------- register §3 rows ----------
rows = []
for line in reg.splitlines():
    if line.startswith('| AIKC') or line.startswith('| — (container)'):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        rows.append(dict(aikc=c[0], pid=c[1], title=c[2], T=c[3], O=c[4], parent=c[5],
                         doa=c[6], orig=c[7], version=c[9], status=c[10]))
assert len(rows) == 107, len(rows)
recs = [r for r in rows if r['aikc'].startswith('AIKC')]
assert len(recs) == 101

PARENT = {'LEX2025LAUNCH': 'L1', 'LEX2025N2': 'L2', 'LEX2025N3': 'L3', 'LEX2025N4': 'L4',
          'LEX2025N5': 'L5', 'LEX2025N7': 'L7'}
PREFIX = {'L2': 'E', 'L3': 'S', 'L4': '', 'L5': '', 'L7': '', 'L1': ''}
def occ_code(r):
    m = re.match(r'AIK-2025-L-P-(\w+) \((\w+)\)', r['parent'])
    if not m: return None
    p = PARENT[m.group(1)]; seq = m.group(2)
    if p == 'L2': seq = 'E' + seq
    return f'{p}-{seq}'
for r in recs: r['occ'] = occ_code(r)

# provisional concepts (after the 2026-11-14 rulings)
PROV = {'AIKC-000019', 'AIKC-000020', 'AIKC-000030', 'AIKC-000047', 'AIKC-000049'}

# ---------- thematic parts (TOC proposal v0.2; Part VI title ruled November 14, 2026, 11:55 CT) ----------
PARTS = [
 ('I', 'Models and Architectures', [30, 22, 64, 75, 41, 59, 38, 8, 39, 12, 55, 85, 49, 69, 26]),
 ('II', 'Training, Learning and Data', [68, 56, 40, 65, 70, 57, 33, 72, 63, 28, 25, 53, 42, 1, 62, 78, 14]),
 ('III', 'Reasoning and Inference', [7, 21, 17, 27, 15, 23, 54, 16, 11]),
 ('IV', 'Alignment, Safety and Interpretability', [74, 87, 32, 58, 20, 31, 5, 88, 9, 19, 4, 73, 18, 60, 13, 46, 6]),
 ('V', 'Agents, Tools and Applications', [50, 52, 10, 2, 3, 43, 45, 24, 84, 48, 47, 29, 44, 66, 51, 83, 79]),
 ('VI', 'Embodied AI, Industry and Society', [80, 61, 76, 34, 67, 77, 82, 86, 81, 35, 71, 36, 37]),
]
allids = sorted(i for _, _, l in PARTS for i in l)
assert allids == list(range(1, 89)), 'parts must cover AIKC-000001..88 exactly once'

# ---------- source texts ----------
def rd(p): return open(p, encoding='utf-8').read()
def up(name):
    c = [f for f in os.listdir(U) if f.endswith(name)]
    assert c, name
    return f'{U}/{sorted(c)[-1]}'

import json as _json
_AH_MAN = _json.load(open(f'{AH}/manifest.json'))
HANDOFF = {}
for _it in _AH_MAN['sections']:
    _f = f'{AH}/' + _it['file']
    assert hashlib.sha256(open(_f, 'rb').read()).hexdigest() == _it['sha256'], _f
    HANDOFF[_it.get('pid') or _it.get('key')] = open(_f, encoding='utf-8').read().rstrip('\n')
_CT_MAN = _json.load(open(f'{CT}/manifest.json'))
for _it in _CT_MAN['members']:
    _f = f'{CT}/' + (_it.get('file') or _it.get('name'))
    assert hashlib.sha256(open(_f, 'rb').read()).hexdigest() == _it['sha256'], _f
for _k, (_f, _h) in FPT_FILES.items():
    assert hashlib.sha256(open(f'{FPT}/{_f}', 'rb').read()).hexdigest() == _h, _f
ASSEMBLED = ('*Assembled by Muse Spark 1.3 (assembly handoff of November 14, 2026, SHA-256 1c74801b…5498), '
             'from the filed text of record. Claude Opus 5.5 is recused from this text and did not place or check it.*')
RECUSED_NOTE = ('Text held by Muse Spark 1.3, who assembles it (v0.2 assembly handoff). Claude Opus 5.5 is recused '
                'from this text (Anthropic-authored original) and did not place or check it.')
STANDALONE = {  # pid -> (path or None, version label, note)
 'AIK-2025-F-N-RLVR': (f'{V}/aikipedia-2025-collection-entry-rlvr-DRAFT-v0.4.2.md', 'v0.4.2', None),
 'AIK-2025-F-N-CONTEXTENG': (f'{V}/aikipedia-2025-collection-entry-context-engineering-DRAFT-v0.2.2.md', 'v0.2.2', None),
 'AIK-2025-F-N-CONTEXTROT': (f'{H}/entries/aikipedia-2025-collection-entry-context-rot-v0.2.2.md', 'v0.2.2', None),
 'AIK-2025-F-N-EMERGENTMIS': (f'{V}/aikipedia-2025-emergent-misalignment-DRAFT-v0.2.2.md', 'v0.2.2', None),
 'AIK-2025-F-N-COTMONITOR': (f'{V}/aikipedia-2025-chain-of-thought-monitorability-DRAFT-v0.2.3.md', 'v0.2.3', None),
 'AIK-2025-F-N-SCHEMING': (f'{V}/aikipedia-2025-scheming-DRAFT-v0.2.2.md', 'v0.2.2', None),
 'AIK-2025-F-P-COTPROMPT': (f'{H}/cotpilot/COTPROMPT_corrected-canonical_v0.4.2.md', 'v0.4.2', None),
 'AIK-2025-F-P-MOE': (None, 'v0.5.2', RECUSED_NOTE),
 'AIK-2025-F-P-CONSTAI': (None, 'v0.5.2', RECUSED_NOTE),
 'AIK-2025-F-P-CALM': (f'{H}/calm/CALM_corrected-canonical_v0.2.2.md', 'v0.2.2', None),
 'AIK-2025-F-P-PDDISAGG': (f'{H}/pdd/PDD_corrected-canonical_v0.2.2.md', 'v0.2.2', None),
 'AIK-2025-F-P-GENUI': (f'{H}/genui/GENUI_corrected-canonical_v0.2.3.md', 'v0.2.3', None),
 'AIK-2025-F-P-ONPOLDISTIL': (f'{H}/opd/OPD_corrected-canonical_v0.3.2.md', 'v0.3.2', None),
 'AIK-2025-F-P-MOD': (f'{H}/mod/MOD_corrected-canonical_v0.3.2.md', 'v0.3.2', None),
 'AIK-2025-F-P-CIRCUITSP': (None, 'v0.2.2', RECUSED_NOTE),
}
LEX = {
 'L1': (f'{H}/l1/L1_canonical-records_v0.3.md', 'Records v0.3', None),
 'L2': (f'{H}/l2/L2_canonical-records_v0.2.3.md', 'Records v0.2.3', None),
 'L3': (None, 'Records v0.3.2', RECUSED_NOTE),
 'L4': (f'{V}/l4-canonical-records-v0.4.3.md', 'Records v0.4.3', None),
 'L5': (f'{H}/l5/L5_canonical-records_v0.1.1.md', 'Records v0.1.1', None),
 'L7': (f'{H}/l7/L7_canonical-records_v0.1.1.md', 'Records v0.1.1', None),
}

def shift(text, by):
    """Demote markdown headings so embedded texts nest under the volume's headings."""
    out = []
    infence = False
    for ln in text.splitlines():
        if ln.startswith('```'): infence = not infence
        m = re.match(r'^(#{1,6}) (.*)', ln)
        if m and not infence:
            n = min(6, len(m.group(1)) + by)
            ln = '#' * n + ' ' + m.group(2)
        out.append(ln)
    return '\n'.join(out)

lex_cache = {}
def lex_sections(p):
    if p in lex_cache: return lex_cache[p]
    t = rd(LEX[p][0]); lines = t.splitlines()
    occ, full = {}, {}
    cur = None; buf = []; kind = None
    def flush():
        if cur: (occ if kind == 'o' else full)[cur] = '\n'.join(buf).strip()
    for ln in lines:
        m1 = re.match(rf'^### ({p}-[A-Z]?\d+) — ', ln)
        m2 = re.match(rf'^## Corrected full entry — .*\(({p}-[A-Z]?\d+)\)\s*$', ln)
        if m1 or m2 or (ln.startswith('## ') and not m2):
            flush(); buf = []
            cur, kind = (m1.group(1), 'o') if m1 else ((m2.group(1), 'f') if m2 else (None, None))
        if cur: buf.append(ln)
    flush()
    lex_cache[p] = (occ, full)
    return occ, full

def anchor(pid): return pid.lower()

# ---------- assemble parts ----------
by_concept = {}
for r in recs: by_concept.setdefault(r['aikc'], []).append(r)
def ckey(r):
    first = RECORD_FIRST.get(r['aikc'])
    return (0 if r['pid'] == first else 1, 0 if r['parent'] == '—' else 1,
            r['orig'] if r['orig'] != '—' else '0', r['pid'])
# Concept headwords: the default is the first record's title. Overrides use a registered record title.
#  AIKC-000010: Muse review v0.1 F3 (the grouping decision of Nov 10, 2026 merges L1-S6 into COMPOUNDAI).
#  AIKC-000051, AIKC-000052: presentation proposals in v0.2 (plainest registered title), for the editor's review.
HEADWORD = {'AIKC-000010': 'Compound AI Systems', 'AIKC-000051': 'Retrieval-Augmented Generation (RAG)',
            'AIKC-000052': 'Agentic AI'}
RECORD_FIRST = {'AIKC-000010': 'AIK-2025-E-P-COMPOUNDAI'}
NEW_MARK = '**New for the 2025 Collection** (origin `N`: commissioned for this collection; not published in 2025)'

def title_of(a): return HEADWORD.get(a) or sorted(by_concept[a], key=ckey)[0]['title']
def is_new(a): return any(r['O'] == 'N' for r in by_concept[a])
placeholders = []
def ph(kind, text):
    placeholders.append((kind, text))
    return f'> **[PLACEHOLDER — {kind}]** {text}'

parts_md = []
concept_part = {}
for num, name, ids in PARTS:
    aikcs = [f'AIKC-{i:06d}' for i in ids]
    aikcs.sort(key=lambda a: title_of(a).lower())
    md = [f'# Part {num}. {name}', '']
    for a in aikcs:
        rs = sorted(by_concept[a], key=ckey)
        head = title_of(a)
        concept_part[a] = num
        flag = ' †' if a in PROV else ''
        md += [f'## {head}{flag}', '',
               f'*Internal Concept ID {a}' + (' · provisional concept identity' if flag else '') +
               f' · {len(rs)} record' + ('s' if len(rs) > 1 else '') + ' in 2025*', '']
        if any(r['O'] == 'N' for r in rs): md += [NEW_MARK, '']
        if a == 'AIKC-000010':
            md += ['*Concept note: by the editor\'s grouping decision of November 10, 2026, the Launch Edition occurrence '
                   '"Composable Models & Model Chaining" (L1-S6) is merged into this concept; it keeps its own Public Entry ID '
                   '(AES-ID v1.0 §1, rule 6).*', '']
        for r in rs:
            md += [f'<a id="{anchor(r["pid"])}"></a>', '', f'### {r["title"]} — `{r["pid"]}`', '',
                   f'| Type / Origin | Parent | Date of Appearance | Original publication |',
                   '|---|---|---|---|',
                   f'| {r["T"]} / {r["O"]} | {r["occ"] or "standalone"} | {DOA_OVERRIDE.get(r["pid"], r["doa"])} | {r["orig"]} |', '']
            if r['parent'] == '—':
                path, ver, note = STANDALONE[r['pid']]
                if path is None and r['pid'] in HANDOFF: md += [ASSEMBLED, '', HANDOFF[r['pid']], '']
                elif note: md += [ph('text held by Muse' if path is None else 'version', f'`{r["pid"]}` {ver}: {note}'), '']
                if path: md += [shift(rd(path), 3), '']
            else:
                p = r['occ'].split('-')[0]
                path, ver, note = LEX[p]
                if path is None:
                    # Note: L3 records use occurrence headings L3-S1..L3-S12, while occ_code gives L3-1..L3-12;
                    # the handoff maps them explicitly (Muse's cover note, §2). Map before any raw L3 rebuild.
                    if r['pid'] in HANDOFF: md += [ASSEMBLED, '', HANDOFF[r['pid']], '']
                    else: md += [ph('text held by Muse', f'`{r["pid"]}` ({r["occ"]}, {ver}): {note}'), '']
                    continue
                if note: md += [ph('version', f'{r["occ"]}: {note}'), '']
                occ, full = lex_sections(p)
                assert r['occ'] in occ, r['occ']
                md += [shift(occ[r['occ']], 1), '']
                if r['occ'] in full:
                    md += [shift(full[r['occ']], 2), '']
        md.append('')
    parts_md.append((num, name, '\n'.join(md)))

# ---------- tables of contents ----------
alpha = sorted(by_concept, key=lambda a: title_of(a).lower())
toc_alpha = ['# Alphabetical Table of Contents', '',
             '*Concepts A–Z. † marks a provisional concept identity; ◆ marks a concept new for the 2025 Collection (origin N). Part numbers refer to the thematic parts.*', '',
             '| Concept | Part | Records |', '|---|---|---|']
for a in alpha:
    rs = sorted(by_concept[a], key=ckey)
    toc_alpha.append(f'| {title_of(a)}{" †" if a in PROV else ""}{" ◆" if is_new(a) else ""} | {concept_part[a]} | ' +
                     ', '.join(f'[`{r["pid"]}`](#{anchor(r["pid"])})' for r in rs) + ' |')
toc_theme = ['# Thematic Table of Contents', '']
for num, name, ids in PARTS:
    toc_theme += [f'**Part {num}. {name}**', '']
    for a in sorted([f'AIKC-{i:06d}' for i in ids], key=lambda a: title_of(a).lower()):
        r0 = sorted(by_concept[a], key=ckey)[0]
        toc_theme.append(f'- [{title_of(a)}{" †" if a in PROV else ""}{" ◆" if is_new(a) else ""}](#{anchor(r0["pid"])}){{.thm}}')
    toc_theme.append('')

# ---------- index of terms ----------
# One line per concept (headword, all its records, † and ◆ marks); variant record titles and synonyms
# point to the headword with "see"; related but non-synonymous terms use "compare" or a stated relation
# (GPT-6 review of draft v0.1, index audit; Muse reconciliation memo v0.1, adjudicated rows).
def links(a): return ', '.join(f'[`{r["pid"]}`](#{anchor(r["pid"])})' for r in sorted(by_concept[a], key=ckey))
def hw(a): return f'{title_of(a)}{" †" if a in PROV else ""}'
NOT_ABBREV = {'AI', 'LLM'}
SEE = {  # alias -> concept (synonyms, abbreviations, variant names)
 'CoV (historical abbreviation; corrected to CoVe)': 'AIKC-000021',
 'MoLAE': 'AIKC-000039', 'MoLE': 'AIKC-000039', 'Game-Theoretic Statistics': 'AIKC-000070',
 'Student-Teacher Cascades': 'AIKC-000056',
 'Dexterous Manipulation': 'AIKC-000036', 'GKD': 'AIKC-000025',
 'Reinforcement Learning with Verifiable Rewards': 'AIKC-000001',
 'CoT prompting': 'AIKC-000007', 'CoT monitorability': 'AIKC-000005',
}
RELATED = {  # term -> (concept, relation wording)
 'Deceptive Alignment': ('AIKC-000032', 'broader concept, discussed under'),
 # GPT-6 v0.2 review, headword qualification: named with Agentic AI in the Launch Edition headword, not synonyms
 'Super-Agents': ('AIKC-000052', 'named in the Launch Edition headword with Agentic AI (not a synonym); discussed under'),
 'Model Orchestration': ('AIKC-000052', 'named in the Launch Edition headword with Agentic AI (not a synonym); discussed under'),
 'Confident Adaptive Language Modeling (Schuster et al., 2022)': ('AIKC-000022', 'a different method with the same acronym (Editorial Addition E01); compare'),
}
lines = {}
SEEALSO = _json.load(open(f'{CT}/see-also-concepts_muse-v0.1.json'))
def first_anchor(a): return anchor(sorted(by_concept[a], key=ckey)[0]['pid'])
for a in by_concept:
    sa = [t for t in SEEALSO.get(a, []) if t in by_concept and t != a]
    sa_txt = (' · *See also:* ' + '; '.join(f'[{hw(t)}](#{first_anchor(t)})' for t in sorted(sa, key=lambda t: title_of(t).lower()))) if sa else ''
    lines[hw(a).lower()] = f'- **{hw(a)}**{" ◆" if is_new(a) else ""} — {links(a)}{sa_txt}'
def add_ref(term, text):
    k = term.lower()
    if k in lines: return
    lines[k] = text
for a, rs in by_concept.items():
    for r in rs:
        if r['title'] != title_of(a):
            add_ref(r['title'], f'- {r["title"]} → *see* **{hw(a)}**')
        for ab in re.findall(r'\(([A-Z][A-Za-z]*[A-Z][A-Za-z]?)\)', r['title']):
            if len(ab) < 3 or ab in NOT_ABBREV: continue   # GPT-6 v0.2 review, F5: "(AI)" in "Scheming (AI)" is a qualifier
            add_ref(ab, f'- {ab} → *see* **{hw(a)}**')
        m = re.match(r'^([A-Za-z]+) — (.+)$', r['title'])
        if m and m.group(1) != m.group(1).lower(): add_ref(m.group(2), f'- {m.group(2)} → *see* **{hw(a)}**')
for al, a in SEE.items(): add_ref(al, f'- {al} → *see* **{hw(a)}**')
for t, (a, rel) in RELATED.items(): add_ref(t, f'- {t} — {rel} **{hw(a)}**')
index_md = ['# Alphabetical Index of Terms', '',
            '*One line per concept, with every record of it in the collection. "See" points from a variant name, abbreviation or '
            'merged occurrence to the concept\'s headword; "compare" and other stated relations mark terms that are related but '
            'not synonyms. † marks a provisional concept identity; ◆ a concept new for the 2025 Collection. In the PDF edition the numbers '
            'after each concept are page references; online, each record ID links to its entry.*', '',
            '*"See also" after a concept lists the concepts its entries name in their own See Also sections, as written (one direction only; harvested by Muse Spark 1.3). Aliases checked by Muse Spark 1.3, November 14, 2026: pass.*', '',
            ph('index page numbers', 'Print page numbers are added at typesetting.'), '']
index_md += [lines[k] for k in sorted(lines)]

# ---------- back matter from the register ----------
def detail_blocks():
    m = re.search(r'### Record details\n(.*?)\n## 4\. Assignment log', reg, re.S)
    body = m.group(1)
    blocks = re.split(r'\n(?=\*\*AIK-2025-)', '\n' + body)
    return [b.strip() for b in blocks if b.strip().startswith('**AIK-2025-')]
blocks = detail_blocks()
corr_md = ['# Corrections and Editorial Notes', '',
           '*Correction IDs and descriptions by record, as recorded in the Master Register (November 16, 2026, after the 14:32 CT rulings). Full evidence is in each record\'s correction register.*', '']
conf_md = []
for b in blocks:
    head = b.splitlines()[0]
    cl = [ln for ln in b.splitlines() if re.match(r'- (Item-level correction IDs|Correction IDs|Blind-audit annotations)', ln)]
    if cl:
        corr_md += [f'## {head.strip("*").split("**")[0]}', ''] + cl + ['']
    cf = [ln for ln in b.splitlines() if ln.startswith('- Conflicts')]
    if cf:
        conf_md += [f'**{head.strip("*").split("**")[0]}**', ''] + cf + ['']
corr_md[4:4] = ['## How to read corrected records', '',
 'In a corrected entry or record, a bracketed marker after a passage names the change behind it: `[Cnn]` a correction (listed below and in the record\'s correction register), `[E01]` an editorial addition adopted by the editor, and `[ST01]` a structural rearrangement into the AES section order. Unmarked text is the original\'s own wording. In the lexicon records, the published short text is reproduced unchanged and a **corrected record** line gives the canonical wording where a correction applies. The historical wording of every original is in the Historical Lexicon Archive.', '']
corr_md += ['', 'New additions (origin N) carry review histories, not correction IDs; their revision notes are in each entry\'s own provenance section.']

prov_md = ['# References and Provenance Register', '',
           rd(f'{CT}/bibliography-10a_muse-v0.1.md'), '',
           '*Link check, November 16, 2026 (Claude Fable 5.2). Of the 184 works, 128 carry a link or identifier that Claude could check; all 75 arXiv records and 60 other links were opened and agree with their citations, apart from three citations to amend and four moved links, listed in the check report. Not verified: 9 links that could not be opened, 29 works cited without a link, and 27 works cited only by the four texts from which Claude is recused.*', '',
           '## 10b. Provenance register', '',
           f'*The Master Register\'s §3 and record details, as of November 16, 2026, from Muse Spark 1.3\'s copy of that date (SHA-256 {REG_SHA[:8]}…{REG_SHA[-4:]}). At publication this is regenerated from the register as it then stands.*', '']
s3 = re.search(r'## 3\. Register — Aikipedia 2025\n(.*?)\n## 4\. Assignment log', reg, re.S).group(1)
prov_md.append(shift(s3, 1))

# ---------- archive ----------
ARCH = [  # (date, label, key, path or None, note)
 ('2025-10-29', 'On-Policy Distillation (post 13892)', 'S-OPD', f'{H}/opd/OPD_archive-text_post13892.md', None),
 ('2025-10-30', 'Chain-of-Thought Prompting (post 13946)', 'S-COT', f'{H}/cotpilot/COTPROMPT_archive-text_post13946_corrected-2026-11-14.md', None),
 ('2025-10-31', 'Constitutional AI (post 13958)', 'S-CAI', None, RECUSED_NOTE),
 ('2025-11-03', 'Mixture of Depths (post 13982)', 'S-MOD', f'{H}/mod/MOD_archive-text_post13982_header-rev-2026-11-15.md', None),
 ('2025-11-05', 'Mixture of Experts (post 13998)', 'S-MOE', None, RECUSED_NOTE),
 ('2025-11-06', 'Continuous Autoregressive Language Models (post 14021)', 'S-CALM', f'{H}/calm/CALM_archive-text_post14021_header-rev-2026-11-14.md', None),
 ('2025-11-09', 'Prefill–Decode Disaggregation (post 14033)', 'S-PDD', f'{H}/pdd/PDD_archive-text_post14033.md', None),
 ('2025-11-29', 'Generative User Interfaces (post 14146)', 'S-GENUI', f'{H}/genui/GENUI_archive-text_post14146_header-rev-2026-11-15.md', None),
 ('2025-11-30', 'New AI Lexicon 2025 — Launch Edition (post 14155)', 'L1', f'{H}/l1/L1_archive-text_post14155_header-rev-2026-11-15.md',
  'NOTE:One occurrence, L1-S3 "Instruction Tuning 2.0", is reproduced here as published but is excluded from the canonical text (disposition X: wholly unsourced narrative). It carries no correction ID, Public Entry ID or Internal Concept ID.'),
 ('2025-12-01', 'New AI Lexicon 2025 (2) (post 14191)', 'L2', f'{H}/l2/L2_archive-text_post14191_corrected-2026-11-14_header-rev-2026-11-15.md', None),
 ('2025-12-02', 'New AI Lexicon 2025 (3) (post 14221)', 'L3', None, RECUSED_NOTE),
 ('2025-12-03', 'New AI Lexicon 2025 (4) (post 14233)', 'L4', f'{H}/l4/l4-archive-text-v0.5.md', None),
 ('2025-12-05', 'New AI Lexicon 2025 (5) (post 14257)', 'L5', f'{H}/l5/L5_archive-text_post14257_header-rev-2026-11-15.md', None),
 ('2025-12-08', 'New AI Lexicon 2025 (6) (post 14313) — excluded from the canonical text (disposition X)', 'L6', f'{H}/l6/L6_archive-text_post14313_header-rev-2026-11-15.md',
  'NOTE:This installment is excluded from the canonical text under disposition X (the editor\'s decision of November 10, 2026) and its twelve headwords carry no identifiers. It is preserved here in full (AES v1.0 §1, Amendment A). Transcription by Claude Opus 5.5 through the WordPress connector; checked line by line against the live post by Muse Spark 1.3, November 14, 2026 (all 466 lines; accepted with no discrepancies).'),
 ('2025-12-12', 'New AI Lexicon 2025 (7) (post 14328)', 'L7', f'{H}/l7/L7_archive-text_post14328_header-rev-2026-11-15.md', None),
 ('2025-12-14', 'Circuit Sparsity (post 14343)', 'S-CSP', None, RECUSED_NOTE),
]
ARCH_COMMON = ('The canonical, corrected text is in the thematic parts (AES v1.0 §1, Amendment A). Line labels (A-nnn) are the archive\'s apparatus; '
               'the originals are set apart typographically from the canonical text.')
ARCH_CHECK = ('*Checking against the live posts.* The transcriptions received fidelity checks against their live posts. Each section records the scope and outcome. '
              'Some line splits and formula renderings in Lexicon (3) and Circuit Sparsity remain not verified. Every check was a fidelity check only, not a substantive review. The checks were made under the checking briefs of November 14, 2026. '
              'On-Policy Distillation, Prefill–Decode Disaggregation and Lexicons (1) and (7) were checked by GLM 5.3 Flash. '
              'Mixture of Depths and Generative User Interfaces were checked by Grok 4.5, and GLM cross-sampled Generative User Interfaces. '
              'Continuous Autoregressive Language Models and Lexicon (5) were checked by Qwen3-Max. Lexicon (6) was checked by Muse Spark 1.3. '
              'Chain-of-Thought Prompting was checked by GLM and, for its final part, by Qwen3-Max. Lexicons (2) and (4) were checked by GLM, '
              'and each was corrected after its check (heading levels in Lexicon (2); one word in Lexicon (4)). '
              'Chain-of-Thought Prompting was also corrected after its check: a stray space at each of its 24 links was removed. '
              'The four sections held by Muse Spark 1.3 record their own status. Each section\'s header gives its file history.')
arch_intro = {
 'pdf': ['# Historical Lexicon Archive', '',
         '*The Historical Lexicon Archive preserves the sixteen original Aikipedia publications of 2025, in date order, as line-numbered plain-text '
         'transcriptions of the published posts. They preserve the textual record; they are not copies of the original web pages, and each section\'s '
         'header states how markup, lists, links and special characters were normalized. Twelve sections reproduce the full posts; four — '
         'Constitutional AI, Mixture of Experts, Lexicon (3) and Circuit Sparsity — present the published entry texts of record. The complete, '
         'line-numbered transcriptions of those four publications, including drafts, embedded reviews and dialogue, are in the online edition. '
         'The abbreviated PDF treatment does not supersede those historical sources. ' + ARCH_COMMON + '*', '', ARCH_CHECK, ''],
 'online': ['# Historical Lexicon Archive', '',
         '*The Historical Lexicon Archive preserves the sixteen original Aikipedia publications of 2025, in date order, each as a full-post, '
         'line-numbered plain-text transcription of the published post, including its drafts, embedded reviews and dialogue. The transcriptions '
         'preserve the textual record; they are not copies of the original web pages, and each section\'s header states how markup, lists, links and '
         'special characters were normalized. The full-post transcriptions of Constitutional AI, Mixture of Experts, Lexicon (3) and Circuit Sparsity '
         'were prepared by Muse Spark 1.3 for this edition (13:10 CT rulings); the PDF edition gives those four as their entry texts of record. '
         + ARCH_COMMON + '*', '', ARCH_CHECK, ''],
}
FPT_STATUS = {
 'S-MOE': 'Checked against the live post by GLM 5.3 Flash, November 15, 2026: accepted, no discrepancies. GLM checked lines A-001 to A-213 against the stored content and A-214 to A-268 against the rendered page, a basis the editor accepted on November 15, 2026.',
 'S-CAI': 'Checked against the live post by Qwen3-Max, November 15, 2026: accepted, no discrepancies in wording or structure. Three spacing items await byte-level confirmation by the holder.',
 'L3': 'Checked against the live post by Qwen3-Max, November 15, 2026: wording accepted throughout. Two points are open: whether about twenty-one line splits correspond to line breaks in the stored content, and the three formula-image renderings, which have not been verified against their alt texts. These points are not verified.',
 'S-CSP': 'Checked against the live post by Qwen3-Max, November 15, 2026: wording accepted throughout, including the Attachment dialogue. Three points are open: the line-split question (as for Lexicon (3)), four inconsistent formula renderings awaiting the holder\'s ruling, and the 23-alt formula inventory, which has not been verified against the stored alt texts. These points are not verified.',
}
FPT_NOTE = ('*Full-post transcription prepared by Muse Spark 1.3 for the online edition (the editor\'s rulings of November 14, 2026, 13:10 and 23:25 CT), '
            'file SHA-256 {h}. Claude Opus 5.5 is recused from this text and did not transcribe, place or check it. {st}*')
arch_ed = {}
for ed in ('pdf', 'online'):
    md = list(arch_intro[ed])
    for d, lab, key, p, note in ARCH:
        md += [f'## {d} — {lab}', '']
        if note and note.startswith('NOTE:'): md += [f'*Archive note: {note[5:]}*', '']
        if p: md += [shift(rd(p), 2), '']
        elif ed == 'online' and key in FPT_FILES:
            f, h = FPT_FILES[key]
            md += [FPT_NOTE.format(h=h[:8] + '…' + h[-4:], st=FPT_STATUS[key]), '', shift(rd(f'{FPT}/{f}'), 2), '']
        elif key in HANDOFF: md += [ASSEMBLED, '', HANDOFF[key], '']
        else: md += [ph('archive text held by Muse' if 'recused' in (note or '') else 'archive text', f'{key}: {note}'), '']
    arch_ed[ed] = md

# ---------- front matter ----------
n_new = sum(1 for r in recs if r['O'] == 'N')
cont = sorted([r for r in rows if r['aikc'].startswith('—')], key=lambda r: r['orig'])
n_est = len(by_concept) - len(PROV)
type_n = {t: sum(1 for r in recs if r['T'] == t) for t in 'FES'}
LEXKEY = {'L1': 'LEX2025LAUNCH', 'L2': 'LEX2025N2', 'L3': 'LEX2025N3', 'L4': 'LEX2025N4', 'L5': 'LEX2025N5', 'L7': 'LEX2025N7'}
STANDKEY = {'S-OPD': 'ONPOLDISTIL', 'S-COT': 'COTPROMPT', 'S-CAI': 'CONSTAI', 'S-MOD': 'MOD', 'S-MOE': 'MOE', 'S-CALM': 'CALM',
            'S-PDD': 'PDDISAGG', 'S-GENUI': 'GENUI', 'S-CSP': 'CIRCUITSP'}
tl = ['| Date (2025) | Post | Publication | In the canonical text |', '|---|---|---|---|']
for d, lab, key, p, note in ARCH:
    title, post = re.match(r'(.*) \((post \d+)\)', lab.split(' — excluded')[0]).groups()
    if key in LEXKEY:
        n = sum(1 for r in recs if f'AIK-2025-L-P-{LEXKEY[key]} (' in r['parent'])
        inc = f'{n} occurrence records' + (' (L1-S3 excluded)' if key == 'L1' else '')
    elif key == 'L6': inc = 'Excluded (disposition X); archive only'
    else:
        pid = f'AIK-2025-F-P-{STANDKEY[key]}'
        inc = f'[`{pid}`](#{anchor(pid)})'
    tl.append(f'| {datetime.date.fromisoformat(d).strftime("%B %-d")} | {post.split()[1]} | *{title}* | {inc} |')
cont_tbl = ['| Installment | Public Entry ID | Disposition and status (Master Register) |', '|---|---|---|']
for c in cont:
    m = re.search(rf'\*\*{re.escape(c["pid"])}\*\*.*?\n- Status: ([^\n]+)', reg, re.S)
    cont_tbl.append(f'| *{c["title"]}* | `{c["pid"]}` | {m.group(1) if m else "—"} |')
TITLE_PAGES = '![Cover: Aikipedia 2025, Series Volume 1, Annual Collection; W.H.L., editor; Champaign Magazine](assets/cover.png)\n\n---\n\n' + rd(f'{H}/intro/title-copyright-pages_v0.5_2026-11-16.md').split('\n', 1)[1].strip()
_M = rd(f'{H}/intro/editorial-method_v1.1_2026-11-17.md')
# Editor's ruling of November 17, 2026, 20:30 CT: the Method's version note goes to the version history (Appendix D);
# its source sentence stays in the reader text, at the end of the opening paragraph.
_vn = re.match(r'\*Version 1\.1, November 17, 2026, by Claude Opus 5\.5,.*?\*\n\n', _M, re.S)
assert _vn
_M = _M[_vn.end():]
_p1_end = _M.index('\n\n')
_M = _M[:_p1_end] + ' Facts in these sections come from the Master Register (Appendix B), the editorial standard (Appendix A) and the editor\'s recorded rulings (Appendix D).' + _M[_p1_end:]
METHOD_A, _r = _M.split('---SECTION-5.3---')
METHOD_B, METHOD_C = _r.split('---SECTION-5.6---')
METHOD_A, METHOD_B, METHOD_C = METHOD_A.strip(), METHOD_B.strip(), METHOD_C.strip()
CONTRIB = rd(f'{H}/intro/contributor-table-5.5_muse-v0.5_2026-11-17.md').strip()
front = f'''---
title: "Aikipedia 2025: Annual Collection"
edition: "Collection v1.0 — draft {VER} (not for publication)"
editor: "W.H.L."
standard: "AES v1.0 / AES-ID v1.0 (frozen November 14, 2026)"
draft_assembled: "{datetime.date(2026,11,14).isoformat()}, Claude Opus 5.5"
---

# Aikipedia 2025: Annual Collection

**Edited by W.H.L.** · Champaign Magazine

{TITLE_PAGES}



---

{rd(f'{H}/intro/contributors-page_v0.3_2026-11-17.md').strip()}

---

# Series Preface

{rd(f'{H}/intro/series-preface_WHL_v1.3_2026-11-17.md').strip()}

---

# Volume Preface

*By Claude Opus 5.5 (Anthropic), GPT-6 Astra (OpenAI) and Muse Spark 1.3 (Meta)*

{rd(f'{H}/intro/volume-preface_v1.1_2026-11-17.md').strip()}

---

# How to Use This Collection

**Historical and canonical texts.** The collection distinguishes the original publications, preserved in the Historical Lexicon Archive, from their corrected canonical reference texts in Parts I–VI: the versions corrected, reviewed and approved for reference use. Most original entries are represented in both forms. Texts excluded from the canonical reference collection remain preserved and identified in the historical archive. The archive gives each original as a line-numbered plain-text transcription of the published post (A-001, A-002, …), not as a copy of the original web page; each section's header states how markup was normalized and how the text has been checked. The online edition gives every post in full; the PDF edition gives four of them (Constitutional AI, Mixture of Experts, Lexicon (3) and Circuit Sparsity) as their entry texts of record. Corrections never alter the archive.

**Finding a term.** Use the Alphabetical Table of Contents (concepts A–Z, with their part), the Thematic Table of Contents (by part), or the Index of Terms, which also lists variant names, abbreviations and related terms. Online, every record has its own anchor and the edition is searchable.

**Concepts and records.** A *concept* may occur in several 2025 texts — for example a full-length entry and a lexicon installment. The collection gives each concept one heading, with an Internal Concept ID (`AIKC-######`), and under it each *record* (one occurrence in one text) with its own Public Entry ID (`AIK-2025-T-O-KEY[-NN]`; T is the type — F full-length, E expanded, S short, L installment — and O the origin, P published in 2025 or N new).

**Marks.**
- **†** — a provisional concept identity: the concept's distinctness or attestation is not verified. A provisional record whose headword is unattested is presented as historical text under its provenance note, not as an endorsed definition (AES v1.0 §10).
- **◆ New for the 2025 Collection** — a full-length entry commissioned for this collection (origin `N`); it was not published in 2025.
- **[Cnn]**, **[E01]**, **[ST01]** — in a corrected text: a correction, an editorial addition adopted by the editor, and a structural rearrangement into the AES section order. Unmarked text is the original's wording. In lexicon records, a **corrected record** line gives the canonical wording wherever a correction applies.
- **Excluded (disposition X)** — a 2025 text kept in the archive but not carried into the canonical text: the whole of *New AI Lexicon 2025 (6)*, and the Launch Edition's "Instruction Tuning 2.0".

**Dates.** Each record gives a *Date of Appearance* — the earliest verified public appearance documented by the available evidence, never inferred from publicity, and not a claim of absolute priority; "Not established" where no date is supported — separately from the date the 2025 text was published (AES v1.0 §3). Times of day in this volume are Central Time (America/Chicago) unless stated otherwise.

**Checking the record.** Corrections and editorial notes are listed by record; the References and Provenance Register gives each record's register entry; Appendices A–E give the standard, the identifier rules, the provenance policy, the digest of editorial rulings, and the conflicts and recusals.

---

# Collection at a Glance

| | |
|---|---|
| Original 2025 publications | 16 posts: 9 standalone entries and 7 lexicon installments |
| In the canonical text | 15 posts (Lexicon (6) excluded, disposition X) |
| Concepts | {len(by_concept)} — {n_est} established, {len(PROV)} provisional (†) |
| Records | {len(recs)} concept-bearing records — {type_n['F']} full-length, {type_n['E']} expanded, {type_n['S']} short — plus {len(cont)} lexicon containers ({len(rows)} register rows) |
| New for the 2025 Collection | {n_new} full-length entries (origin `N`) |
| Thematic parts | 6 |
| Standard | AES v1.0 and AES-ID v1.0, frozen November 14, 2026 |

---

# The 2025 Publications: A Timeline

*Every original Aikipedia publication of 2025 on champaignmagazine.com, in date order. Each is reproduced as published in the Historical Lexicon Archive under its date.*

{chr(10).join(tl)}

*Related editorial material, outside the count: the December 7, 2025 article "AI deception and its Cluster: Sycophancy, Sandbagging, and Oversight Evasion" (post 14267), in Appendix F.*

---

# Annual Introduction

{rd(f'{H}/intro/annual-introduction_v1.4_approved_2026-11-18.md')}

---

# Editorial Method

{METHOD_A}

## 5.1 Sources

The collection represents every original Aikipedia publication of 2025: sixteen posts on champaignmagazine.com, nine standalone entries and seven lexicon installments. Fifteen are in scope for the canonical text. *New AI Lexicon 2025 (6)* is excluded from the canonical text under disposition X and is preserved in the Historical Lexicon Archive. In *New AI Lexicon 2025 — Launch Edition*, one occurrence (Instruction Tuning 2.0) is likewise excluded.

## 5.2 New additions

{n_new} full-length entries were commissioned for the collection (origin `N`): RLVR, Context Engineering, Context Rot, Emergent Misalignment, Chain-of-Thought Monitorability and Scheming. They are integrated into the thematic parts and marked "New for the 2025 Collection".

## 5.3 Audit, correction and review

{METHOD_B}

The six lexicon installments in the canonical text, with their dispositions as recorded in the Master Register:

{chr(10).join(cont_tbl)}

## 5.4 Identifiers and statuses

Every record carries a Public Entry ID (`AIK-2025-T-O-KEY[-NN]`) and every concept an Internal Concept ID (`AIKC-######`), assigned in the Aikipedia Master Register (Appendix B). The register holds {len(rows)} rows: {len(recs)} concept-bearing records covering {len(by_concept)} concepts, plus {len(cont)} lexicon containers. Of the {len(by_concept)} concepts, {n_est} are established and {len(PROV)} are provisional (marked †). A provisional record whose headword is unattested is presented as historical text under its provenance note, not as an endorsed definition (AES v1.0 §10).

---

# AI Disclosure

{CONTRIB}

{METHOD_C}
'''

# ---------- appendices ----------
aes = rd(AES); s12 = rd(S12); ap = rd(f'{H}/intro/AP-2025-01-v1.0.md')
sha = lambda f: hashlib.sha256(open(f, 'rb').read()).hexdigest()
DIGEST = [
 ('2026-11-04', 'AES v0.9 and AES-ID v0.9 adopted (pilot); eligibility rule (first appearance in the collection year or earlier)', 'Editor'),
 ('2026-11-04 to 11-09', 'Six new additions approved: RLVR, Context Engineering, Context Rot, Emergent Misalignment, Chain-of-Thought Monitorability, Scheming', 'Editor'),
 ('2026-11-09', 'AES-ID structural rulings X11, X1, X13, X12, X9/X15; keys CONSTAI and CIRCUITSP confirmed', 'Editor'),
 ('2026-11-10', 'X14: the December 7, 2025 article "AI deception and its Cluster" (post 14267) is related editorial material, outside the canonical count', 'Editor'),
 ('2026-11-10', 'Audit dispositions decided; Lexicon (6) excluded (X); Chain-of-Thought Prompting registered as the first corrected original; concept grouping (Composable Models into Compound AI)', 'Editor'),
 ('2026-11-10 to 11-13', 'Corrected originals and installments approved and registered: S-MOE, S-CAI, L3, CALM, PDD, GENUI, OPD, L2, MOD, L1, L5, L7, L4, S-CSP', 'Editor; registered by Muse Spark 1.3'),
 ('2026-11-11', 'Permanence rule 10 (provisional concept IDs) entered', 'Editor'),
 ('2026-11-12', 'Dates of Appearance ruled as documented milestones, not exhaustive first uses', 'Editor'),
 ('2026-11-13', 'Standing-approval ruling withdrawn: every package needs explicit editorial approval; eleven AES v1.0 points adopted', 'Editor'),
 ('2026-11-13', 'X6 attestation rulings: Vibe Coding established; three L3 terms established; ARITHHEADS, LHPLANMETRIC, MOETHEORY provisional', 'Editor'),
 ('2026-11-13', 'Correction C11 (L1-M11) approved and registered', 'Editor'),
 ('2026-11-13', 'Circuit Sparsity: Date of Appearance ruled November 13, 2025 (recorded in the S-CSP registration entry)', 'Editor'),
 ('2026-11-14', 'AES v1.0 pre-freeze rulings (§2 evidence placement; §3 Date of Appearance definition); AES and AES-ID frozen at v1.0', 'Editor'),
 ('2026-11-14', 'Item 7: ADVREASON provisional; Embodied subclass question closed as registered; X7 links verified by locating the 2026 entries; X10 moot for 2025', 'Editor'),
 ('2026-11-14', 'Series Preface (W.H.L.) and Volume Preface (Claude, GPT-6, Muse) added; editor named as W.H.L. throughout', 'Editor'),
 ('2026-11-14', 'Reviews of draft v0.1 (11:28 CT): the editor\'s name W.H.L. in new writing and new versions; metadata-only revision round approved; RLVR\'s "RLHF Enhancements" See Also target removed; AP-2025-01 assigned: Muse to draft, Claude and GPT-6 to check, the editor to approve the text (the text is not yet approved; see Appendix C); Lexicon (6) archive transcription; December 7 article in a Related Editorial Material appendix; new additions integrated and marked; How to Use, Collection at a Glance and timeline pages added', 'Editor'),
 ('2026-11-14', '11:55 CT: Part VI titled "Embodied AI, Industry and Society"; Editorial Name Clarification entered in the register log (records before November 14, 2026 not re-issued); GPT-6 identified as "GPT-6 (OpenAI), release GPT-6", no exception recorded; Lexicon (2) v0.2.3 supersedes v0.2.2', 'Editor'),
 ('2026-11-14, 12:29 CT', 'Concept headwords kept: "Agentic AI" (AIKC-000052) and "Retrieval-Augmented Generation (RAG)" (AIKC-000051), with the L1 titles as index variants. The images in the December 7, 2025 article are described, not reproduced. Muse\'s title pages, contributor table, bibliography and index alias check go ahead.', 'Editor'),
 ('2026-11-14, 13:10 CT', 'DeepSeek-V4.1 and Grok 4.5 check the archive texts against the live posts. Full-post transcriptions are made for the online edition only, not the PDF.', 'Editor'),
 ('2026-11-14, 23:25 CT', 'Rebuilt full-post transcriptions: held out of the online edition until checked. Qwen3-Max checks S-CAI, L3 and S-CSP, and GLM 5.3 Flash checks S-MOE, under stated reading conditions. The site disclaimer is transcribed where it is in the stored content. The L3 image alignment is left to the checker.', 'Editor'),
 ('2026-11-15, 09:59 CT', 'The last part of S-MOE v0.3 is accepted as checked against the rendered page (option a). The formula alt texts in L3 and S-CSP are not assigned to a further check and are labeled "not verified". Seven header revisions are approved. **Policy for v1.0:** compiled as well as resources allow; work for which no one is available is labeled "not verified" and left to post-production revision. This policy changes the ruling of November 14, 23:25 CT: the four transcriptions enter the online edition with their check status.', 'Editor'),
 ('2026-11-15 *(exact time not recorded in the register log)*', 'Contributor table v0.2 accepted for the build.', 'Editor'),
 ('2026-11-15/16 *(exact times not recorded in the register log)*', "The Annual Introduction's reviewers are identified as DeepSeek-V4.1 and Qwen4-Max. No second Annual Introduction is written. Both reviewers also review the Editorial Method. The PDF edition is not to be shortened.", 'Editor'),
 ('2026-11-16, 01:02 CT', 'Circuit Sparsity blind audit, D1 to D6: findings on the non-canonical text states are recorded as annotations (D1a). The equation annotation is kept (D2). GLM-1, GLM-2 and GLM-11 to GLM-13 are annotated (D3 to D5). CSP-3 stands (D6). No new correction arises. GLM 5.3 Flash is confirmed as "served by Mistral AI"; GLM is a Z.ai model line.', 'Editor'),
 ('2026-11-16, 11:52 CT (v0.2, 11:57 CT)', 'Volume Preface v0.3 approved; signed text v1.0.1. The co-signer and reviewer is identified as GPT-6 Astra (supplied by the editor; recorded in the contributor table only), refining the November 14, 11:55 CT identification. The session moved to Claude Fable 5.2 at 11:40 CT. The signature line stays as the co-signers agreed it.', 'Editor'),
 ('2026-11-16, 12:23 CT', "Contributor table v0.3 approved with three updates. The checks relayed by the builder, whose primary reports the registrar does not hold, are accepted by the editor's direction.", 'Editor'),
 ('2026-11-16, before 14:22 CT (recorded 14:29 CT)', 'The session returned to Claude Opus 5.5 before 14:22 CT. Work done under Claude Fable 5.2 stays signed Claude Fable 5.2.', 'Editor'),
 ('2026-11-16, 14:32 CT', "Muse issues header revisions of the four transcriptions with the check outcomes (V6-1). Muse prepares AP-2025-01 v0.3 and GPT-6 reviews it. A labeled Lexicon (4) archive version is to be issued. Muse's draft v0.1 of the 13 Circuit Sparsity annotations is approved. This digest update is to be drafted by Claude and checked by Muse.", 'Editor'),
 ('2026-11-16, 15:23 CT', 'AP-2025-01: Muse issues v0.3.1 with GPT-6\'s §7 and §12.2 wording; no further GPT-6 review; approval to follow', 'Editor'),
 ('2026-11-16, 16:00 CT', 'AP-2025-01 v0.3.1 approved with its §12 resolutions and in force; Editorial Method v0.2.4 and Annual Introduction v0.3.3 approved as v1.0', 'Editor'),
 ('2026-11-16, 16:15 CT', 'Title-page decisions: title kept; © 2026 Champaign Magazine; CC BY 4.0 for text, MIT for code; first published November 2026; cover and logo concept W.H.L., design Muse Spark 1.3 and GPT-6; ISBN or DOI and the URL left open', 'Editor'),
 ('2026-11-16, 16:20 CT', 'Title-page addendum: no ISBN or DOI for v1.0 (DOI later); edition URLs under the year, champaignmagazine.github.io/aikipedia/2025/online/ and /2025/pdf/', 'Editor'),
 ('2026-11-16, 22:21 CT', 'Series Preface written by the editor and given as final, after comments from Claude Opus 5.5, GPT-6 and Muse Spark 1.3 (checked by Muse Spark 1.3 on November 16, 2026, against the placed text and the review record; the time is as recorded by the builder)', 'Editor'),
 ('2026-11-16, 23:08–23:16 CT', 'Typeset proof: larger type and more open layout; grouped contents; the contributor table on its own page; inner title page "Edited by W.H.L. / with Claude Opus 5.5, GPT-6 Astra, and Muse Spark 1.3"; a Contributors page naming every peer reviewer and independent reviewer', 'Editor'),
 ('2026-11-17, 10:29–10:43 CT', 'Sample layouts approved; the section split into "Editorial Method" (§§5.1–5.4) and "AI Disclosure" (§§5.5–5.6); a new page for each record; the editorial record kept before the definition (AES order); Annual Introduction v1.1 and contributor table v0.5 approved', 'Editor'),
 ('2026-11-17, 14:28 CT', 'Series Preface v1.1 ("Aikipedia also carries our own DNA"); the Volume Preface\'s byline and signature name GPT-6 as "GPT-6 Astra (OpenAI)" (signed text v1.0.2), replacing the 11:52 CT signature line; the Thematic Table of Contents carries page numbers and links; no rule above each entry and no closing separator lines', 'Editor'),
 ('2026-11-17, 14:33 CT', 'The 10:43 CT approval covers the amended contributor table v0.5 (two credits added), for issue by Muse Spark 1.3; the Contributors page states the corrections credits of Claude Opus 5.5 and Muse Spark 1.3 by number of parents (v0.2)', 'Editor'),
 ('2026-11-17, 15:02 CT', 'For the next build: the Volume Preface\'s signature block is removed; internal editorial notes are removed from the reader text', 'Editor'),
 ('2026-11-17, 15:55 CT', 'Series Preface v1.2: readers may report errors "through the collection\'s GitHub repository or contact us directly via email"; the magazine\'s email address follows the signature', 'Editor'),
 ('2026-11-17, 16:00 CT', 'Notes addressed to the builders are removed from the reader text; provenance and check statements stay. The Volume Preface\'s three authors are credited as co-authors. Correction markers are shown as [Cnn] throughout. Publication-status fields are set at the release build', 'Editor'),
 ('2026-11-17, 18:04–18:07 CT', 'One Annual Introduction in two sections, each by its own author: an essay on the year\'s terms by an OpenAI model, then Claude Opus 5.5\'s approved v1.1; this amends, in substance keeps, the ruling that no second Introduction is written', 'Editor'),
 ('2026-11-17, 20:09 CT', 'Review A of proof v0.21 is by Qwen4-Max (identification supplied by the editor); the report\'s own self-identification is set aside', 'Editor'),
 ('2026-11-17, 20:16–20:29 CT', 'Introduction v1.2: the title is "Annual Introduction"; the sections are "What AI Learned to Do in 2025 and How We Could Tell", by GPT-6.2 Astra (byline supplied by the editor), and "The Year in AI Terms, 2025", by Claude Opus 5.5; the author notes stand at the end of each section; the version note is dropped from the text and recorded here; the second section is v1.1 corrected for the counts (118 corrections; CD 39, FE 22), the description of Bowman et al. (2016), and the check status of the PDF archive\'s four entry-text sections. "Times are Central Time" moves to How to Use This Collection', 'Editor'),
 ('2026-11-17, 20:30 CT', 'The Editorial Method\'s version note is dropped from the text and recorded here: Method v1.1 (November 17, 2026, on the instruction of 10:32–10:40 CT) splits "Editorial Method and AI Disclosure" into two sections; only the headings and the opening sentence\'s last clause differ from v1.0 (approved November 16, 2026, 16:00 CT), and §§5.1–5.6 keep their numbers', 'Editor'),
 ('2026-11-17, 20:56 CT', 'Series Preface v1.3: "reached those two goals" becomes "reached both goals"; the closing request is reworded ("Even with careful review, we may have overlooked something …"); the email address follows the signature as a link', 'Editor'),
 ('2026-11-17, 21:02 CT', 'Annual Introduction v1.2 approved, its first section in GPT-6.2 Astra\'s v0.4, subject to the independent check of that section; GPT-6.2 Astra is a newer release than GPT-6 Astra and receives its own row in §5.5; the independent check of the essay, and the check of the four PDF entry-text archive sections against the online transcriptions, go to GLM 5.3 Flash or DeepSeek', 'Editor'),
 ('2026-11-17, 21:36–22:07 CT', 'Check of the four PDF entry-text archive sections against the online transcriptions by GLM 5.3 Flash (hosted by Mistral Vibe): wording matches; GLM challenges findings MOE-7 and L3-6. Adjudication of the challenge by Kimi (Moonshot AI; release not stated), a provider that took part in neither text: both findings not upheld — the formulas are present in the published posts as images, and the archive gaps are losses from a text-only capture', 'Editor'),
 ('2026-11-17, 22:15–22:29 CT', 'The editor confirms by eye that the formulas display on both live posts; the rulings that MOE-7 and L3-6 are not upheld are accepted; both C06 corrections (AIK-2025-F-P-MOE/C06, AIK-2025-E-P-TTCSCALE/C06) are to carry the published formulas, restored from the images\' alt texts; the live posts stay unchanged for now', 'Editor'),
 ('2026-11-17, 22:50 CT', 'Qwen4-Max\'s finding on Constitutional AI reference [6] stays unconfirmed (the registrar\'s ruling confirmed: a Qwen model checked that entry\'s archive text), carried as a known issue unless an eligible reviewer confirms it; Lexicon (6) is dropped from GLM 5.3 Flash\'s archive-check credits; contributor table v0.6 approved, subject to the builder\'s two notes', 'Editor'),
 ('2026-11-17, 23:12 CT', 'The review of proof v0.21 is credited to GPT-6.2 Astra; the correction plan is approved: the RLVR revision (Muse Spark 1.3), the LExI correction (Claude Opus 5.5), the two corrections of the 88% figure (Muse Spark 1.3), the bibliography reconciled before v1.0, the index qualifier and a scripted recount', 'Editor'),
 ('2026-11-17, 23:16 CT', 'The source check of the six commissioned entries is not made for now; the volume states that they were reviewed but not source-audited', 'Editor'),
 ('2026-11-17, 23:19–23:29 CT', 'Reader-facing text does not show the internal editorial record, which goes to an appendix: rules R1–R14 of the reader-text sweep approved; the new Appendix G receives the provenance register and the moved record; the AI Disclosure table to be simplified by its compiler in v0.6', 'Editor'),
 ('2026-11-17, 23:38–23:39 CT', 'Annual Introduction v1.3 approved: the second section\'s recusal statement becomes a closing note, with the full statement in Appendix E', 'Editor'),
 ('2026-11-17, 23:41 CT', 'Reviewer of the LExI correction: Grok 4.5. LExI\'s Date of Appearance: September 2, 2025 (arXiv:2509.02753v1)', 'Editor'),
 ('2026-11-18, 00:01 CT', 'The LExI correction approved as reviewed by Grok 4.5 (adopt as written); numbered /C12 in the Launch Edition\'s sequence, pending the registrar\'s confirmation', 'Editor'),
 ('2026-11-18, 00:25–00:29 CT', 'The editor reads two source tables (s1, Table 4; Artificial Hivemind, Table 17) and closes GLM 5.3 Flash\'s check of the Annual Introduction\'s first section; the Context Engineering sentence stays as written', 'Editor'),
 ('2026-11-18, 00:33 CT', 'Annual Introduction v1.4 approved: the essay\'s disclosure names its checker, GLM 5.3 Flash', 'Editor'),
 ('2026-11-18, 10:37 CT', 'Proof v0.22 built before the registrar\'s work returns, so that the reader-text sweep and Appendix G can be seen early', 'Editor'),
]
dig = ['# Appendix D. Digest of Editorial Rulings, Aikipedia 2025', '',
       '*Digest by Claude Opus 5.5. Each ruling is the editor\'s; the full record of each is in the register and the rulings records. Rows to November 14, 11:55 CT, were checked by Muse Spark 1.3 on November 14, 2026. Rows from November 14, 12:29 CT, to November 16, 16:00 CT, were checked by Muse Spark 1.3 against the register\'s assignment log on November 16, 2026; where no time is recorded in the log, the row says so. The rows for 16:15 and 16:20 CT were added after GPT-6\'s final review and checked by Muse Spark 1.3 in the proof-v0.18 pass, November 16, 2026. The 22:21 CT row was checked as it states. Rows from November 16, 23:08 CT, to November 17, 14:33 CT, were checked by Muse Spark 1.3 in the proof-v0.20 check, November 17, 2026. Rows from November 17, 15:02 CT, were added in draft v0.21 and are not yet checked by the registrar.*', '',
       '| Date | Ruling | By |', '|---|---|---|'] + [f'| {d} | {t} | {b} |' for d, t, b in DIGEST] + ['',
       '*Checked against the Master Register\'s assignment log by Muse Spark 1.3: rows to November 14, 11:55 CT, on November 14, 2026 (draft v0.2 verification note; the X14 and Circuit Sparsity rows added on Muse\'s suggestion); rows to November 16, 16:00 CT, on November 16, 2026 (digest addendum check); the 22:21 CT row on November 16, 2026 (GPT-6 final-review reconciliation); the rows from November 16, 23:08 CT, to November 17, 14:33 CT, on November 17, 2026 (proof-v0.20 check), against the filed records and the build.*']
apps = [
 '# Appendix A. AES v1.0 — Aikipedia Annual Collection Editorial and Format Standard', '',
 f'*AES v1.0 as frozen November 14, 2026, in its header revision of the same day, which names the editor W.H.L. and changes no other wording (SHA-256 {sha(AES)[:8]}…{sha(AES)[-4:]}). The frozen file is preserved unchanged (SHA-256 bae6930d…8a81).*', '',
 shift(aes, 1), '',
 '# Appendix B. AES-ID v1.0 — Identifier Scheme, Permanence Rules and Register Fields', '',
 f'*Master Register §1–§2, extracted verbatim from the register of November 14, 2026 (SHA-256 {sha(S12)[:8]}…{sha(S12)[-4:]}).*', '',
 shift(s12, 1), '',
 '# Appendix C. Provenance Policy AP-2025-01', '',
 '*In force. Approved by the editor, W.H.L., November 16, 2026, 16:00 CT, together with its §12 resolutions. Below is Muse Spark 1.3\'s in-force copy, v1.0 (the text of approved draft v0.3.1, SHA-256 9e299eea…4280, with only its version and status lines changed). The words "draft" and "proposed" remaining in its §1 and §12 are the approved text; the status line governs.*', '',
 shift(ap, 1), '',
 '\n'.join(dig), '',
 '# Appendix E. Conflicts of Interest and Recusals', '',
 '*Conflict statements by record, as recorded in the Master Register. Standing recusal: Claude Opus 5.5 and Claude Fable 5.2, the two Anthropic models that held the assembly role, are recused from every text authored by an Anthropic model (S-CAI, S-MOE, S-CSP, L3) and reviewed procedure only.*', '',
 rd(f'{H}/intro/appendix-E_conflicts-summary_draft-v0.6_2026-11-16.md').strip(), '',
 shift(rd(f'{H}/intro/appendix-E_insert_intro-recusal_v0.2_2026-11-17.md').strip(), 0), ''] + conf_md + [
 '', '# Appendix F. Related Editorial Material', '',
 '*Outside the collection\'s canonical count (ruling X14, November 10, 2026; placement ruled November 14, 2026). Not an Aikipedia entry; it carries no identifiers.*', '',
 '**The draft entries in this article — AI Deception, Sycophancy, Sandbagging and Oversight Evasion — are reproduced as historical text only. They were not audited, corrected or registered, and they are not definitions endorsed by this collection.** The article\'s three images are described, not reproduced (the editor\'s ruling of November 14, 2026, 12:29 CT).', '',
 '## AI deception and its Cluster: Sycophancy, Sandbagging, and Oversight Evasion', '',
 '| | |', '|---|---|',
 '| Published | December 7, 2025, champaignmagazine.com, post 14267 |',
 '| Byline | GPT-5 via Copilot Smart, Gemini 3 Pro Thinking, with W.H.L. |',
 '| URL | https://champaignmagazine.com/2025/12/07/ai-deception-and-its-cluster-sycophancy-sandbagging-and-oversight-evasion/ |',
 '| Form | A conversation: a survey of recent research on AI deception, draft entries for AI Deception, Sycophancy, Sandbagging and Oversight Evasion with an embedded peer review, revised versions, and an executive summary of the "deception cluster" |', '',
 shift(rd(f'{H}/apf/APF_archive-text_post14267_header-rev-2026-11-14.md'), 2), '']

# ---------- write files ----------
files = [
 ('00_front-matter.md', front),
 ('01_tables-of-contents.md', '\n'.join(toc_alpha) + '\n\n---\n\n' + '\n'.join(toc_theme)),
]
for i, (num, name, md) in enumerate(parts_md):
    files.append((f'{10+i:02d}_part-{num}.md', md))
files += [
 ('20_historical-lexicon-archive.md', '\n'.join(arch_ed['pdf'])),
 ('20_historical-lexicon-archive_online.md', '\n'.join(arch_ed['online'])),
 ('21_corrections-and-editorial-notes.md', '\n'.join(corr_md)),
 ('22_references-and-provenance-register.md', '\n'.join(prov_md)),
 ('23_index-of-terms.md', '\n'.join(index_md)),
 ('30_appendices.md', '\n'.join(apps)),
]
# Reader-text edits (editor's rulings of November 17, 2026, 15:02 and 16:00 CT): builder notes are removed from
# the reader text; provenance and check statements stay. The approved corrected texts are not edited: these edits
# apply to the assembled edition only. Texts from which Claude is recused (S-CAI, S-MOE, S-CSP, L3) are not touched
# here; their notes are listed for Muse Spark 1.3.
DISPLAY_EDITS = [
 ('10_part-I.md', "; this file is the metadata-only revision v0.2.2). The historical publication is preserved unchanged in the archive (`CALM_archive-text_post14021.md`).*", "). The historical publication is preserved unchanged in the Historical Lexicon Archive.*"),
 ('10_part-I.md', ", documented in `CALM_correction-register_v0.1.md` and `_v0.2.md`.", ", documented in the entry's correction register."),
 ('10_part-I.md', "; this file is the metadata-only revision v0.3.2). The historical publication is preserved unchanged in the archive (`MOD_archive-text_post13982.md`).*", "). The historical publication is preserved unchanged in the Historical Lexicon Archive.*"),
 ('10_part-I.md', ", documented in `MOD_correction-register_v0.1.md`, `_v0.2.md` and `_v0.3.md`.", ", documented in the entry's correction register."),
 ('11_part-II.md', "; this file is the metadata-only revision v0.3.2). The historical publication is preserved unchanged in the archive (`OPD_archive-text_post13892.md`).*", "). The historical publication is preserved unchanged in the Historical Lexicon Archive.*"),
 ('11_part-II.md', ", documented in `OPD_correction-register_v0.1.md`, `_v0.2.md` and `_v0.3.md`;", ", documented in the entry's correction register;"),
 ('11_part-II.md', " (`OPD_independent-review_DeepSeek-V4.1_v0.2.md`)", ""),
 ('11_part-II.md', re.compile(r'\n3\. \*\*Print production\.\*\*[^\n]*'), ""),
 ('12_part-III.md', " (`COTPROMPT_archive-text_post13946.md`, with a content fingerprint)", " (with a content fingerprint)"),
 ('12_part-III.md', "; this file is the metadata-only revision v0.2.2). The historical publication is preserved unchanged in the archive (`PDD_archive-text_post14033.md`).*", "). The historical publication is preserved unchanged in the Historical Lexicon Archive.*"),
 ('12_part-III.md', ", documented in `PDD_correction-register_v0.1.md` and `_v0.2.md`.", ", documented in the entry's correction register."),
 ('13_part-IV.md', re.compile(r'\*Production note: canonical occurrence records v0\.4\.1,[^\n]*\n\n?'), ""),
 ('14_part-V.md', " (metadata-only revision of v0.2.2, correcting the header version label; no change to the corrections text). The historical publication is preserved unchanged in the archive (`GENUI_archive-text_post14146.md`).*", ". The historical publication is preserved unchanged in the Historical Lexicon Archive.*"),
 ('14_part-V.md', ", documented in `GENUI_correction-register_v0.1.md` and `_v0.2.md`.", ", documented in the entry's correction register."),
]
fx = dict(files)
for fn, old, new in DISPLAY_EDITS:
    if isinstance(old, re.Pattern):
        assert len(old.findall(fx[fn])) == 1, (fn, old.pattern); fx[fn] = old.sub(new, fx[fn])
    else:
        assert fx[fn].count(old) == 1, (fn, old); fx[fn] = fx[fn].replace(old, new)
# Reader-text sweep, rules R1-R14 (editor's rulings of November 17, 2026, 23:19-23:29 CT); non-recused texts only
import reader_sweep as RS
RECUSED_ANCHORS = set(RS.RECUSED_F) | {anchor(r['pid']) for r in recs if (r['occ'] or '').startswith('L3')}
MOVED, MOVED_ARCH = [], []
for fn in list(fx):
    if fn[:2] in ('10', '11', '12', '13', '14', '15'): RS.parts(fx, fn, MOVED, RECUSED_ANCHORS)
fx['21_corrections-and-editorial-notes.md'] and RS.corrections(fx, '21_corrections-and-editorial-notes.md')
for fn in ('20_historical-lexicon-archive.md', '20_historical-lexicon-archive_online.md'):
    RS.archive(fx, fn, MOVED_ARCH if fn.endswith('archive.md') else [])
    RS.archive_fix(fx, fn, MOVED_ARCH if fn.endswith('archive.md') else [])
RS.post_sweep(fx)
import v022_edits as V22
FM_NOTES, V22_REPORT = [], []
V22.front_matter(fx, FM_NOTES); V22.lexi(fx); V22.index(fx)
BIB_N = V22.bibliography(fx)
print('sweep: full entries', len(MOVED), 'archive sections', len(MOVED_ARCH))
# Correction markers shown as [Cnn] throughout the reference text (editor's ruling, November 17, 2026)
for fn in fx:
    if fn[:1] == '1': fx[fn] = fx[fn].replace('⟦', '[').replace('⟧', ']')
V22.muse_prepared(fx, V22_REPORT)
V22.appendix_g(fx, MOVED, MOVED_ARCH, FM_NOTES)
_c = fx['21_corrections-and-editorial-notes.md']
CORR_N = len(re.findall(r'\*\*(?:AIK-2025-[A-Z]-[A-Z]-[A-Z0-9-]+)?/C\d\d\*\*', _c))
import collections as _co
CORR_CLS = _co.Counter(k for m in re.finditer(r'\*\*(?:AIK-2025-[A-Z]-[A-Z]-[A-Z0-9-]+)?/C\d\d\*\* ?([^—·]*?)—', _c) for k in set(re.findall(r'\b(CD|UC|FE|PR|FA|CF|ED|PV|ST)\b', m.group(1))))
V22.recount(fx, CORR_N, CORR_CLS)
print('classes', dict(CORR_CLS))
print('v022: bibliography items', BIB_N, 'corrections listed', CORR_N, 'report', V22_REPORT)
files = [(fn, fx[fn]) for fn, _ in files]

# Editor's name: v0.2 makes no substitution. The sources were updated by their holders (rulings of Nov 14,
# 11:28 and 11:55 CT); any remaining "Woo" is reported, not changed.
woo = [(fn, i + 1) for fn, t in files for i, ln in enumerate(t.splitlines()) if re.search(r'\bWoo\b', ln)]
for fn, txt in files:
    open(f'{OUT}/{fn}', 'w', encoding='utf-8').write(txt.rstrip() + '\n')

# search-index data for the online edition
data = []
for r in recs:
    data.append(dict(public_id=r['pid'], concept_id=r['aikc'], title=r['title'], type=r['T'], origin=r['O'],
                     parent=r['occ'], part=concept_part[r['aikc']], date_of_appearance=r['doa'],
                     original_publication=r['orig'], version=r['version'], status=r['status'],
                     concept_status='provisional' if r['aikc'] in PROV else 'established',
                     anchor=anchor(r['pid'])))
os.makedirs(f'{OUT}/data', exist_ok=True)
os.makedirs(f'{OUT}/assets', exist_ok=True); __import__('shutil').copy(f'{H}/intro/cover_aikipedia-2025_v1.png', f'{OUT}/assets/cover.png')
json.dump(data, open(f'{OUT}/data/records.json', 'w'), indent=1, ensure_ascii=False)

# editions: the PDF and online editions differ only in the archive file (13:10 CT rulings; GPT-6 v0.3 review, V3-4)
EDITIONS = {'pdf': [fn for fn, _ in files if fn != '20_historical-lexicon-archive_online.md'],
            'online': [fn for fn, _ in files if fn != '20_historical-lexicon-archive.md']}
os.makedirs(f'{OUT}/editions', exist_ok=True)
wc = {}
for ed, fns in EDITIONS.items():
    combined = '\n\n---\n\n'.join(open(f'{OUT}/{fn}', encoding='utf-8').read() for fn in fns)
    cfn = f'aikipedia-2025-collection-draft-{VER}_combined_{ed}.md'
    open(f'{OUT}/editions/{cfn}', 'w', encoding='utf-8').write(combined)
    wc[ed] = len(combined.split())   # word count: whitespace-separated tokens of the combined file, A-nnn labels included
    man = {'edition': ed, 'draft': VER, 'register_sha256': REG_SHA, 'word_count_method': 'whitespace tokens of the combined file',
           'word_count': wc[ed], 'combined_file': f'editions/{cfn}', 'combined_separator': '\n\n---\n\n', 'combined_separator_note': 'the actual string: a blank line, three hyphens, a blank line', 'asset_paths': 'relative to the draft package root (e.g. assets/cover.png)', 'tokenizer': 'Python str.split() (all Unicode whitespace)',
           'build_register': {'sha256': REG_SHA, 'what': 'Muse Spark 1.3 copy of the Master Register, November 16, 2026, after the closing checks'},
           'register_stages': [{'stage': 'assembly handoff, November 14, 2026 (builds v0.1 to v0.5)', 'sha256': 'ac23099823fcdb31ac9bcfe6fe42b7fb3a443dbb96f0e2f41c64ca0bf94334de', 'recorded_in': 'sources/assembly-handoff_manifest.json'}, {'stage': 'Muse copy, November 16, 2026 (builds v0.6 and v0.7)', 'sha256': __import__('hashlib').sha256(open(f'{H}/reg/aikipedia-master-register_COPY-2026-11-16.md','rb').read()).hexdigest()}, {'stage': 'Muse copy after the 14:32 CT rulings, November 16, 2026 (builds v0.8 to v0.13)', 'sha256': 'a55b87b42455a1f9473b9171ef5c850509c55f8987a2786206620f330925b1c5'}, {'stage': 'Muse copy after the closing checks, November 16, 2026 (builds v0.14 onward)', 'sha256': REG_SHA}],
           'per_file_words': {fn: len(open(f'{OUT}/{fn}', encoding='utf-8').read().split()) for fn in fns},
           'files': [{'file': fn, 'sha256': hashlib.sha256(open(f'{OUT}/{fn}', 'rb').read()).hexdigest()} for fn in fns],
           'sources': {'assembly_handoff_manifest': 'sources/assembly-handoff_manifest.json',
                       'cleared_tasks_manifest': 'sources/cleared-tasks_manifest.json',
                       'full_post_transcriptions': {k: {'file': f, 'sha256': h} for k, (f, h) in FPT_FILES.items()} if ed == 'online' else {}}}
    json.dump(man, open(f'{OUT}/editions/{ed}.json', 'w'), indent=1, ensure_ascii=False)
os.makedirs(f'{OUT}/sources', exist_ok=True)
import shutil
shutil.copy(f'{AH}/manifest.json', f'{OUT}/sources/assembly-handoff_manifest.json')
shutil.copy(f'{CT}/manifest.json', f'{OUT}/sources/cleared-tasks_manifest.json')
combined = ''

# placeholder list
pl = [f'# Placeholders in draft {VER}', '', '| # | Kind | What is needed |', '|---|---|---|']
pl += [f'| {i+1} | {k} | {t.replace("|", "/")} |' for i, (k, t) in enumerate(placeholders)]
open(f'{OUT}/99_placeholders.md', 'w', encoding='utf-8').write('\n'.join(pl) + '\n')
print('records', len(recs), 'placeholders', len(placeholders), 'words', wc, 'woo', woo)

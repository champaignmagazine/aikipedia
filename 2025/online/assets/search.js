// Search for the Aikipedia 2025 online edition: loads data/search.json once and filters in the browser.
(function () {
  const $ = id => document.getElementById(id);
  let items = [];
  const esc = s => String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const fold = s => String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/[’‘]/g, "'").replace(/[“”]/g, '"');
  function terms(q) { const out = []; fold(q).replace(/"([^"]+)"|(\S+)/g, (_, p, w) => { out.push(p || w); return ''; }); return out.filter(Boolean); }
  function snippet(text, ts) {
    const t = String(text || ''); const ft = fold(t);
    let i = -1; for (const x of ts) { i = ft.indexOf(x); if (i >= 0) break; }
    let s = esc(i < 0 ? t.slice(0, 220) : (i > 80 ? '…' : '') + t.slice(Math.max(0, i - 80), i + 160));
    for (const x of ts) { if (x.length < 2) continue; s = s.replace(new RegExp('(' + x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>'); }
    return s + (t.length > 240 ? '…' : '');
  }
  function run() {
    const q = $('q').value, k = $('k').value, ts = terms(q);
    const ORD = { 'Entry': 0, 'Archive post': 1, 'Section': 2 };
    const res = items.filter(it => (!k || it.k === k) && (!ts.length || ts.every(t => fold(it.t + ' ' + it.x).includes(t)))).sort((a, b) => ((ORD[a.k] ?? 3) - (ORD[b.k] ?? 3)) || (ts.every(t => fold(b.t).includes(t)) - ts.every(t => fold(a.t).includes(t))));
    $('count').textContent = ts.length || k ? res.length + (res.length === 1 ? ' result' : ' results') : '';
    $('res').innerHTML = (ts.length || k) ? res.slice(0, 200).map(it =>
      `<li><div class="t"><a href="${it.u}">${esc(it.t)}</a></div><div class="small">${esc(it.k)}</div><div class="s">${snippet(it.x, ts)}</div></li>`).join('') : '';
    const p = new URLSearchParams(); if (q) p.set('q', q); if (k) p.set('k', k); history.replaceState(null, '', '?' + p.toString());
  }
  const qp = new URLSearchParams(location.search); if (qp.has('q')) $('q').value = qp.get('q'); if (qp.has('k')) $('k').value = qp.get('k');
  fetch('data/search.json').then(r => r.json()).then(d => { items = d; run(); });
  ['q', 'k'].forEach(id => $(id).addEventListener('input', run));
})();

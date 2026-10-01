/* Link-A-Link load calculator: static, no dependencies. */
(function () {
  const G = 9.81;
  const CRANK = 30.5; // mm lateral offset between the two rosettes of a Standard Link

  const SEGMENTS = [
    ...[125, 150, 175, 200, 225, 250, 275, 300].map(n => ({ id: `link${n}`, label: `Standard Link ${n}`, pitch: Math.hypot(n, CRANK), mass: p => p[`link${n}`], joint: true })),
    ...[60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300].map(n => ({ id: `mod${n}`, label: `Modular Link, ${n} body (≈${n + 100})`, pitch: n + 100, mass: p => p[`body${n}`] + p.modends, joint: true })),
    { id: 'pl50', label: 'Payload Link 50', pitch: 50, mass: p => p.pl50, joint: false, end: true },
    { id: 'pl75', label: 'Payload Link 75', pitch: 75, mass: p => p.pl75, joint: false, end: true },
    { id: 'pl100', label: 'Payload Link 100', pitch: 100, mass: p => p.pl100, joint: false, end: true },
    { id: 'swivel', label: 'Swivel Payload Link', pitch: 76, mass: p => p.swivel, joint: false, end: true },
  ];

  // Ballast cavity estimates (cm³) and densities (g/cm³)
  const BASES = {
    clamp: { label: 'Clamp / screwed down (no tip check)', R: null },
    round180: { label: 'Round Base 180', R: 90, mass: p => p.round180 + p.deskjoint },
    round200: { label: 'Round Base 200', R: 100, mass: p => p.round200 + p.deskjoint },
    round220: { label: 'Round Base 220', R: 110, mass: p => p.round220 + p.deskjoint },
    round240: { label: 'Round Base 240', R: 120, mass: p => p.round240 + p.deskjoint },
    wbS: { label: 'Weighted Base Small (125)', R: 62, mass: p => p.wb_S + p.wbjoint, cavity: 300 },
    wbM: { label: 'Weighted Base Medium (175)', R: 87, mass: p => p.wb_M + p.wbjoint, cavity: 750 },
    wbL: { label: 'Weighted Base Large (225)', R: 112, mass: p => p.wb_L + p.wbjoint, cavity: 1300 },
  };
  const BALLAST = { none: 0, sand: 1.5, steel: 4.5 };

  function el(tag, attrs = {}, html = '') { const e = document.createElement(tag); Object.entries(attrs).forEach(([k, v]) => e.setAttribute(k, v)); e.innerHTML = html; return e; }

  function init() {
    const root = document.getElementById('lal-calc');
    if (!root || root.dataset.ready) return;
    root.dataset.ready = '1';
    const M = window.LAL_MASSES;

    const segOptions = SEGMENTS.map(s => `<option value="${s.id}">${s.label}</option>`).join('');
    root.innerHTML = `
      <div class="calc-grid">
        <label>Payload (device + its mount), g<input id="c-payload" type="number" value="500" min="0" step="10"></label>
        <label>Device centre of mass beyond the payload link, mm<input id="c-offset" type="number" value="30" step="5"></label>
        <label>Print profile<select id="c-profile"><option value="pla">PLA+ · 4 walls · 20 %</option><option value="petg">PETG · 6 walls · 40 %</option></select></label>
        <label>Base<select id="c-base">${Object.entries(BASES).map(([k, b]) => `<option value="${k}">${b.label}</option>`).join('')}</select></label>
        <label>Ballast (weighted bases)<select id="c-ballast"><option value="none">Empty</option><option value="sand">Dry sand</option><option value="steel" selected>Steel BBs / shot</option></select></label>
      </div>
      <h3>Chain (from the base outward)</h3>
      <p class="calc-hint">Angle is measured from horizontal: 90 = straight up, 0 = level, −90 = straight down.</p>
      <table class="calc-chain"><thead><tr><th>#</th><th>Segment</th><th>Angle °</th><th></th></tr></thead><tbody id="c-rows"></tbody></table>
      <p><button class="md-button" id="c-add">+ Add segment</button> <button class="md-button" id="c-preset">Load example (starter webcam arm)</button></p>
      <div id="c-out"></div>
      <div id="c-svg"></div>`;

    const rows = root.querySelector('#c-rows');
    function addRow(id = 'link200', ang = 45) {
      const tr = el('tr');
      tr.innerHTML = `<td class="n"></td><td><select>${segOptions}</select></td><td><input type="number" value="${ang}" step="5" min="-90" max="90"></td><td><button class="md-button rm" title="Remove">✕</button></td>`;
      tr.querySelector('select').value = id;
      tr.querySelector('.rm').onclick = () => { tr.remove(); calc(); };
      tr.querySelectorAll('select,input').forEach(i => i.addEventListener('input', calc));
      rows.appendChild(tr);
    }
    function preset() { rows.innerHTML = ''; addRow('link200', 72); addRow('link150', 8); addRow('pl50', -10); root.querySelector('#c-payload').value = 300; root.querySelector('#c-offset').value = 30; calc(); }
    root.querySelector('#c-add').onclick = () => { addRow('link150', 0); calc(); };
    root.querySelector('#c-preset').onclick = preset;
    root.querySelectorAll('#c-payload,#c-offset,#c-profile,#c-base,#c-ballast').forEach(i => i.addEventListener('input', calc));

    function calc() {
      const P = M[root.querySelector('#c-profile').value];
      const payload = +root.querySelector('#c-payload').value || 0;
      const offset = +root.querySelector('#c-offset').value || 0;
      const trs = [...rows.children];
      trs.forEach((tr, i) => tr.querySelector('.n').textContent = i + 1);
      // build geometry
      let x = 0, y = 0, lastAng = 0;
      const joints = [{ x, y }];          // joint 0 = base pivot
      const masses = [];                  // {m (g), x, y, kind}
      const pts = [{ x, y }];
      trs.forEach((tr, i) => {
        const seg = SEGMENTS.find(s => s.id === tr.querySelector('select').value);
        const ang = (+tr.querySelector('input').value || 0) * Math.PI / 180; lastAng = ang;
        const nx = x + seg.pitch * Math.cos(ang), ny = y + seg.pitch * Math.sin(ang);
        masses.push({ m: seg.mass(P), x: (x + nx) / 2, y: (y + ny) / 2, kind: 'arm', seg: i });
        // one link-hardware set at the joint where this segment starts
        masses.push({ m: P.hw, x, y, kind: 'arm', seg: i });
        x = nx; y = ny; pts.push({ x, y });
        if (seg.joint) joints.push({ x, y });
      });
      const px = x + offset * Math.cos(lastAng), py = y + offset * Math.sin(lastAng);
      masses.push({ m: payload, x: px, y: py, kind: 'payload', seg: trs.length });

      // torque at each joint k: everything attached beyond it (segments with index >= k)
      const res = joints.map((j, k) => {
        let t = 0, tArm = 0;
        masses.filter(mm => mm.seg >= k).forEach(mm => {
          const tq = mm.m / 1000 * G * (mm.x - j.x) / 1000; t += tq; if (mm.kind === 'arm') tArm += tq;
        });
        return { k, t, tArm };
      });
      const armMass = masses.filter(m => m.kind === 'arm').reduce((a, b) => a + b.m, 0);
      const kgm = t => Math.abs(t) / G;
      const band = v => v < 0.15 ? ['ok', 'Comfortable'] : v < 0.35 ? ['warn', 'Firm: PETG, tighten well'] : v < 0.6 ? ['hot', 'Heavy: PETG/ASA, 5–8 walls, clamp or screw-down'] : ['bad', 'Past what this guide would trust'];

      let html = `<div class="spec">
        <div><b>Reach (tip)</b><span>${Math.round(px)} mm</span></div>
        <div><b>Height above first pivot</b><span>${Math.round(py)} mm</span></div>
        <div><b>Printed arm mass</b><span>≈ ${Math.round(armMass)} g</span></div>
        <div><b>Total above base</b><span>≈ ${Math.round(armMass + payload)} g</span></div></div>`;
      html += `<table><thead><tr><th>Joint</th><th>Torque</th><th>kg·m</th><th>From arm self-weight</th><th>Verdict</th></tr></thead><tbody>`;
      res.forEach(r => {
        const v = kgm(r.t), [c, txt] = band(v);
        html += `<tr><td>${r.k === 0 ? 'Base pivot' : 'Joint ' + r.k}</td><td>${Math.abs(r.t).toFixed(2)} N·m</td><td>${v.toFixed(3)}</td><td>${r.t ? Math.round(100 * r.tArm / r.t) : 0} %</td><td><span class="verdict ${c}">${txt}</span></td></tr>`;
      });
      html += `</tbody></table>`;

      // tip-over check for free-standing bases
      const bk = root.querySelector('#c-base').value, B = BASES[bk];
      if (B.R) {
        const dens = BALLAST[root.querySelector('#c-ballast').value];
        const baseM = B.mass(P) + (B.cavity ? B.cavity * dens : 0);
        const dir = Math.sign(px) || 1, R = B.R * dir;
        let restore = baseM * B.R, tip = 0;
        masses.forEach(mm => { const d = (R - mm.x) * dir; if (d >= 0) restore += mm.m * d; else tip += -mm.m * d; });
        const sf = tip ? restore / tip : Infinity;
        const [c, txt] = sf >= 2 ? ['ok', 'Stable'] : sf >= 1.3 ? ['warn', 'Marginal: a bump will tip it'] : ['bad', 'Will tip over'];
        html += `<p><b>Tip-over check</b> (${B.label}${B.cavity ? `, ≈ ${Math.round(baseM)} g with ballast` : `, ≈ ${Math.round(baseM)} g`}): safety factor <b>${isFinite(sf) ? sf.toFixed(1) : '∞'}</b> <span class="verdict ${c}">${txt}</span></p>`;
      }
      root.querySelector('#c-out').innerHTML = html;

      // sketch
      const xs = pts.map(p => p.x).concat([px, 0, -60]), ys = pts.map(p => p.y).concat([py, 0, -60]);
      const minx = Math.min(...xs) - 60, maxx = Math.max(...xs) + 60, miny = Math.min(...ys) - 60, maxy = Math.max(...ys) + 60;
      let s = `<svg class="bp" viewBox="${minx} ${-maxy} ${maxx - minx} ${maxy - miny}" xmlns="http://www.w3.org/2000/svg"><rect x="${minx}" y="${-maxy}" width="${maxx - minx}" height="${maxy - miny}" class="bpbg"/>`;
      s += `<line x1="${minx}" y1="60" x2="${maxx}" y2="60" class="dim" stroke-dasharray="6 6"/>`;
      for (let i = 1; i < pts.length; i++) s += `<line x1="${pts[i - 1].x}" y1="${-pts[i - 1].y}" x2="${pts[i].x}" y2="${-pts[i].y}" class="lnk" stroke-width="24" stroke-linecap="round"/>`;
      joints.forEach(j => s += `<circle cx="${j.x}" cy="${-j.y}" r="26" class="jnt"/>`);
      s += `<circle cx="${px}" cy="${-py}" r="${10 + Math.sqrt(payload) * 0.8}" class="co" opacity=".85"/>`;
      s += `</svg>`;
      root.querySelector('#c-svg').innerHTML = s;
    }
    preset();
  }
  if (window.document$) window.document$.subscribe(init); else document.addEventListener('DOMContentLoaded', init);
})();

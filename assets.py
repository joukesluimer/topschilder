# -*- coding: utf-8 -*-
"""
Topschilder.nl — CSS, JavaScript en favicon.

Deze staan hier als tekst zodat de hele site uit een handvol losse bestanden
bestaat en er geen mappenstructuur nodig is in de repository. build.py schrijft
ze bij elke build weg naar site/assets/.

Wil je de Supabase-koppeling aanpassen? Dat doe je onderin dit bestand in
CONFIG_JS. Vormgeving zit in STYLE_CSS.
"""

STYLE_CSS = r'''/* Topschilder.nl — eigen CSS, geen frameworks. ~14kb, geen render-blocking JS. */

:root{
  --navy:#3c290f;
  --navy-700:#513a17;
  --navy-500:#6b5024;
  --accent:#f4820b;
  --accent-dark:#d96f00;
  --accent-soft:#fff4e6;
  --green:#0f8a5f;
  --ink:#241906;
  --body:#57492f;
  --muted:#6f6047;
  --line:#e9e2d6;
  --bg:#ffffff;
  --bg-soft:#faf7f1;
  --radius:12px;
  --radius-lg:18px;
  --shadow:0 1px 2px rgba(60,41,15,.06), 0 8px 24px rgba(60,41,15,.07);
  --shadow-lg:0 2px 4px rgba(60,41,15,.06), 0 18px 46px rgba(60,41,15,.13);
  --max:1160px;
  --font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{
  margin:0;font-family:var(--font);color:var(--body);
  font-size:17px;line-height:1.65;background:var(--bg);
  -webkit-font-smoothing:antialiased;
}
img{max-width:100%;height:auto;display:block}
a{color:var(--navy-500);text-decoration:none}
a:hover{text-decoration:underline}
p a,li a,td a{text-decoration:underline;text-underline-offset:2px;text-decoration-thickness:1px}
.btn,.chips a,.places a,nav a,.footer a,.crumbs a{text-decoration:none}
h1,h2,h3,h4{color:var(--ink);line-height:1.2;margin:0 0 .5em;font-weight:750;letter-spacing:-.02em}
h1{font-size:clamp(1.85rem,4.2vw,3rem)}
h2{font-size:clamp(1.4rem,2.7vw,2.1rem);margin-top:0}
h3{font-size:1.17rem;font-weight:700}
p{margin:0 0 1.1em}
ul,ol{margin:0 0 1.2em;padding-left:1.3em}
li{margin-bottom:.5em}
hr{border:0;border-top:1px solid var(--line);margin:2.5rem 0}
small{font-size:.85rem}

.wrap{max-width:var(--max);margin:0 auto;padding:0 20px}
.narrow{max-width:760px}
.section{padding:64px 0}
.section-sm{padding:44px 0}
.soft{background:var(--bg-soft)}
.dark{background:var(--navy);color:#c7d6e5}
.dark h1,.dark h2,.dark h3{color:#fff}
.dark a{color:#ffd9ab}
.center{text-align:center}
.lead{font-size:1.14rem;color:var(--body)}
.mt0{margin-top:0}.mb0{margin-bottom:0}

/* ---------- Header ---------- */
.header{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.96);backdrop-filter:saturate(140%) blur(8px);border-bottom:1px solid var(--line)}
.header-in{display:flex;align-items:center;gap:24px;height:70px}
.logo{display:flex;align-items:center;gap:9px;font-weight:800;font-size:1.28rem;color:var(--navy);letter-spacing:-.03em}
.logo:hover{text-decoration:none}
.logo-mark{width:30px;height:30px;flex:0 0 30px;border-radius:8px;background:linear-gradient(135deg,var(--accent),var(--accent-dark));display:grid;place-items:center;color:#fff;font-size:1rem}
.logo span.dot{color:var(--accent)}
.nav{display:flex;gap:4px;margin-left:auto;align-items:center}
.nav a{color:var(--ink);font-size:.95rem;font-weight:600;padding:9px 13px;border-radius:8px}
.nav a:hover{background:var(--bg-soft);text-decoration:none}
.nav .btn{margin-left:8px}
.burger{display:none;margin-left:auto;background:none;border:1px solid var(--line);border-radius:9px;padding:9px 11px;cursor:pointer;font-size:1.1rem;line-height:1}

@media(max-width:900px){
  .nav{display:none;position:absolute;top:70px;left:0;right:0;background:#fff;flex-direction:column;align-items:stretch;padding:12px 20px 20px;border-bottom:1px solid var(--line);box-shadow:var(--shadow)}
  .nav.open{display:flex}
  .nav a{padding:12px 6px}
  .nav .btn{margin:8px 0 0;text-align:center}
  .burger{display:block}
}

/* ---------- Buttons ---------- */
.btn{
  display:inline-block;padding:13px 24px;border-radius:10px;font-weight:700;font-size:1rem;
  border:1px solid transparent;cursor:pointer;font-family:inherit;text-align:center;
  transition:transform .12s ease, box-shadow .12s ease, background .12s ease;
}
.btn:hover{text-decoration:none;transform:translateY(-1px)}
.btn-primary{background:var(--accent);color:#fff;box-shadow:0 3px 0 var(--accent-dark)}
.btn-primary:hover{background:var(--accent-dark);box-shadow:0 4px 0 #b85e00;color:#fff}
.btn-dark{background:var(--navy);color:#fff}
.btn-dark:hover{background:var(--navy-700);color:#fff}
.btn-ghost{background:#fff;border-color:var(--line);color:var(--ink)}
.btn-ghost:hover{border-color:var(--navy-500);color:var(--navy)}
.btn-lg{padding:16px 32px;font-size:1.07rem}
.btn-block{display:block;width:100%}

/* ---------- Hero ---------- */
.hero{background:linear-gradient(165deg,var(--navy) 0%,#241906 60%,#5c431a 100%);color:#c7d6e5;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;inset:auto -10% -60% 40%;height:520px;background:radial-gradient(closest-side,rgba(244,130,11,.20),transparent);pointer-events:none}
.hero-in{display:grid;grid-template-columns:1.05fr .95fr;gap:52px;align-items:center;padding-top:74px;padding-bottom:84px;position:relative;z-index:2}
.hero h1{color:#fff;margin-bottom:.4em}
.hero p.lead{color:#b8cadd;font-size:1.16rem;max-width:52ch}
.hero-usps{list-style:none;padding:0;margin:26px 0 30px}
.hero-usps li{display:flex;gap:11px;align-items:flex-start;margin-bottom:11px;color:#dbe7f2;font-weight:500}
.check{flex:0 0 22px;width:22px;height:22px;border-radius:50%;background:rgba(255,255,255,.13);color:#7ee2b0;display:grid;place-items:center;font-size:.72rem;margin-top:2px;font-weight:700}
.hero-proof{display:flex;gap:26px;flex-wrap:wrap;align-items:center;margin-top:8px;font-size:.9rem;color:#9db3c9}
.stars{color:#ffc043;letter-spacing:2px}

@media(max-width:920px){
  .hero-in{grid-template-columns:1fr;gap:34px;padding-top:48px;padding-bottom:56px}
}

/* ---------- Formulier-kaart ---------- */
.formcard{background:#fff;border-radius:var(--radius-lg);box-shadow:var(--shadow-lg);padding:28px;color:var(--body)}
.formcard h2{font-size:1.32rem;margin-bottom:.25em}
.formcard .sub{font-size:.93rem;color:var(--muted);margin-bottom:20px}
.steps{display:flex;gap:6px;margin-bottom:22px}
.steps div{flex:1;height:5px;border-radius:99px;background:var(--line)}
.steps div.on{background:var(--accent)}
.step{display:none}
.step.active{display:block;animation:fade .22s ease}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}

label{display:block;font-weight:650;color:var(--ink);font-size:.93rem;margin-bottom:6px}
.hint{font-weight:400;color:var(--muted);font-size:.85rem}
input[type=text],input[type=email],input[type=tel],input[type=number],select,textarea{
  width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:10px;font-size:1rem;
  font-family:inherit;color:var(--ink);background:#fff;transition:border-color .12s
}
input:focus,select:focus,textarea:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(244,130,11,.14)}
textarea{min-height:110px;resize:vertical}
.field{margin-bottom:16px}
.row2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
@media(max-width:560px){.row2{grid-template-columns:1fr}}

.choice{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-bottom:4px}
@media(max-width:560px){.choice{grid-template-columns:1fr}}
.choice label{
  display:flex;align-items:center;gap:10px;border:1.5px solid var(--line);border-radius:10px;
  padding:13px 14px;cursor:pointer;font-weight:600;font-size:.95rem;margin:0;transition:all .12s;background:#fff
}
.choice label:hover{border-color:var(--navy-500)}
.choice input{accent-color:var(--accent);margin:0;flex:0 0 auto;width:17px;height:17px}
.choice input:checked+span{color:var(--navy)}
.choice label:has(input:checked){border-color:var(--accent);background:var(--accent-soft)}
.formnav{display:flex;gap:10px;margin-top:20px}
.formnav .btn{flex:1}
.err{color:#c0392b;font-size:.87rem;margin-top:8px;display:none}
.err.show{display:block}
.formfoot{font-size:.8rem;color:var(--muted);text-align:center;margin:14px 0 0;line-height:1.5}
.success{display:none;text-align:center;padding:24px 6px}
.oc-stap{font-size:1rem;margin:20px 0 8px}
.oc-stap:first-of-type{margin-top:4px}
.oc-plak{margin:0 0 12px;font-size:.93rem}
.oc-plak summary{cursor:pointer;color:var(--navy);font-weight:600;margin-bottom:10px}
input[type=file]{width:100%;padding:12px;border:1.5px dashed var(--line);border-radius:10px;background:#faf8f5;font-size:.93rem}
.oc-melding{font-size:.85rem;color:var(--muted);margin:6px 0 0}
.oc-rij{display:grid;grid-template-columns:minmax(0,1fr) 72px 104px 34px;gap:6px;align-items:center;margin-bottom:8px}
.oc-rij select,.oc-rij input{padding:9px 8px;font-size:.9rem}
.oc-rij .oc-weg{border:0;background:none;color:var(--muted);font-size:1.3rem;cursor:pointer;line-height:1}
.oc-kop{display:grid;grid-template-columns:minmax(0,1fr) 72px 104px 34px;gap:6px;font-size:.78rem;color:var(--muted);font-weight:600;margin-bottom:4px}
@media(max-width:560px){.oc-kop{display:none}.oc-rij{grid-template-columns:minmax(0,1fr) minmax(0,1fr) 28px;padding-bottom:10px;border-bottom:1px solid var(--line)}.oc-rij select{grid-column:1/-1}}
.oc-btw{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.88rem;margin:8px 0 4px}
.oc-btw label{white-space:nowrap}
.oc-btw label,.oc-lijst label{display:flex;gap:8px;align-items:center;font-weight:400;margin:0}
.oc-lijst{display:grid;gap:7px;font-size:.88rem}
.oc-lijst input,.oc-btw input{accent-color:var(--accent);width:16px;height:16px;flex:0 0 auto}
.oc-uitslag{margin-top:22px;border-top:2px solid var(--line);padding-top:6px}
.oc-uitslag h3{font-size:1.05rem;margin:18px 0 8px}
.oc-posten{list-style:none;padding:0;margin:0}
.oc-posten li{border-top:1px solid var(--line);padding:10px 0}
.oc-posten small{color:var(--muted);font-size:.84rem}
.oc-post{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;font-size:.93rem;margin-bottom:2px}
.oc-oordeel{display:inline-block;padding:2px 8px;border-radius:99px;font-size:.78rem;font-weight:700;white-space:nowrap}
.oc-laag{background:#e8f1fb;color:#1d4f86}.oc-binnen{background:#e7f5ec;color:#1e6b3a}.oc-hoog{background:#fdecea;color:#a3271b}.oc-geen{background:var(--line);color:var(--muted)}
.btn-link{border:0;background:none;color:var(--navy);font-weight:600;cursor:pointer;padding:4px 0;font-size:.9rem}
.success.show{display:block}
.success .big{width:58px;height:58px;border-radius:50%;background:#e7f7ef;color:var(--green);display:grid;place-items:center;font-size:1.6rem;margin:0 auto 16px}

/* ---------- Cards & grids ---------- */
.grid{display:grid;gap:20px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
@media(max-width:900px){.g3,.g4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.g2,.g3,.g4{grid-template-columns:1fr}}
@media(max-width:980px){.g2:has(> div > .formcard){grid-template-columns:minmax(0,1fr)}}

.card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:24px;transition:box-shadow .15s, transform .15s}
a.card:hover{text-decoration:none;box-shadow:var(--shadow);transform:translateY(-2px);border-color:#cfd9e4}
.card h3{margin-bottom:.35em;color:var(--ink)}
.card p{margin-bottom:.6em;font-size:.95rem;color:var(--body)}
.card .price{font-size:.88rem;color:var(--muted);font-weight:600}
.card .go{color:var(--accent-dark);font-weight:700;font-size:.92rem}
.ic{width:44px;height:44px;border-radius:11px;background:var(--accent-soft);color:var(--accent-dark);display:grid;place-items:center;margin-bottom:14px}
.ic svg{width:23px;height:23px}

.steps3{counter-reset:s;display:grid;grid-template-columns:repeat(3,1fr);gap:26px;list-style:none;padding:0}
@media(max-width:760px){.steps3{grid-template-columns:1fr;gap:18px}}
.steps3 li{counter-increment:s;position:relative;padding-left:56px;margin:0}
.steps3 li::before{
  content:counter(s);position:absolute;left:0;top:-2px;width:40px;height:40px;border-radius:50%;
  background:var(--navy);color:#fff;display:grid;place-items:center;font-weight:800;font-size:1.05rem
}
.steps3 h3{margin-bottom:.25em}
.steps3 p{font-size:.95rem;margin:0}

/* ---------- Plaatsenlijst ---------- */
.places{columns:4;column-gap:24px;list-style:none;padding:0;margin:0}
@media(max-width:900px){.places{columns:3}}
@media(max-width:620px){.places{columns:2}}
.places li{break-inside:avoid;margin-bottom:9px;font-size:.95rem}

.chips{display:flex;flex-wrap:wrap;gap:9px;padding:0;margin:0;list-style:none}
.chips li{margin:0}
.chips a{display:inline-block;padding:8px 15px;border-radius:99px;background:#fff;border:1px solid var(--line);font-size:.92rem;font-weight:600;color:var(--ink)}
.chips a:hover{border-color:var(--accent);color:var(--accent-dark);text-decoration:none}

/* ---------- Reviews ---------- */
.review{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:22px}
.review .stars{font-size:.95rem}
.review p{font-size:.96rem;margin:10px 0 14px;color:var(--ink)}
.review .who{font-size:.87rem;color:var(--muted);font-weight:600}

/* ---------- Tabel ---------- */
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius);background:#fff}
table{border-collapse:collapse;width:100%;font-size:.95rem}
th,td{text-align:left;padding:13px 16px;border-bottom:1px solid var(--line)}
th{background:var(--bg-soft);font-weight:700;color:var(--ink);white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
td.num{white-space:nowrap;font-variant-numeric:tabular-nums;font-weight:650;color:var(--ink)}
.deel{margin:28px 0;border:1px solid var(--line);border-radius:var(--radius);padding:14px 18px;background:#fff}.deel summary{cursor:pointer;font-weight:650}.deel textarea{width:100%;font:13px/1.4 ui-monospace,monospace;margin:8px 0;padding:8px;border:1px solid var(--line);border-radius:6px;resize:vertical}
@media(max-width:560px){td.num{white-space:normal}th,td{padding-left:10px;padding-right:10px}}

/* ---------- FAQ ---------- */
.faq details{border:1px solid var(--line);border-radius:var(--radius);background:#fff;margin-bottom:10px;overflow:hidden}
.faq summary{padding:16px 20px;cursor:pointer;font-weight:700;color:var(--ink);list-style:none;display:flex;justify-content:space-between;gap:16px;align-items:center}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:1.35rem;color:var(--accent-dark);font-weight:700;line-height:1}
.faq details[open] summary::after{content:"−"}
.faq details[open] summary{border-bottom:1px solid var(--line)}
.faq .a{padding:16px 20px;font-size:.97rem}
.faq .a p:last-child{margin-bottom:0}

/* ---------- Prose ---------- */
.prose h2{margin-top:2.2em}
.prose h2:first-child{margin-top:0}
.prose h3{margin-top:1.7em}
.prose ul li{margin-bottom:.55em}
.checklist{list-style:none;padding:0}
.checklist li{position:relative;padding-left:30px;margin-bottom:.7em}
.checklist li::before{content:"✓";position:absolute;left:0;top:0;color:var(--green);font-weight:800}

.callout{background:var(--accent-soft);border-left:4px solid var(--accent);border-radius:0 var(--radius) var(--radius) 0;padding:18px 22px;margin:26px 0}
.callout p:last-child{margin-bottom:0}
.callout strong{color:var(--ink)}

/* ---------- CTA blok ---------- */
.cta{background:linear-gradient(150deg,var(--navy),#241906);border-radius:var(--radius-lg);padding:44px;color:#c7d6e5;text-align:center}
.cta h2{color:#fff;margin-bottom:.4em}
.cta p{max-width:52ch;margin:0 auto 24px;color:#b8cadd}
@media(max-width:600px){.cta{padding:30px 22px}}

/* ---------- Breadcrumbs ---------- */
.crumbs{font-size:.85rem;color:var(--muted);padding-top:16px;display:flex;flex-wrap:wrap;align-items:baseline;row-gap:2px}
.crumbs a{color:var(--muted)}
.crumbs span{margin:0 7px;opacity:.5}

/* ---------- Footer ---------- */
.footer{background:var(--navy);color:#93a9c0;padding:56px 0 26px;font-size:.93rem;margin-top:0}
.footer h4,.footer .fh{color:#fff;font-size:.95rem;font-family:inherit;line-height:1.3;margin-bottom:14px;letter-spacing:.02em}
.footer a{color:#93a9c0}
.footer a:hover{color:#fff}
.footer-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:34px}
@media(max-width:820px){.footer-grid{grid-template-columns:1fr 1fr;gap:28px}}
@media(max-width:520px){.footer-grid{grid-template-columns:1fr}}
.footer ul{list-style:none;padding:0;margin:0}
.footer li{margin-bottom:8px}
.footer-bot{border-top:1px solid rgba(255,255,255,.11);margin-top:40px;padding-top:20px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;font-size:.85rem;color:#7b93ac}

/* ---------- Sticky mobiele CTA ---------- */
.sticky-cta{display:none}
@media(max-width:760px){
  .sticky-cta{
    display:block;position:fixed;left:0;right:0;bottom:0;z-index:70;
    background:rgba(255,255,255,.97);border-top:1px solid var(--line);padding:10px 16px;
    box-shadow:0 -4px 20px rgba(60,41,15,.10)
  }
  body{padding-bottom:76px}
}

.badge{display:inline-block;background:var(--accent-soft);color:#a35200;font-size:.78rem;font-weight:750;padding:5px 11px;border-radius:99px;letter-spacing:.03em;text-transform:uppercase;margin-bottom:14px}
.badge-dark{background:rgba(255,255,255,.12);color:#ffd9ab}

.stat{text-align:center}
.stat .n{font-size:2.1rem;font-weight:800;color:var(--ink);letter-spacing:-.03em;line-height:1.1}
.dark .stat .n{color:#fff}
.stat .l{font-size:.88rem;color:var(--muted)}
.dark .stat .l{color:#93a9c0}



/* =========================================================================
   Beeld, beweging en interactie — toegevoegd bij de visuele upgrade
   ========================================================================= */

/* ---------- Logo in de header ---------- */
.logo img{height:38px;width:auto;display:block}
.footer .logo img{height:40px}
@media(max-width:520px){.logo img{height:32px}}

/* ---------- Illustraties ---------- */
.illu{width:100%;height:auto;display:block;border-radius:var(--radius-lg)}
.foto{margin:24px 0 0}
.foto img{width:100%;border-radius:var(--radius-lg)}
.hero .foto{margin:0}
.hero .foto img{box-shadow:var(--shadow-lg)}
.card .foto{margin:-4px 0 14px}
.card .foto img{border-radius:10px}
.illu-card{background:var(--bg-soft);border-radius:var(--radius-lg);overflow:hidden;border:1px solid var(--line)}
.card .illu{border-radius:10px;margin:-4px 0 14px}
.hero .illu{border-radius:var(--radius-lg);box-shadow:var(--shadow-lg)}

/* ---------- Scroll-onthulling ---------- */
.reveal{opacity:0;transform:translateY(18px);transition:opacity .55s ease,transform .55s ease}
.reveal.in{opacity:1;transform:none}
.reveal-d1{transition-delay:.08s}.reveal-d2{transition-delay:.16s}.reveal-d3{transition-delay:.24s}

/* ---------- Voor/na-schuif ---------- */
.vn{position:relative;border-radius:var(--radius-lg);overflow:hidden;user-select:none;touch-action:none;border:1px solid var(--line);background:var(--bg-soft)}
.vn img,.vn svg{display:block;width:100%;height:auto}
.vn-na{position:absolute;inset:0;clip-path:inset(0 0 0 50%)}
.vn-greep{position:absolute;top:0;bottom:0;left:50%;width:3px;background:#fff;box-shadow:0 0 0 1px rgba(60,41,15,.25);cursor:ew-resize}
.vn-greep::after{content:"";position:absolute;top:50%;left:50%;width:42px;height:42px;margin:-21px 0 0 -21px;border-radius:50%;background:#fff;box-shadow:var(--shadow)}
.vn-greep::before{content:"◀ ▶";position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:2;font-size:.7rem;color:var(--accent-dark);letter-spacing:-1px}
.vn-label{position:absolute;bottom:14px;font-size:.78rem;font-weight:700;background:rgba(36,25,6,.82);color:#fff;padding:5px 12px;border-radius:99px;letter-spacing:.03em}
.vn-label.l{left:14px}.vn-label.r{right:14px}

/* ---------- Prijsindicator ---------- */
.calc{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:26px;box-shadow:var(--shadow)}
.calc h3{margin-bottom:18px}
.calc .rij{display:flex;align-items:center;gap:14px;margin-bottom:18px;flex-wrap:wrap}
.calc label{margin:0;flex:0 0 120px}
.calc select{flex:1;min-width:180px}
.calc input[type=range]{flex:1;min-width:160px;accent-color:var(--accent);height:6px}
.calc .waarde{font-weight:750;color:var(--ink);min-width:74px;text-align:right;font-variant-numeric:tabular-nums}
.calc-uit{background:var(--accent-soft);border-radius:var(--radius);padding:20px;text-align:center;margin-top:6px}
.calc-uit .bedrag{font-size:2rem;font-weight:800;color:var(--ink);letter-spacing:-.03em;line-height:1.15;font-variant-numeric:tabular-nums}
.calc-uit .sub{font-size:.87rem;color:var(--muted);margin-top:4px}

/* ---------- Kleine verfijningen ---------- */
a.card{position:relative;overflow:hidden}
a.card::after{content:"";position:absolute;left:0;right:0;bottom:0;height:3px;background:var(--accent);transform:scaleX(0);transform-origin:left;transition:transform .25s ease}
a.card:hover::after{transform:scaleX(1)}
.hero-in{position:relative}
.badge-live{display:inline-flex;align-items:center;gap:7px}
.badge-live i{width:7px;height:7px;border-radius:50%;background:#7ee2b0;display:inline-block;animation:pols 2.4s ease-in-out infinite}
@keyframes pols{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.45;transform:scale(.8)}}

@media(prefers-reduced-motion:reduce){
  .reveal{opacity:1;transform:none;transition:none}
  .badge-live i{animation:none}
  a.card::after{transition:none}
  html{scroll-behavior:auto}
}

.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap}

/* =========================================================================
   Visuele upgrade 2 — hero met foto, stappen, kaarten, tabellen, callouts
   (alleen aanvullingen en overrides; eerdere regels blijven staan)
   ========================================================================= */

/* ---------- Sectieritme ---------- */
@media(min-width:900px){.section{padding:84px 0}}
.section .center > h2::after{content:"";display:block;width:52px;height:4px;border-radius:4px;background:linear-gradient(90deg,var(--accent),#ffb15c);margin:16px auto 0}
.soft{background:linear-gradient(180deg,#faf6ee 0%,var(--bg-soft) 100%)}
.badge{box-shadow:inset 0 0 0 1px rgba(217,111,0,.18)}
.badge-dark{box-shadow:inset 0 0 0 1px rgba(255,217,171,.22)}

/* ---------- Hero met foto ---------- */
.hero-foto{background:#241906;isolation:isolate}
.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:62% 40%;z-index:-2;max-width:none}
.hero-foto::before{content:"";position:absolute;inset:0;z-index:-1;
  background:linear-gradient(100deg,rgba(28,19,5,.93) 0%,rgba(28,19,5,.80) 40%,rgba(28,19,5,.42) 68%,rgba(28,19,5,.28) 100%),
             linear-gradient(0deg,rgba(28,19,5,.55),transparent 40%)}
.hero-foto::after{z-index:-1}
.hero-foto .hero-in{z-index:auto;padding-top:84px;padding-bottom:96px}
.hero-foto h1{font-size:clamp(2rem,4.6vw,3.35rem);text-shadow:0 2px 24px rgba(0,0,0,.25)}
.hero-foto p.lead{color:#eadfcd}
.hero-foto .hero-usps li{color:#f6efe4}
.hero-foto .check{background:rgba(126,226,176,.16);box-shadow:inset 0 0 0 1px rgba(126,226,176,.35)}
.hero-tags{list-style:none;padding:0;margin:4px 0 0;display:flex;flex-wrap:wrap;gap:8px}
.hero-tags li{margin:0;font-size:.85rem;font-weight:600;color:#f3e7d6;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.16);padding:6px 12px;border-radius:99px;backdrop-filter:blur(4px)}
.hero .formcard{border-top:4px solid var(--accent);box-shadow:0 30px 70px rgba(0,0,0,.35),0 2px 6px rgba(0,0,0,.12)}
@media(max-width:920px){
  .hero-foto::before{background:linear-gradient(180deg,rgba(28,19,5,.80) 0%,rgba(28,19,5,.90) 45%,rgba(28,19,5,.97) 100%)}
  .hero-bg{height:620px;object-position:60% 30%}
  .hero-foto .hero-in{padding-top:44px;padding-bottom:52px}
}
@media(max-width:560px){.hero-tags{display:none}}

/* ---------- Vertrouwensbalk ---------- */
.trustbar{background:#fff;border-bottom:1px solid var(--line);box-shadow:0 6px 24px rgba(60,41,15,.05);position:relative;z-index:3}
.trustbar ul{list-style:none;margin:0;padding:18px 0;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.trustbar li{display:flex;align-items:center;gap:11px;margin:0;font-size:.93rem;color:var(--body);line-height:1.35}
.trustbar li strong{color:var(--ink)}
.trustbar svg{flex:0 0 38px;width:38px;height:38px;padding:9px;border-radius:10px;background:var(--accent-soft);color:var(--accent-dark)}
@media(max-width:900px){.trustbar ul{grid-template-columns:repeat(2,1fr);gap:14px 18px}}
@media(max-width:420px){.trustbar li{font-size:.86rem}.trustbar svg{flex-basis:34px;width:34px;height:34px;padding:8px}}

/* ---------- Zo werkt het ---------- */
.steps3{gap:22px;position:relative}
.steps3 li{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:30px 26px 26px;box-shadow:var(--shadow);position:relative;z-index:1}
.steps3 li::before{left:auto;right:22px;top:22px;width:34px;height:34px;font-size:.92rem;background:var(--accent-soft);color:var(--accent-dark);box-shadow:inset 0 0 0 1px rgba(217,111,0,.2)}
.step-ic{display:grid;place-items:center;width:58px;height:58px;border-radius:16px;margin-bottom:18px;color:#fff;
  background:linear-gradient(140deg,var(--accent) 0%,var(--accent-dark) 100%);box-shadow:0 10px 22px rgba(217,111,0,.28)}
.steps3 h3{font-size:1.2rem;margin-bottom:.4em}
@media(min-width:761px) and (max-width:980px){.steps3{gap:14px}.steps3 li{padding:24px 18px 20px}.steps3 h3{font-size:1.06rem}.step-ic{width:50px;height:50px;border-radius:14px}}
@media(min-width:761px){
  .steps3::before{content:"";position:absolute;top:58px;left:12%;right:12%;border-top:2px dashed #e7cba6;z-index:0}
}
/* zonder icoon (oudere markup) blijft de nummerbol links staan */
.steps3 li:not(:has(.step-ic)){padding-left:76px}
.steps3 li:not(:has(.step-ic))::before{left:24px;right:auto;top:28px}

/* ---------- Kaarten ---------- */
.card{border-radius:var(--radius-lg)}
.card .ic{width:52px;height:52px;border-radius:14px;background:linear-gradient(140deg,#fff1df,#ffe2bf);box-shadow:inset 0 0 0 1px rgba(217,111,0,.15)}
.card .ic svg{width:25px;height:25px}
.g4 > .card{box-shadow:0 1px 2px rgba(60,41,15,.04)}
.g4 > .card:hover{box-shadow:var(--shadow);border-color:#e3d3bb}
a.card{display:flex;flex-direction:column;box-shadow:0 1px 2px rgba(60,41,15,.05)}
a.card:hover{box-shadow:var(--shadow-lg);transform:translateY(-4px);border-color:#ecd9bd}
a.card > .foto{margin:-24px -24px 18px;overflow:hidden;border-radius:var(--radius-lg) var(--radius-lg) 0 0}
a.card > .foto img{border-radius:0;aspect-ratio:3/2;object-fit:cover;transition:transform .5s ease}
a.card:hover > .foto img{transform:scale(1.05)}
a.card > .illu{margin:-24px -24px 18px;width:calc(100% + 48px);max-width:none;border-radius:var(--radius-lg) var(--radius-lg) 0 0}
a.card .price{display:inline-block;align-self:flex-start;background:var(--bg-soft);border:1px solid var(--line);color:var(--ink);padding:4px 11px;border-radius:99px;font-size:.84rem;margin-top:auto}
a.card .go{display:inline-flex;align-items:center;gap:6px}
a.card .go{color:#a65300}
a.card:hover .go{color:#8a4500}
.footer-bot{color:#c2b39b}

/* ---------- Chips ---------- */
.chips a{transition:border-color .15s,color .15s,transform .15s,box-shadow .15s}
.chips a:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(60,41,15,.08)}

/* ---------- Tabellen ---------- */
.tablewrap{border-radius:var(--radius-lg);box-shadow:0 1px 2px rgba(60,41,15,.05),0 10px 30px rgba(60,41,15,.06)}
th{background:linear-gradient(180deg,#fbf3e6,#f7ecdb);font-size:.8rem;text-transform:uppercase;letter-spacing:.05em;color:#5a3d12;border-bottom:2px solid #efdcc0}
tbody tr:nth-child(even) td{background:#fdfbf7}
tbody tr{transition:background .15s}
tbody tr:hover td{background:#fff7ec}
td.num{color:#8a4700}
td:first-child{font-weight:600;color:var(--ink)}
td:first-child small{font-weight:400}

/* ---------- Callouts en lijsten ---------- */
.callout{position:relative;background:linear-gradient(135deg,#fff6ea 0%,#fff1df 100%);border:1px solid #f6d9b2;border-left:5px solid var(--accent);border-radius:var(--radius);padding:20px 24px 20px 64px;box-shadow:0 6px 20px rgba(217,111,0,.07)}
.callout::before{content:"i";font-family:Georgia,serif;font-style:italic;position:absolute;left:18px;top:18px;width:32px;height:32px;border-radius:50%;background:var(--accent-dark);color:#fff;display:grid;place-items:center;font-weight:800;font-size:.95rem}
.callout-prijs::before{content:"€";font-family:var(--font);font-style:normal}
@media(max-width:520px){.callout{padding:18px 18px 18px 56px}.callout::before{left:14px}}
.checklist li{padding-left:34px}
.checklist li::before{content:"";top:3px;width:22px;height:22px;border-radius:50%;background:#e4f4ec url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230f8a5f' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m6 12 4 4 8-9'/%3E%3C/svg%3E") center/13px no-repeat}
.prose ol{counter-reset:po;list-style:none;padding-left:0}
.prose ol > li{counter-increment:po;position:relative;padding-left:44px;margin-bottom:.9em}
.prose ol > li::before{content:counter(po);position:absolute;left:0;top:0;width:30px;height:30px;border-radius:50%;background:var(--accent-soft);color:var(--accent-dark);font-weight:800;font-size:.9rem;display:grid;place-items:center;box-shadow:inset 0 0 0 1px rgba(217,111,0,.22)}
.prose h2{position:relative;padding-left:18px}
.prose h2::before{content:"";position:absolute;left:0;top:.18em;bottom:.18em;width:5px;border-radius:5px;background:linear-gradient(180deg,var(--accent),#ffb15c)}
.prose .foto img{box-shadow:var(--shadow)}

/* ---------- FAQ ---------- */
.faq details{transition:border-color .15s,box-shadow .15s}
.faq details:hover{border-color:#e7cfae}
.faq details[open]{border-color:#efd3ad;box-shadow:0 6px 20px rgba(60,41,15,.06)}
.faq summary::after{width:28px;height:28px;flex:0 0 28px;border-radius:50%;background:var(--accent-soft);display:grid;place-items:center;font-size:1.1rem}

/* ---------- CTA en donkere secties ---------- */
.cta{position:relative;overflow:hidden;isolation:isolate;padding:56px 44px}
.cta::before{content:"";position:absolute;width:520px;height:520px;right:-160px;top:-260px;border-radius:50%;background:radial-gradient(closest-side,rgba(244,130,11,.32),transparent);z-index:-1}
.cta::after{content:"";position:absolute;width:420px;height:420px;left:-160px;bottom:-240px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,177,92,.16),transparent);z-index:-1}
.cta p{color:#e3d6c2}
.section.dark{position:relative;overflow:hidden;isolation:isolate}
.section.dark::before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(600px 300px at 85% 0%,rgba(244,130,11,.18),transparent),radial-gradient(500px 260px at 0% 100%,rgba(255,177,92,.10),transparent)}

/* ---------- Knoppen: subtiele glans ---------- */
.btn-primary{position:relative;overflow:hidden}
.btn-primary::after{content:"";position:absolute;top:0;bottom:0;left:-60%;width:40%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-18deg);transition:left .6s ease;pointer-events:none}
.btn-primary:hover::after{left:120%}
.btn:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid #ffb15c;outline-offset:2px}

/* ---------- Pagina-intro met formulier (diensten, plaatsen, checken) ---------- */
.section-sm:has(.g2 .formcard){background:radial-gradient(700px 440px at 88% 46%,#fff0dc 0%,rgba(255,240,220,0) 70%)}
.section-sm:has(.g2 .formcard) .g2 .foto img{aspect-ratio:16/9;object-fit:cover}
.g2 .formcard{border-top:4px solid var(--accent)}
@media(min-width:981px){.g2 > div:has(> .formcard){position:sticky;top:94px;align-self:start}}
input[type=file]::file-selector-button{font:inherit;font-weight:650;font-size:.88rem;border:0;border-radius:8px;background:var(--navy);color:#fff;padding:8px 14px;margin-right:12px;cursor:pointer}
input[type=file]::file-selector-button:hover{background:var(--navy-700)}

@media(prefers-reduced-motion:reduce){
  .btn-primary::after{display:none}
  a.card,a.card > .foto img,.chips a,tbody tr{transition:none}
  a.card:hover,a.card:hover > .foto img,.chips a:hover{transform:none}
}
'''

APP_JS = r'''/* Topschilder.nl — formulierlogica, tracking en Supabase-verzending. */
(function () {
  "use strict";

  var CFG = window.TS_CONFIG || {};

  /* --------------------------------------------- prijsoverzicht kopiëren */
  document.querySelectorAll("[data-kopieer]").forEach(function (knop) {
    knop.addEventListener("click", function () {
      var veld = knop.parentNode.querySelector("textarea");
      var klaar = function () { knop.textContent = "Gekopieerd"; setTimeout(function () { knop.textContent = "Kopieer code"; }, 2000); };
      if (navigator.clipboard) { navigator.clipboard.writeText(veld.value).then(klaar, function () { veld.select(); }); }
      else { veld.select(); document.execCommand("copy"); klaar(); }
    });
  });

  /* ---------------------------------------------------------------- menu */
  var burger = document.querySelector(".burger");
  if (burger) {
    burger.addEventListener("click", function () {
      var nav = document.querySelector(".nav");
      nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", nav.classList.contains("open"));
    });
  }

  /* ------------------------------------------------- attributie vasthouden */
  // Google Ads stuurt gclid mee. Die bewaren we 90 dagen zodat we later kunnen
  // zien welke advertentie een betaalde lead heeft opgeleverd.
  function captureAttribution() {
    var qs = new URLSearchParams(location.search);
    var keys = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "gbraid", "wbraid"];
    var found = {};
    var any = false;
    keys.forEach(function (k) {
      var v = qs.get(k);
      if (v) { found[k] = v; any = true; }
    });
    try {
      if (any) {
        found._ts = Date.now();
        found._landing = location.pathname;
        found._referrer = document.referrer || "";
        localStorage.setItem("ts_attr", JSON.stringify(found));
      }
    } catch (e) { /* private mode */ }
  }

  function getAttribution() {
    try {
      var raw = localStorage.getItem("ts_attr");
      if (!raw) return {};
      var a = JSON.parse(raw);
      if (Date.now() - (a._ts || 0) > 90 * 864e5) return {};
      return a;
    } catch (e) { return {}; }
  }
  captureAttribution();

  /* ------------------------------------------------------------- verzenden */
  function postToSupabase(table, payload) {
    if (CFG.DEMO_MODE || !CFG.SUPABASE_URL || !CFG.SUPABASE_ANON_KEY) {
      console.log("[Topschilder] DEMO_MODE — dit zou naar Supabase gaan:", table, payload);
      return Promise.resolve({ demo: true });
    }
    return fetch(CFG.SUPABASE_URL.replace(/\/$/, "") + "/rest/v1/" + table, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "apikey": CFG.SUPABASE_ANON_KEY,
        "Authorization": "Bearer " + CFG.SUPABASE_ANON_KEY,
        "Prefer": "return=minimal"
      },
      body: JSON.stringify(payload)
    }).then(function (r) {
      if (!r.ok) {
        return r.text().then(function (t) { throw new Error("Supabase " + r.status + ": " + t); });
      }
      return { ok: true };
    });
  }

  // De webhook krijgt een PLATTE payload met kant-en-klare velden, zodat je in
  // Make/Zapier alleen "onderwerp" en "samenvatting" hoeft te mappen en klaar bent.
  function buildWebhookPayload(table, d) {
    var soort = table === "leads" ? "Offerteaanvraag"
              : table === "schilders" ? "Schilder aanmelding"
              : table === "offerte_checks" ? "Offerte-check"
              : "Contactbericht";

    var kanaal = d.gclid ? "Google Ads"
               : d.utm_source ? d.utm_source
               : (d.referrer || "").indexOf("google") > -1 ? "Google organisch"
               : !d.referrer ? "Direct" : "Overig";

    var titel = table === "leads"
        ? (d.dienst || "Aanvraag") + " " + (d.plaats || "") + " — " + (d.telefoon || "")
        : table === "schilders"
        ? "Schilder: " + (d.bedrijfsnaam || "") + " (" + (d.werkgebied || "") + ")"
        : soort + " — " + (d.naam || "");

    if (d.opslag_mislukt) titel = "LET OP, niet opgeslagen: " + titel;

    var regels = [
      d.opslag_mislukt ? "LET OP: deze aanvraag is NIET in Supabase opgeslagen (" + (d.fout || "onbekende fout") + "). Zet hem handmatig over.\n" : "",
      soort,
      "",
      d.dienst      ? "Klus:        " + d.dienst : "",
      d.plaats      ? "Plaats:      " + d.plaats + (d.postcode ? " (" + d.postcode + ")" : "") : "",
      d.pandtype    ? "Pand:        " + d.pandtype : "",
      d.omvang      ? "Omvang:      " + d.omvang : "",
      d.planning    ? "Planning:    " + d.planning : "",
      "",
      d.naam        ? "Naam:        " + d.naam : "",
      d.telefoon    ? "Telefoon:    " + d.telefoon : "",
      d.email       ? "E-mail:      " + d.email : "",
      "",
      d.bedrijfsnaam   ? "Bedrijf:     " + d.bedrijfsnaam : "",
      d.contactpersoon ? "Contact:     " + d.contactpersoon : "",
      d.kvk            ? "KvK:         " + d.kvk : "",
      d.werkgebied     ? "Werkgebied:  " + d.werkgebied : "",
      d.diensten       ? "Diensten:    " + d.diensten : "",
      d.bedrag         ? "Offertebedrag: " + d.bedrag : "",
      "",
      d.omschrijving   ? "Omschrijving:\n" + d.omschrijving : "",
      d.offerte_tekst  ? "Offerte:\n" + d.offerte_tekst : "",
      d.bericht        ? "Bericht:\n" + d.bericht : "",
      "",
      "Kanaal:      " + kanaal,
      d.utm_campaign ? "Campagne:    " + d.utm_campaign : "",
      "Pagina:      https://topschilder.nl" + (d.bron_url || "")
    ];

    var plat = { soort: soort, tabel: table, onderwerp: titel, samenvatting: regels.filter(Boolean).join("\n"), kanaal: kanaal };
    Object.keys(d).forEach(function (k) { if (!(k in plat)) plat[k] = d[k]; });
    return plat;
  }

  function postToWebhook(table, data) {
    if (!CFG.WEBHOOK_URL) return Promise.resolve();
    return fetch(CFG.WEBHOOK_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(buildWebhookPayload(table, data))
    }).catch(function () { /* webhook mag nooit de bezoeker blokkeren */ });
  }

  function fireConversion(table) {
    // Meta: alleen het feit dat er een aanvraag is verstuurd, zonder gegevens.
    if (table === CFG.LEADS_TABLE && window.TS_TOESTEMMING && window.TS_TOESTEMMING.lead) {
      window.TS_TOESTEMMING.lead();
    }
    if (CFG.GOOGLE_ADS_ID && CFG.GOOGLE_ADS_LABEL && typeof window.gtag === "function") {
      window.gtag("event", "conversion", {
        send_to: CFG.GOOGLE_ADS_ID + "/" + CFG.GOOGLE_ADS_LABEL
      });
    }
  }

  /* ------------------------------------------------------ multi-step motor */
  function initWizard(form) {
    var steps = Array.prototype.slice.call(form.querySelectorAll(".step"));
    var bars = Array.prototype.slice.call(form.querySelectorAll(".steps div"));
    var idx = 0;
    if (!steps.length) return;

    function show(i) {
      idx = Math.max(0, Math.min(steps.length - 1, i));
      steps.forEach(function (s, n) { s.classList.toggle("active", n === idx); });
      bars.forEach(function (b, n) { b.classList.toggle("on", n <= idx); });
      var box = form.closest(".formcard") || form;
      var top = box.getBoundingClientRect().top + window.scrollY - 90;
      if (window.scrollY > top + 120) window.scrollTo({ top: top, behavior: "smooth" });
    }

    function validate(step) {
      var msg = step.querySelector(".err");
      var problem = "";

      // verplichte radiogroepen
      var groups = {};
      step.querySelectorAll('input[type=radio][data-required]').forEach(function (r) {
        groups[r.name] = groups[r.name] || false;
        if (r.checked) groups[r.name] = true;
      });
      Object.keys(groups).forEach(function (g) {
        if (!groups[g]) problem = problem || "Maak eerst een keuze om verder te gaan.";
      });

      // verplichte velden
      step.querySelectorAll("[required]").forEach(function (el) {
        if (el.type === "radio" || el.type === "checkbox") return;
        if (!el.value.trim()) {
          problem = problem || "Vul de gemarkeerde velden in.";
          el.style.borderColor = "#c0392b";
        } else {
          el.style.borderColor = "";
        }
        if (el.type === "email" && el.value && !/^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i.test(el.value)) {
          problem = "Controleer je e-mailadres.";
          el.style.borderColor = "#c0392b";
        }
        if (el.name === "postcode" && el.value) {
          var pc = el.value.replace(/\s+/g, "").toUpperCase();
          if (/^[1-9]\d{3}[A-Z]{2}$/.test(pc)) {
            el.value = pc.slice(0, 4) + " " + pc.slice(4);
          } else {
            problem = "Controleer je postcode (bijvoorbeeld 3892 AA).";
            el.style.borderColor = "#c0392b";
          }
        }
        if (el.type === "tel" && el.value && el.value.replace(/\D/g, "").length < 9) {
          problem = "Controleer je telefoonnummer.";
          el.style.borderColor = "#c0392b";
        }
      });

      if (msg) { msg.textContent = problem; msg.classList.toggle("show", !!problem); }
      return !problem;
    }

    form.querySelectorAll("[data-next]").forEach(function (b) {
      b.addEventListener("click", function () {
        if (validate(steps[idx])) show(idx + 1);
      });
    });
    form.querySelectorAll("[data-prev]").forEach(function (b) {
      b.addEventListener("click", function () { show(idx - 1); });
    });

    // Een keuze aanklikken springt meteen door — scheelt een klik per stap.
    form.querySelectorAll(".step .choice input[type=radio]").forEach(function (r) {
      r.addEventListener("change", function () {
        var step = r.closest(".step");
        if (step && step.dataset.autoadvance === "1") {
          setTimeout(function () { if (validate(step)) show(idx + 1); }, 160);
        }
      });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate(steps[idx])) return;

      var btn = form.querySelector("[data-submit]");
      var original = btn ? btn.textContent : "";
      if (btn) { btn.disabled = true; btn.textContent = "Versturen…"; }

      // Honeypot: alleen bots vullen dit veld. Doe alsof het gelukt is.
      var hp = form.querySelector('input[name=website]');
      if (hp && hp.value) {
        form.style.display = "none";
        var fake = (form.closest(".formcard") || form.parentNode).querySelector(".success");
        if (fake) fake.classList.add("show");
        return;
      }

      var fd = new FormData(form);
      var payload = {};
      fd.forEach(function (v, k) {
        if (k === "website") return;
        if (payload[k] !== undefined) {
          payload[k] = [].concat(payload[k], v).join(", ");
        } else {
          payload[k] = typeof v === "string" ? v.trim() : v;
        }
      });

      var attr = getAttribution();
      payload.bron_url = location.pathname;
      payload.utm_source = attr.utm_source || "";
      payload.utm_medium = attr.utm_medium || "";
      payload.utm_campaign = attr.utm_campaign || "";
      payload.gclid = attr.gclid || attr.gbraid || attr.wbraid || "";
      payload.referrer = attr._referrer || document.referrer || "";
      payload.status = "nieuw";

      var table = form.dataset.table || CFG.LEADS_TABLE;

      postToSupabase(table, payload)
        .then(function () { return postToWebhook(table, payload); })
        .then(function () {
          fireConversion(table);
          var card = form.closest(".formcard") || form.parentNode;
          form.style.display = "none";
          var ok = card.querySelector(".success");
          if (ok) {
            ok.classList.add("show");
            ok.scrollIntoView({ behavior: "smooth", block: "center" });
          }
        })
        .catch(function (err) {
          console.error(err);
          // Opslaan mislukt: stuur de aanvraag toch naar de webhook, zodat hij
          // niet verloren gaat. Eén keer per formulier, om dubbele mails te voorkomen.
          if (!form.dataset.noodverstuurd) {
            form.dataset.noodverstuurd = "1";
            postToWebhook(table, Object.assign({}, payload, { opslag_mislukt: "ja", fout: String(err).slice(0, 300) }));
          }
          if (btn) { btn.disabled = false; btn.textContent = original; }
          var msg = steps[idx].querySelector(".err");
          if (msg) {
            msg.innerHTML = 'Er ging iets mis bij het versturen. Probeer het nog eens, of neem <a href="/contact/">contact</a> met ons op.';
            msg.classList.add("show");
          }
        });
    });

    show(0);
  }

  document.querySelectorAll("form[data-wizard]").forEach(initWizard);


  /* ------------------------------------------------- scroll-onthulling */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var onthul = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    onthul.forEach(function (e) { e.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    onthul.forEach(function (e) { io.observe(e); });
  }

  /* ------------------------------------------------ voor/na-vergelijker */
  document.querySelectorAll("[data-vn]").forEach(function (vn) {
    var na = vn.querySelector(".vn-na");
    var greep = vn.querySelector(".vn-greep");
    if (!na || !greep) return;

    function zet(pct) {
      pct = Math.max(2, Math.min(98, pct));
      na.style.clipPath = "inset(0 0 0 " + pct + "%)";
      greep.style.left = pct + "%";
      greep.setAttribute("aria-valuenow", Math.round(pct));
    }
    function uitEvent(ev) {
      var r = vn.getBoundingClientRect();
      var x = (ev.touches ? ev.touches[0].clientX : ev.clientX) - r.left;
      zet((x / r.width) * 100);
    }
    var sleept = false;
    greep.addEventListener("pointerdown", function (e) {
      sleept = true; greep.setPointerCapture(e.pointerId); e.preventDefault();
    });
    greep.addEventListener("pointerup", function () { sleept = false; });
    greep.addEventListener("pointermove", function (e) { if (sleept) uitEvent(e); });
    vn.addEventListener("click", function (e) {
      if (e.target !== greep) uitEvent(e);
    });
    greep.addEventListener("keydown", function (e) {
      var nu = parseFloat(greep.style.left) || 50;
      if (e.key === "ArrowLeft") { zet(nu - 5); e.preventDefault(); }
      if (e.key === "ArrowRight") { zet(nu + 5); e.preventDefault(); }
    });
    zet(50);
  });

  /* ------------------------------------------------------ prijsindicator */
  var calc = document.querySelector("[data-calc]");
  if (calc) {
    var kies = calc.querySelector("select");
    var schuif = calc.querySelector("input[type=range]");
    var aantalUit = calc.querySelector("[data-aantal]");
    var bedragUit = calc.querySelector("[data-bedrag]");
    var subUit = calc.querySelector("[data-sub]");
    var link = calc.querySelector("[data-cta]");

    function euro(n) {
      return "€" + Math.round(n).toLocaleString("nl-NL");
    }
    function reken() {
      var o = kies.options[kies.selectedIndex];
      var van = parseFloat(o.dataset.van), tot = parseFloat(o.dataset.tot);
      var n = parseInt(schuif.value, 10);
      aantalUit.textContent = n + " " + (o.dataset.eenheid || "");
      bedragUit.textContent = euro(van * n) + " – " + euro(tot * n);
      subUit.textContent = o.dataset.uitleg || "";
      if (link) link.href = "/schilderwerk/" + o.value + "/";
    }
    kies.addEventListener("change", function () {
      var o = kies.options[kies.selectedIndex];
      schuif.min = o.dataset.min; schuif.max = o.dataset.max; schuif.value = o.dataset.start;
      reken();
    });
    schuif.addEventListener("input", reken);
    reken();
  }

  /* --------------------------------------------- pagina-context voorvullen */
  var ctx = document.body.dataset;
  var url = new URLSearchParams(location.search);
  var vDienst = url.get("dienst") || ctx.dienst;
  var vPlaats = url.get("plaats") || ctx.plaats;
  document.querySelectorAll("form[data-wizard]").forEach(function (f) {
    if (vDienst) {
      var d = [].slice.call(f.querySelectorAll("input[name=dienst]")).filter(function (i) { return i.value === vDienst; })[0];
      if (d) d.checked = true;
    }
    if (vPlaats) {
      var p = f.querySelector("input[name=plaats]");
      if (p && !p.value) p.value = vPlaats.slice(0, 60);
    }
    if (url.get("via") === "offertecheck") {
      var o = f.querySelector("textarea[name=omschrijving]");
      if (o && !o.value) o.value = "Ik heb al een offerte en zoek een vergelijkende offerte. ";
    }
  });
})();
'''

CONFIG_JS = r'''/* =========================================================================
   TOPSCHILDER — CONFIGURATIE
   Dit is het ENIGE bestand dat je hoeft aan te passen om leads te ontvangen.
   Vul hieronder je Supabase project-URL en anon key in.

   Waar vind je die?
   Supabase dashboard -> Project Settings -> API
     - "Project URL"              -> SUPABASE_URL
     - "anon" / "publishable" key -> SUPABASE_ANON_KEY

   Deze twee waarden zijn PUBLIEK en veilig om in je site te zetten,
   mits je supabase_schema.sql hebt uitgevoerd. Dat script zet Row Level
   Security aan met alleen INSERT-rechten: bezoekers kunnen een lead
   insturen, maar niemand kan leads uitlezen zonder service key.
   ========================================================================= */

window.TS_CONFIG = {
  SUPABASE_URL: "https://dijcpmqlzetxmnzonytw.supabase.co",
  SUPABASE_ANON_KEY: "sb_publishable_mWy5c8QjZM5ajlQjOD2FQg_9osH_bPD",

  LEADS_TABLE: "leads",
  SCHILDERS_TABLE: "schilders",

  // Staat op false: formulieren schrijven echt naar Supabase.
  // Zet tijdelijk op true als je iets wilt testen zonder data op te slaan.
  DEMO_MODE: false,

  // Make.com-scenario "Topschilder - nieuwe lead". Elke aanvraag gaat hier
  // ook naartoe, zodat je meteen een mail krijgt.
  WEBHOOK_URL: "https://hook.eu1.make.com/lg5v26xqlpa34gmkolamf1e0opd2uhy9",

  // Google Ads conversietracking. Vul in zodra je een conversieactie hebt
  // aangemaakt, dan telt elke ingestuurde offerteaanvraag als conversie.
  GOOGLE_ADS_ID: "",           // bv. "AW-123456789"
  GOOGLE_ADS_LABEL: "",        // bv. "AbC-D_efG-h12_34-567"

  // Meta-pixel. Laat leeg zolang er geen pixel is: dan laadt er niets van Meta
  // en verschijnt ook de cookiebanner niet. Vul het ID in (alleen cijfers, uit
  // Meta Events Manager), dan vraagt de site eerst toestemming en laadt de
  // pixel pas na "Accepteren".
  META_PIXEL_ID: ""            // bv. "123456789012345"
};
'''

FAVICON_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#3c290f"/>
<rect x="34" y="13" width="20" height="8" rx="4" fill="#f4820b"/>
<path d="M44 21v5a3 3 0 0 1-3 3h-6" stroke="#f4820b" stroke-width="3.4" fill="none" stroke-linecap="round"/>
<rect x="31" y="27" width="7" height="9" rx="2" fill="#f4820b"/>
<circle cx="23" cy="24" r="9" fill="#fff"/>
<path d="M13 24a10 10 0 0 1 20 0z" fill="#fff"/>
<path d="M15 38h16l4 14H11z" fill="#fff"/>
</svg>'''



STYLE_CSS += r'''
/* Werkgebiedkaart */
.kaart-knoppen{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}
.chip-k{font:inherit;font-size:.92rem;font-weight:600;padding:8px 14px;border-radius:999px;border:1px solid #d9c8a8;background:#fff;color:#3c290f;cursor:pointer}
.chip-k:hover{border-color:#f4820b}
.chip-k[aria-pressed="true"]{background:#3c290f;border-color:#3c290f;color:#fff}
.chip-k:focus-visible,.kaart-link:focus-visible{outline:3px solid #f4820b;outline-offset:2px}
.kaart-grid{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:20px;align-items:stretch}
.kaart svg{width:100%;height:auto;aspect-ratio:1000/944;display:block;border-radius:var(--radius-lg);border:1px solid #e6d9c2;background:#dfe9e8}
.kw{fill:#dfe9e8}.kl{fill:#f7f1e6;stroke:#ddcfb6;stroke-width:1.5}.ka{fill:#fbe9cf}
.kp{cursor:pointer;outline:none}.kh{fill:transparent}
.kd{fill:#f4820b;stroke:#3c290f;stroke-width:2.5;transition:fill .15s}
.kp text{fill:#3c290f;font-weight:700;paint-order:stroke;stroke:#fffaf2;stroke-width:5px;stroke-linejoin:round;pointer-events:none;display:none}
.kp.kg text,.kaart svg.zoom .kp text,.kp:hover text,.kp:focus text,.kp.aan text{display:block}
.kp:hover .kd,.kp:focus .kd,.kp.aan .kd{fill:#3c290f;stroke:#f4820b;stroke-width:4}
.kp[hidden]{display:none}
.kaart-info{background:#3c290f;color:#f7f1e6;border-radius:var(--radius-lg);padding:24px;display:flex;flex-direction:column;align-items:flex-start;gap:8px}
.kaart-prov{margin:0;color:#ffc98a;font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.kaart-naam{color:#fff;margin:0}.kaart-hook{color:#f7f1e6;margin:0 0 auto;font-size:.97rem}
.kaart-link{margin-top:14px}
.kaart-bron{font-size:.8rem;margin-top:10px}
@media(max-width:860px){.kaart-grid{grid-template-columns:minmax(0,1fr)}.kaart-hook{margin-bottom:0}}
'''

APP_JS += r'''
/* Werkgebiedkaart: inzoomen per provincie en plaatsinfo. Zonder JavaScript blijven alle links werken. */
(function () {
  var kaart = document.querySelector("[data-kaart]");
  if (!kaart) return;
  var svg = kaart.querySelector("svg");
  var B = +kaart.dataset.b, H = +kaart.dataset.h;
  var punten = [].slice.call(svg.querySelectorAll(".kp"));
  var knoppen = [].slice.call(kaart.querySelectorAll(".chip-k"));
  var naam = kaart.querySelector(".kaart-naam"), prov = kaart.querySelector(".kaart-prov");
  var hook = kaart.querySelector(".kaart-hook"), link = kaart.querySelector(".kaart-link");
  var vb = [0, 0, B, H], anim = 0;
  var rust = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  function maten() {
    var u = vb[2] / (svg.clientWidth || B);
    var groot = svg.clientWidth >= 500;
    punten.forEach(function (p) {
      p.querySelector(".kd").setAttribute("r", (groot ? 7 : 6) * u);
      p.querySelector(".kd").style.strokeWidth = 1.6 * u;
      p.querySelector(".kh").setAttribute("r", (groot ? 13 : 15) * u);
      var t = p.querySelector("text"), x = +p.dataset.x, y = +p.dataset.y;
      var kant = p.dataset.l;
      t.setAttribute("font-size", (groot ? 14 : 12) * u);
      t.style.strokeWidth = 3.2 * u + "px";
      t.setAttribute("x", kant === "t" || kant === "b" ? x : x + (kant === "l" ? -11 : 11) * u);
      t.setAttribute("y", kant === "b" ? y + 20 * u : kant === "t" ? y - 11 * u : y + 4.5 * u);
    });
  }
  function zet(v) { vb = v; svg.setAttribute("viewBox", v.join(" ")); maten(); }
  function naar(doel) {
    cancelAnimationFrame(anim);
    if (rust) return zet(doel);
    var van = vb.slice(), t0 = performance.now();
    (function stap(t) {
      var f = Math.min(1, (t - t0) / 420), e = 1 - Math.pow(1 - f, 3);
      zet(van.map(function (a, i) { return a + (doel[i] - a) * e; }));
      if (f < 1) anim = requestAnimationFrame(stap);
    })(t0);
  }
  function kader(lijst) {
    var xs = lijst.map(function (p) { return +p.dataset.x; }), ys = lijst.map(function (p) { return +p.dataset.y; });
    var x0 = Math.min.apply(0, xs), x1 = Math.max.apply(0, xs), y0 = Math.min.apply(0, ys), y1 = Math.max.apply(0, ys);
    var marge = svg.clientWidth < 500 ? 400 : 190;
    var w = Math.max(x1 - x0 + marge, 300), h = Math.max(y1 - y0 + 130, 300 * H / B);
    if (w / h > B / H) h = w * H / B; else w = h * B / H;
    return [(x0 + x1 - w) / 2, (y0 + y1 - h) / 2, w, h];
  }
  function toon(p) {
    punten.forEach(function (q) { q.classList.toggle("aan", q === p); });
    prov.textContent = p.dataset.prov;
    naam.textContent = "Schilder " + p.dataset.naam;
    hook.textContent = p.dataset.hook;
    link.textContent = "Bekijk " + p.dataset.naam + " →";
    link.href = p.getAttribute("href");
  }
  punten.forEach(function (p) {
    p.addEventListener("mouseenter", function () { toon(p); });
    p.addEventListener("focus", function () { toon(p); });
  });
  knoppen.forEach(function (k) {
    k.addEventListener("click", function () {
      var pv = k.dataset.prov;
      knoppen.forEach(function (x) { x.setAttribute("aria-pressed", x === k ? "true" : "false"); });
      var zicht = punten.filter(function (p) {
        var ja = !pv || p.dataset.prov === pv;
        if (ja) p.removeAttribute("hidden"); else p.setAttribute("hidden", "");
        return ja;
      });
      svg.classList.toggle("zoom", !!pv);
      naar(pv ? kader(zicht) : [0, 0, B, H]);
    });
  });
  window.addEventListener("resize", maten);
  maten();
})();
'''


APP_JS += r"""
/* ------------------------------------------------- offertecheck in de browser */
// Alles gebeurt hier in de browser: de offerte wordt nergens naartoe gestuurd.
(function () {
  var box = document.querySelector("[data-offertecheck]");
  if (!box) return;
  var BANDEN = window.TS_PRIJSBANDEN || {};
  var hand = document.querySelector("[data-handcheck]");
  document.querySelectorAll("[data-check-uit]").forEach(function (e) { e.hidden = true; });
  document.querySelectorAll("[data-check-aan]").forEach(function (e) { e.hidden = false; });
  box.hidden = false;
  if (hand) hand.hidden = true;
  box.querySelector("[data-oc-hand]").addEventListener("click", function () { if (hand) hand.hidden = false; });

  var rijen = box.querySelector("[data-oc-rijen]");
  var melding = box.querySelector("[data-oc-melding]");
  var fout = box.querySelector("[data-oc-fout]");
  var uitslag = box.querySelector("[data-oc-uitslag]");
  var plaats = box.querySelector("[name=plaats]");
  var opties = Object.keys(BANDEN).map(function (k) {
    return "<option value='" + k + "'>" + BANDEN[k].naam + " (" + BANDEN[k].eenheid + ")</option>";
  }).join("") + "<option value='anders'>Iets anders</option>";

  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function euro(n) { return "€" + Math.round(n).toLocaleString("nl-NL"); }
  function getal(t) {
    // Nederlandse notatie: 1.250,50 -> 1250.5
    t = String(t || "").replace(/[€\s]/g, "").replace(/,-$/, "");
    if (!t) return null;
    if (/,\d{1,2}$/.test(t)) t = t.replace(/\./g, "").replace(",", ".");
    else if (/^\d{1,3}(\.\d{3})+$/.test(t)) t = t.replace(/\./g, "");
    else t = t.replace(",", ".");
    var n = parseFloat(t);
    return isNaN(n) ? null : n;
  }

  function voegRijToe(p) {
    p = p || {};
    var r = document.createElement("div");
    r.className = "oc-rij";
    r.innerHTML = "<select aria-label='Soort werk'>" + opties + "</select>" +
      "<input type='text' inputmode='decimal' aria-label='Aantal' placeholder='Aantal'>" +
      "<input type='text' inputmode='decimal' aria-label='Bedrag' placeholder='€'>" +
      "<button type='button' class='oc-weg' aria-label='Post verwijderen'>×</button>";
    var v = r.querySelectorAll("select,input");
    v[0].value = p.categorie || "buitenkozijn";
    if (p.hoeveelheid != null) v[1].value = String(p.hoeveelheid).replace(".", ",");
    if (p.bedrag != null) v[2].value = String(p.bedrag).replace(".", ",");
    r.querySelector(".oc-weg").addEventListener("click", function () { r.remove(); });
    rijen.appendChild(r);
  }
  box.querySelector("[data-oc-plus]").addEventListener("click", function () { voegRijToe(); });
  voegRijToe();

  /* --------------------------- tekst uitlezen */
  var WOORDEN = [
    ["keukenfront", /keuken|front|kastdeur|\blade|\bladen/],
    ["trap", /\btrap/],
    ["houtrot_plek", /houtrot|inzetstuk|rotte|epoxy/],
    ["behang_m2", /behang/],
    ["steiger", /steiger|hoogwerker/],
    ["binnenkozijn", /binnenkozijn|deurkozijn|kozijnen? binnen|binnen.*kozijn/],
    ["buitenkozijn", /kozijn|raam|ramen|dakkapel|boeiboord/],
    ["deur", /\bdeur/],
    ["uurloon", /\bper uur|uurloon|uurtarief|regie|\buren\b/],
    ["muren_plafonds_m2", /muur|muren|wand|plafond|latex|m2|m²/]
  ];
  var EENHEID = /(\d+(?:[.,]\d+)?)\s*(?:x\s*)?(m2|m²|stuks?|st\.?|kozijnen|kozijn|deuren|deur|fronten|front|trappen|trap|uren|uur|plekken|plek|keer)\b/i;
  var BEDRAG = /(?:€|\beur\b)\s*(\d{1,3}(?:\.\d{3})*(?:,(?:\d{1,2}|-))?|\d+(?:,(?:\d{1,2}|-))?)|(\d{1,3}(?:\.\d{3})*,(?:\d{2}|-))(?!\s*%)/gi;
  var MERKEN = /sikkens|sigma|flexa|histor|wijzonol|trimetal|boss|drost|rambo|herbol|caparol|alpina|koopmans|osmo|ralston|jotun|tikkurila|levis|copagro/i;

  function leesTekst(tekst) {
    var t = tekst.toLowerCase();
    var posten = [], totaal = null;
    tekst.split(/\r?\n/).forEach(function (regel) {
      var r = regel.toLowerCase();
      var bedragen = [], m;
      BEDRAG.lastIndex = 0;
      while ((m = BEDRAG.exec(regel))) bedragen.push(getal(m[1] || m[2]));
      bedragen = bedragen.filter(function (b) { return b != null && b > 0; });
      if (!bedragen.length) return;
      var bedrag = bedragen[bedragen.length - 1];
      if (/totaal|te betalen|eindbedrag/.test(r) && !/sub/.test(r)) { totaal = bedrag; return; }
      if (/subtotaal|\bbtw\b|korting/.test(r)) return;
      var cat = "anders";
      for (var i = 0; i < WOORDEN.length; i++) { if (WOORDEN[i][1].test(r)) { cat = WOORDEN[i][0]; break; } }
      var q = null, e = r.match(EENHEID);
      if (e && !/keer/.test(e[2])) q = getal(e[1]);
      if (cat === "steiger" || cat === "trap") q = q || 1;
      posten.push({ categorie: cat, hoeveelheid: q, bedrag: bedrag });
    });
    var btw = /\b21\s*%/.test(t) ? 21 : /\b9\s*%/.test(t) ? 9 : null;
    var excl = /excl\.?\w*\s*(btw|b\.t\.w)/.test(t) ? true : /incl\.?\w*\s*(btw|b\.t\.w)/.test(t) ? false
      : /excl/.test(t) ? true : null;
    var lijst = {
      lagen: /\d\s*(x|keer|lagen|laags)\b|grondlaag|aflak|grondverf|voorlak/.test(t),
      merk: MERKEN.test(t),
      voorbereiding: /schuren|ontvet|plamu|kitten|reinig|afplak/.test(t),
      steiger: /steiger|hoogwerker|ladder/.test(t),
      houtrot: /houtrot/.test(t),
      garantie: /garantie/.test(t),
      btw: btw != null,
      planning: /planning|uitvoering|week|startdatum|oplever/.test(t)
    };
    return { posten: posten, totaal: totaal, btw: btw, excl: excl, lijst: lijst };
  }

  function vulIn(res) {
    rijen.innerHTML = "";
    res.posten.forEach(voegRijToe);
    if (!res.posten.length) voegRijToe();
    if (res.excl != null) box.querySelector("[name=btwsoort][value=" + (res.excl ? "excl" : "incl") + "]").checked = true;
    Object.keys(res.lijst).forEach(function (k) {
      var c = box.querySelector("[name=lijst][value=" + k + "]");
      if (c) c.checked = res.lijst[k];
    });
    box.dataset.totaal = res.totaal || "";
    box.dataset.btw = res.btw || "";
    melding.textContent = res.posten.length
      ? res.posten.length + " post(en) gevonden. Controleer ze hieronder: het uitlezen is automatisch en kan zich vergissen."
      : "We vonden geen posten met een bedrag. Vul ze hieronder zelf in.";
  }

  var pdfjs = null;
  function laadPdfjs() {
    if (pdfjs) return pdfjs;
    pdfjs = new Promise(function (ok, nee) {
      var s = document.createElement("script");
      s.src = "/assets/vendor/pdfjs/pdf.min.js";
      s.onload = function () {
        window.pdfjsLib.GlobalWorkerOptions.workerSrc = "/assets/vendor/pdfjs/pdf.worker.min.js";
        ok(window.pdfjsLib);
      };
      s.onerror = nee;
      document.head.appendChild(s);
    });
    return pdfjs;
  }
  function pdfNaarTekst(bestand) {
    return Promise.all([laadPdfjs(), bestand.arrayBuffer()]).then(function (x) {
      return x[0].getDocument({ data: x[1] }).promise;
    }).then(function (doc) {
      var paginas = [];
      for (var i = 1; i <= Math.min(doc.numPages, 10); i++) paginas.push(doc.getPage(i));
      return Promise.all(paginas.map(function (p) {
        return p.then(function (pg) { return pg.getTextContent(); }).then(function (c) {
          // Groepeer tekst per regel op basis van de hoogte op de pagina.
          var regels = {};
          c.items.forEach(function (it) {
            var y = Math.round(it.transform[5] / 3);
            (regels[y] = regels[y] || []).push(it);
          });
          return Object.keys(regels).sort(function (a, b) { return b - a; }).map(function (y) {
            return regels[y].sort(function (a, b) { return a.transform[4] - b.transform[4]; })
              .map(function (it) { return it.str; }).join(" ");
          }).join("\n");
        });
      }));
    }).then(function (p) { return p.join("\n"); });
  }

  box.querySelector("[data-oc-lees]").addEventListener("click", function () {
    var bestand = box.querySelector("[name=bestand]").files[0];
    var tekst = box.querySelector("[name=tekst]").value;
    melding.textContent = "";
    if (bestand) {
      if (bestand.type !== "application/pdf") { melding.textContent = "Alleen pdf-bestanden kunnen we uitlezen. Heb je een foto, vul de posten dan zelf in."; return; }
      melding.textContent = "Bezig met uitlezen…";
      pdfNaarTekst(bestand).then(function (t) {
        if (t.replace(/\s/g, "").length < 30) {
          melding.textContent = "Deze pdf bevat geen leesbare tekst, waarschijnlijk een scan. Vul de posten zelf in.";
          return;
        }
        vulIn(leesTekst(t));
      }).catch(function () { melding.textContent = "Deze pdf konden we niet openen. Vul de posten zelf in."; });
    } else if (tekst.trim().length > 10) {
      vulIn(leesTekst(tekst));
    } else {
      melding.textContent = "Kies een pdf of plak eerst de tekst van de offerte.";
    }
  });

  /* --------------------------- vergelijken */
  var CHECKS = {
    lagen: "Het aantal lagen (bijvoorbeeld een grondlaag en twee aflakken)",
    merk: "Het verfmerk en type verf",
    voorbereiding: "Wat er aan voorbereiding gebeurt (schuren, ontvetten, kitten)",
    steiger: "Of steiger of hoogwerker in de prijs zit",
    houtrot: "Hoe houtrot wordt afgerekend",
    garantie: "De garantie: hoe lang en waarop",
    btw: "Het btw-tarief per post",
    planning: "Wanneer het werk wordt uitgevoerd"
  };

  // Link naar het aanvraagformulier met klus en plaats alvast ingevuld.
  function aanvraagLink() {
    var cats = [].slice.call(rijen.querySelectorAll("select")).map(function (s) { return s.value; });
    var heeft = function (c) { return cats.indexOf(c) >= 0; };
    var dienst = (heeft("buitenkozijn") || heeft("steiger")) ? "Buitenschilderwerk"
      : heeft("houtrot_plek") ? "Houtrot reparatie"
      : (heeft("keukenfront") && cats.length === 1) ? "Spuitwerk"
      : (heeft("behang_m2") && cats.length === 1) ? "Behangen"
      : "Binnenschilderwerk";
    var naam = plaats.value && plaats.value !== "1" ? plaats.options[plaats.selectedIndex].text : "";
    return "/offerte-aanvragen/?dienst=" + encodeURIComponent(dienst) +
      (naam ? "&plaats=" + encodeURIComponent(naam) : "") + "&via=offertecheck#offerte";
  }

  box.querySelector("[data-oc-check]").addEventListener("click", function () {
    fout.classList.remove("show");
    if (!plaats.value) { fout.textContent = "Kies je plaats."; fout.classList.add("show"); return; }
    var index = parseFloat(plaats.value) || 1;
    var excl = box.querySelector("[name=btwsoort]:checked").value === "excl";
    var btw = (parseFloat(box.dataset.btw) || 9) / 100;
    var LABEL = { laag: "Onder de richtprijs", binnen: "Binnen de richtprijs", hoog: "Boven de richtprijs" };
    var tel = { laag: 0, binnen: 0, hoog: 0 }, som = 0, html = "";

    [].slice.call(rijen.children).forEach(function (r) {
      var v = r.querySelectorAll("select,input");
      var cat = v[0].value, q = getal(v[1].value), bedrag = getal(v[2].value);
      if (bedrag == null) return;
      som += bedrag;
      var b = BANDEN[cat];
      var naam = b ? b.naam : "Overig";
      if (!b || !q || q <= 0) {
        html += "<li><div class='oc-post'><strong>" + esc(naam) + "</strong><span class='oc-oordeel oc-geen'>Niet te vergelijken</span></div><small>" +
          euro(bedrag) + (excl ? " excl. btw" : "") + (b ? " · vul het aantal in om te vergelijken" : "") + "</small></li>";
        return;
      }
      // Banden zijn incl. btw, behalve uurloon. Reken het bedrag om naar dezelfde basis.
      var vgl = b.excl_btw ? (excl ? bedrag : bedrag / (1 + btw)) : (excl ? bedrag * (1 + btw) : bedrag);
      var van = b.van * index * q, tot = b.tot * index * q;
      var o = vgl < van * 0.9 ? "laag" : vgl > tot * 1.1 ? "hoog" : "binnen";
      tel[o]++;
      html += "<li><div class='oc-post'><strong>" + esc(naam) + "</strong><span class='oc-oordeel oc-" + o + "'>" + LABEL[o] + "</span></div><small>" +
        esc(String(q).replace(".", ",")) + " × " + esc(b.eenheid.replace("per ", "")) + " · offerte " + euro(vgl) + (b.excl_btw ? " excl." : " incl.") + " btw" +
        " · richtprijs " + euro(van) + " – " + euro(tot) + "</small></li>";
    });
    if (!html) { fout.textContent = "Vul minstens één post met een bedrag in."; fout.classList.add("show"); return; }

    var buiten = [].slice.call(rijen.querySelectorAll("select")).some(function (sel) {
      return ["buitenkozijn", "houtrot_plek", "steiger"].indexOf(sel.value) >= 0;
    });
    var mist = [].slice.call(box.querySelectorAll("[name=lijst]")).filter(function (c) {
      return !c.checked && (buiten || (c.value !== "steiger" && c.value !== "houtrot"));
    })
      .map(function (c) { return CHECKS[c.value]; });
    var kop = tel.hoog > 0 ? "Een deel van je offerte ligt boven de richtprijs"
      : tel.laag > 0 ? "Je offerte ligt deels onder de richtprijs"
      : tel.binnen > 0 ? "Je offerte ligt binnen de richtprijzen" : "We konden de posten niet vergelijken";
    var uitleg = tel.hoog > 0 ? "Dat kan kloppen, bijvoorbeeld bij slecht hout of veel voorwerk. Vraag de schilder waar het verschil in zit, of leg er een tweede offerte naast."
      : tel.laag > 0 ? "Een lage prijs is niet altijd slecht. Check wel of alles erin zit, zoals het aantal lagen, de steiger en houtrot."
      : tel.binnen > 0 ? "Check hieronder of er niets ontbreekt. Dan weet je zeker dat je appels met appels vergelijkt."
      : "Vul bij de posten het aantal in, dan kunnen we ze naast de richtprijs leggen.";
    var totaal = parseFloat(box.dataset.totaal);

    uitslag.innerHTML = "<h2>" + kop + "</h2><p>" + uitleg + "</p>" +
      "<p><strong>Opgeteld:</strong> " + euro(som) + (excl ? " excl. btw" : " incl. btw") +
      (totaal && Math.abs(totaal - som) > 1 && Math.abs(totaal - som * (1 + btw)) > 1 && Math.abs(totaal * (1 + btw) - som) > 1 ? " <small>(het totaal op de offerte is " + euro(totaal) + ")</small>" : "") + "</p>" +
      "<h3>Per post</h3><ul class='oc-posten'>" + html + "</ul>" +
      "<h3>" + (mist.length ? "Vraag de schilder hiernaar" : "Alles staat erin") + "</h3>" +
      (mist.length ? "<ul>" + mist.map(function (m) { return "<li>" + m + "</li>"; }).join("") + "</ul>" : "<p>De belangrijkste punten staan in de offerte. Goed teken.</p>") +
      "<p class='formfoot'>Vergeleken met onze richtprijzen voor jouw regio. Dit is een indicatie, geen oordeel over het bedrijf.</p>" +
      "<div class='formnav'><a class='btn btn-primary' href='" + aanvraagLink() + "'>" +
      (tel.hoog > 0 ? "Leg er een tweede offerte naast" : "Vraag vergelijkende offertes aan") + "</a></div>";
    uitslag.hidden = false;
    uitslag.scrollIntoView({ behavior: "smooth", block: "start" });
  });
})();
"""

APP_JS += r"""
/* ------------------------------------------------- verfcalculator */
(function () {
  var box = document.querySelector("[data-verfcalc]");
  if (!box) return;
  var uit = box.querySelector("[data-vc-uitkomst]");
  function n(id) { var v = parseFloat(String(box.querySelector(id).value).replace(",", ".")); return isNaN(v) || v < 0 ? 0 : v; }
  function blikken(l) {
    // Kleinste combinatie van gangbare blikmaten die genoeg is.
    var maten = [10, 5, 2.5, 1], rest = l, out = [];
    maten.forEach(function (m) { while (rest >= m * 0.9 && m >= 2.5) { out.push(m); rest -= m; } });
    while (rest > 0.05) { out.push(rest > 1 ? 2.5 : 1); rest -= rest > 1 ? 2.5 : 1; }
    var tel = {};
    out.forEach(function (m) { tel[m] = (tel[m] || 0) + 1; });
    return Object.keys(tel).sort(function (a, b) { return b - a; }).map(function (m) {
      return tel[m] + " × " + String(m).replace(".", ",") + " liter";
    }).join(" + ");
  }
  function reken() {
    var l = n("#vc-l"), b = n("#vc-b"), h = n("#vc-h"), r = n("#vc-r");
    var wat = box.querySelector("#vc-wat").value, lagen = n("#vc-lagen"), ond = n("#vc-ond") || 1;
    var muur = Math.max(0, 2 * (l + b) * h - r * 1.8), plafond = l * b;
    var m2 = 0, liters = 0;
    if (wat !== "plafond") { m2 += muur; liters += muur / 9 * lagen * ond; }
    if (wat !== "muren") { m2 += plafond; liters += plafond / 8 * lagen * ond; }
    if (!m2) { uit.innerHTML = "<p>Vul de maten in.</p>"; return; }
    var afgerond = Math.ceil(liters * 2) / 2;
    uit.innerHTML = "<p><strong>Je hebt ongeveer " + String(afgerond).replace(".", ",") + " liter nodig</strong> voor " +
      Math.round(m2) + " m² en " + lagen + (lagen === 1 ? " laag" : " lagen") + ".</p>" +
      "<p style='margin-top:6px;font-size:.9rem'>Bijvoorbeeld: " + blikken(afgerond) + ". Gerekend met 9 m² per liter voor muren en 8 m² voor plafonds; kijk op het blik voor het precieze rendement.</p>";
  }
  box.addEventListener("input", reken);
  box.addEventListener("change", reken);
  reken();
})();
"""


STYLE_CSS += r'''
/* Cookiebanner: onderin, blokkeert de pagina niet */
.cookiebanner{position:fixed;left:16px;right:16px;bottom:16px;z-index:90;max-width:560px;margin-left:auto;background:#fff;color:var(--body);border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:var(--shadow-lg);padding:18px 20px}
.cookiebanner[hidden]{display:none}
.cookiebanner h2{font-size:1.05rem;margin:0 0 6px}
.cookiebanner p{margin:0 0 14px;font-size:.93rem;line-height:1.5}
.cookiebanner .knoppen{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.cookiebanner button{font:inherit;font-weight:700;font-size:.95rem;padding:11px 14px;border-radius:10px;border:2px solid var(--navy);background:#fff;color:var(--navy);cursor:pointer}
.cookiebanner button:hover{background:var(--navy);color:#fff}
.cookiebanner button:focus-visible,.cookie-instellingen:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.cookie-instellingen{background:none;border:0;padding:0;font:inherit;color:inherit;cursor:pointer;text-decoration:none}
.cookie-instellingen:hover{text-decoration:underline}
@media(max-width:760px){.cookiebanner{left:10px;right:10px;bottom:10px;padding:16px}}
'''

TOESTEMMING_JS = r'''/* Topschilder.nl: cookietoestemming en Meta-pixel.
   Zonder "Accepteren" wordt er niets van Meta geladen. De keuze staat alleen
   in de lokale opslag van deze browser (sleutel ts_toestemming). */
(function () {
  var CFG = window.TS_CONFIG || {};
  var ID = String(CFG.META_PIXEL_ID || "").replace(/\D/g, "");
  var SLEUTEL = "ts_toestemming";
  var GELDIG = 365 * 864e5;
  var geladen = false;

  function lees() {
    try {
      var k = JSON.parse(localStorage.getItem(SLEUTEL) || "null");
      if (k && (k.keuze === "ja" || k.keuze === "nee") && Date.now() - k.t < GELDIG) return k.keuze;
    } catch (e) {}
    return null;
  }
  function bewaar(keuze) {
    try { localStorage.setItem(SLEUTEL, JSON.stringify({ keuze: keuze, t: Date.now() })); } catch (e) {}
  }
  function wisMetaCookies() {
    var host = location.hostname.replace(/^www\./, "");
    ["_fbp", "_fbc"].forEach(function (n) {
      ["", "; domain=" + host, "; domain=." + host].forEach(function (d) {
        document.cookie = n + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + d;
      });
    });
  }
  function laadPixel() {
    if (geladen || !ID) return;
    geladen = true;
    /* Standaardcode van Meta, zonder automatische gebeurtenissen of
       automatische koppeling van formuliergegevens. */
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0"; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
    window.fbq("set", "autoConfig", false, ID);
    window.fbq("init", ID);
    window.fbq("track", "PageView");
  }

  var banner = null;
  function maakBanner() {
    if (banner) return banner;
    banner = document.createElement("section");
    banner.className = "cookiebanner";
    banner.setAttribute("aria-label", "Cookietoestemming");
    banner.hidden = true;
    banner.innerHTML =
      '<h2>Mogen we advertenties meten?</h2>' +
      '<p>Met jouw toestemming plaatst Meta (Facebook en Instagram) cookies om te meten welke advertenties bezoekers en aanvragen opleveren. ' +
      'Weigeren heeft geen invloed op de site of het aanvraagformulier. Lees het <a href="/cookies/">cookiebeleid</a>.</p>' +
      '<div class="knoppen"><button type="button" data-keuze="nee">Weigeren</button><button type="button" data-keuze="ja">Accepteren</button></div>';
    banner.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-keuze]");
      if (!b) return;
      kies(b.getAttribute("data-keuze"));
    });
    document.body.appendChild(banner);
    return banner;
  }
  function toonBanner() { maakBanner().hidden = false; }
  function verbergBanner() { if (banner) banner.hidden = true; }

  function kies(keuze) {
    var was = lees();
    bewaar(keuze);
    verbergBanner();
    if (keuze === "ja") {
      laadPixel();
    } else {
      wisMetaCookies();
      // Was de pixel al geladen, dan stopt die pas na herladen.
      if (was === "ja" && geladen) location.reload();
    }
  }

  window.TS_TOESTEMMING = {
    keuze: lees,
    open: toonBanner,
    lead: function () {
      if (lees() === "ja" && geladen && window.fbq) window.fbq("track", "Lead");
    }
  };

  function start() {
    document.querySelectorAll(".cookie-instellingen").forEach(function (k) {
      k.addEventListener("click", function () { toonBanner(); var b = banner.querySelector("button"); if (b) b.focus(); });
    });
    var k = lees();
    if (k === "ja") laadPixel();
    else if (k === null && ID) toonBanner();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
'''


# =========================================================================
# Visuele ronde 2 — tools, prijskaart, CTA halverwege, afwerking
# (aanvullingen aan het eind, zodat samenvoegen met andere branches makkelijk blijft)
# =========================================================================

STYLE_CSS += r'''
/* ---------- Tools-sectie (home en /tools/) ---------- */
.tools-sectie{background:linear-gradient(160deg,#3c290f 0%,#241906 70%);color:#e3d6c2;position:relative;overflow:hidden;isolation:isolate}
.tools-sectie::before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(640px 320px at 12% 0%,rgba(244,130,11,.22),transparent),radial-gradient(560px 300px at 100% 100%,rgba(255,177,92,.12),transparent)}
.tools-sectie h2{color:#fff}
.tools-sectie .lead{color:#e3d6c2}
.tools-sectie .center > h2::after{background:linear-gradient(90deg,var(--accent),#ffcf94)}
.tools-pagina{padding-top:56px}
.tools-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:22px}
.tool-kaart{flex:1 1 300px;max-width:372px;display:flex;flex-direction:column;background:#fff;border-radius:var(--radius-lg);overflow:hidden;color:var(--body);box-shadow:0 1px 2px rgba(0,0,0,.2),0 18px 40px rgba(0,0,0,.25);transition:transform .25s ease,box-shadow .25s ease}
.tool-kaart:hover{text-decoration:none;transform:translateY(-6px);box-shadow:0 2px 4px rgba(0,0,0,.2),0 28px 60px rgba(0,0,0,.35)}
.tool-beeld{position:relative;height:150px;display:grid;place-items:center;background:linear-gradient(140deg,#fff6ea,#ffe7c8)}
.tool-kleuren .tool-beeld{background:linear-gradient(140deg,#eef4ef,#dfeadf)}
.tool-onderhoud .tool-beeld{background:linear-gradient(140deg,#f7f3ea,#ece3d1)}
.tool-weer .tool-beeld{background:linear-gradient(140deg,#eaf3fb,#d8e8f6)}
.tool-inspiratie .tool-beeld{background:linear-gradient(140deg,#f8efe9,#f0dfd3)}
.tool-beeld svg{width:170px;height:auto;transition:transform .35s ease}
.tool-kaart:hover .tool-beeld svg{transform:scale(1.06) rotate(-1.5deg)}
.tool-label{position:absolute;top:12px;left:12px;font-size:.74rem;font-weight:750;letter-spacing:.04em;text-transform:uppercase;color:#7a3f00;background:rgba(255,255,255,.85);padding:4px 10px;border-radius:99px}
.tool-tekst{padding:22px 24px 24px;display:flex;flex-direction:column;flex:1}
.tool-tekst h2,.tool-tekst h3{font-size:1.25rem;margin:0 0 .2em;color:var(--ink)}
.tool-kort{font-weight:650;color:var(--ink);margin:0 0 .5em}
.tool-tekst p{font-size:.95rem}
.tool-knop{margin-top:auto;display:inline-flex;align-items:center;gap:8px;align-self:flex-start;font-weight:750;color:#fff;background:var(--navy);padding:10px 16px;border-radius:10px;transition:background .2s}
.tool-knop span{transition:transform .2s}
.tool-kaart:hover .tool-knop{background:var(--navy-700)}
.tool-kaart:hover .tool-knop span{transform:translateX(4px)}
.tools-alle{color:#ffd9ab;font-weight:700}
.tool-hero{background:radial-gradient(700px 360px at 85% 55%,#fff0dc 0%,rgba(255,240,220,0) 70%)}
.tools-pagina{background:linear-gradient(180deg,#faf6ee,#f6efe2)}
.tools-pagina::before{display:none}
.tools-pagina .tool-kaart{box-shadow:var(--shadow);border:1px solid var(--line)}
.tools-pagina .tool-kaart:hover{box-shadow:var(--shadow-lg)}

/* ---------- Kostenpagina: bovenkant met prijskaart ---------- */
.kosten-kop{background:radial-gradient(700px 440px at 88% 50%,#fff0dc 0%,rgba(255,240,220,0) 70%)}
.kosten-kop-in{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.8fr);gap:52px;align-items:center}
.kosten-kop-in h1{font-size:clamp(1.9rem,4vw,2.8rem)}
@media(max-width:900px){.kosten-kop-in{grid-template-columns:minmax(0,1fr);gap:26px}}
.kosten-inhoud{padding-top:12px}
.kop-feiten{list-style:none;padding:0;margin:4px 0 0;display:flex;flex-wrap:wrap;gap:8px}
.kop-feiten li{margin:0;font-size:.86rem;font-weight:650;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:99px;padding:6px 12px 6px 30px;position:relative}
.kop-feiten li::before{content:"";position:absolute;left:10px;top:50%;width:14px;height:14px;margin-top:-7px;border-radius:50%;background:#e4f4ec url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230f8a5f' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m6 12 4 4 8-9'/%3E%3C/svg%3E") center/9px no-repeat}
.prijskaart{background:#fff;border-radius:var(--radius-lg);box-shadow:var(--shadow-lg);border:1px solid var(--line);border-top:4px solid var(--accent);overflow:hidden}
.prijskaart > .foto{margin:0}
.prijskaart > .foto img{border-radius:0;aspect-ratio:16/8;object-fit:cover}
.prijskaart-in{padding:22px 24px 24px}
.prijskaart-kop{font-size:.78rem;font-weight:750;letter-spacing:.06em;text-transform:uppercase;color:#a35200;margin:0 0 2px}
.prijskaart-bedrag{font-size:clamp(2rem,4vw,2.6rem);font-weight:800;color:var(--ink);letter-spacing:-.03em;line-height:1.1;margin:0;font-variant-numeric:tabular-nums}
.prijskaart-bedrag span{color:var(--accent-dark);font-weight:700}
.prijskaart-eenheid{font-weight:650;color:var(--ink);margin:2px 0 8px}
.prijskaart-noot{font-size:.88rem;color:var(--muted);margin:0 0 16px;line-height:1.5}
.prijskaart-link{display:block;text-align:center;margin-top:12px;font-weight:650;font-size:.93rem}
@media(max-width:900px){.prijskaart > .foto{display:none}.kosten-kop .lead{font-size:1.05rem}}

/* ---------- Dienstkaarten compact op mobiel ---------- */
@media(max-width:600px){
  .grid > a.card:has(> .foto){display:grid;grid-template-columns:92px minmax(0,1fr);column-gap:14px;padding:12px 14px 12px 12px;align-items:start}
  .grid > a.card > .foto{grid-row:1/span 4;margin:0;border-radius:12px;height:100%;align-self:stretch}
  .grid > a.card > .foto img{aspect-ratio:auto;height:100%;min-height:124px;border-radius:12px}
  .grid > a.card:has(> .foto) h3{font-size:1.04rem;margin:2px 0 .15em}
  .grid > a.card:has(> .foto) p{font-size:.87rem;margin-bottom:.45em;line-height:1.45}
  .grid > a.card:has(> .foto) .price{font-size:.76rem;padding:3px 9px}
  .grid > a.card:has(> .foto) p:last-child{margin:6px 0 0!important}
  .grid > a.card:has(> .foto) .go{font-size:.82rem;white-space:nowrap}
  .g4 > .card:has(> .ic){display:grid;grid-template-columns:44px minmax(0,1fr);column-gap:14px;padding:18px}
  .g4 > .card > .ic{grid-row:1/span 2;width:44px;height:44px;margin:0}
  .g4 > .card:has(> .ic) h3{font-size:1.05rem;margin:2px 0 .25em}
  .g4 > .card:has(> .ic) p{margin:0;font-size:.9rem}
  .g4:has(> .card > .ic){gap:12px}
  .steps3{gap:12px}
  .steps3 li:has(.step-ic){display:grid;grid-template-columns:48px minmax(0,1fr);column-gap:14px;padding:18px 52px 18px 18px}
  .steps3 li > .step-ic{grid-row:1/span 2;width:48px;height:48px;border-radius:14px;margin:0}
  .steps3 li > .step-ic svg{width:22px;height:22px}
  .steps3 li:has(.step-ic) h3{font-size:1.05rem;margin:2px 0 .2em}
  .steps3 li::before{top:16px;right:14px;width:28px;height:28px;font-size:.82rem}
  .grid.g3:has(> a.card > .foto){gap:12px}
}

@media(max-width:980px){.plaats-foto{display:none}}

/* ---------- CTA halverwege ---------- */
.cta-midden{display:flex;align-items:center;gap:22px;margin:34px 0;padding:22px 26px;border-radius:var(--radius-lg);background:linear-gradient(135deg,#3c290f,#241906);color:#e3d6c2;position:relative;overflow:hidden;isolation:isolate;box-shadow:0 14px 34px rgba(60,41,15,.18)}
.cta-midden::before{content:"";position:absolute;width:300px;height:300px;right:-90px;top:-150px;border-radius:50%;background:radial-gradient(closest-side,rgba(244,130,11,.35),transparent);z-index:-1}
.cta-midden-tekst{flex:1;min-width:0}
.cta-midden-titel{color:#fff;font-weight:750;font-size:1.12rem;margin:0 0 .2em;letter-spacing:-.01em}
.cta-midden p:not(.cta-midden-titel){margin:0;font-size:.95rem}
.cta-midden .btn{flex:0 0 auto;white-space:nowrap}
@media(max-width:620px){.cta-midden{flex-direction:column;align-items:stretch;padding:20px}.cta-midden .btn{white-space:normal}}

/* ---------- FAQ ---------- */
.faq summary{transition:color .15s,background .15s}
.faq summary:hover{color:#8a4500;background:#fffaf3}
.faq details[open]{border-left:4px solid var(--accent)}
.faq details[open] .a{animation:fade .25s ease}
.faq summary::after{transition:transform .25s ease,background .2s}
.faq details[open] summary::after{transform:rotate(180deg);background:var(--accent);color:#fff}

/* ---------- Formulier: afwerking ---------- */
.steps div{transition:background .35s ease}
.choice label{transition:border-color .15s,background .15s,box-shadow .15s,transform .1s}
.choice label:active{transform:scale(.985)}
.choice label:has(input:checked){box-shadow:0 0 0 3px rgba(244,130,11,.15)}
.choice label:has(input:focus-visible){outline:3px solid #ffb15c;outline-offset:2px}
.choice input:checked{animation:vink .25s ease}
@keyframes vink{0%{transform:scale(.6)}70%{transform:scale(1.15)}100%{transform:scale(1)}}
input:hover:not(:focus),select:hover:not(:focus),textarea:hover:not(:focus){border-color:#d8c9b0}
.formcard .formnav .btn-ghost:hover{background:var(--bg-soft)}

/* ---------- Header en mobiele sticky CTA ---------- */
.header{transition:box-shadow .2s ease}
.header.is-gescrold{box-shadow:0 6px 20px rgba(60,41,15,.08)}
.nav a:not(.btn){position:relative}
.nav a:not(.btn)::after{content:"";position:absolute;left:13px;right:13px;bottom:4px;height:2px;border-radius:2px;background:var(--accent);transform:scaleX(0);transition:transform .2s ease}
.nav a:not(.btn):hover::after{transform:scaleX(1)}
@media(max-width:900px){.nav a:not(.btn)::after{display:none}}
@media(max-width:760px){
  .sticky-cta{background:transparent;border-top:0;box-shadow:none;padding:10px 14px calc(10px + env(safe-area-inset-bottom));transition:transform .3s ease,opacity .3s ease;pointer-events:none}
  .sticky-cta .btn{pointer-events:auto;box-shadow:0 3px 0 var(--accent-dark),0 10px 28px rgba(60,41,15,.28);border-radius:12px}
  .sticky-cta.is-weg{transform:translateY(120%);opacity:0}
}

/* ---------- Scroll-onthulling via JS (alleen onder de vouw) ---------- */
.rv{opacity:0;transform:translateY(16px);transition:opacity .5s ease,transform .5s ease}
.rv.rv-in{opacity:1;transform:none}

@media(prefers-reduced-motion:reduce){
  .tool-kaart,.tool-beeld svg,.tool-knop span,.faq summary::after,.sticky-cta,.header{transition:none}
  .tool-kaart:hover,.tool-kaart:hover .tool-beeld svg{transform:none}
  .choice input:checked,.faq details[open] .a{animation:none}
  .rv{opacity:1;transform:none;transition:none}
}
'''

APP_JS += r'''
/* ---------- Visuele ronde 2: header, sticky CTA en onthulling ---------- */
(function () {
  "use strict";
  var header = document.querySelector(".header");
  if (header) {
    var zet = function () { header.classList.toggle("is-gescrold", window.scrollY > 8); };
    zet();
    window.addEventListener("scroll", zet, { passive: true });
  }
  if (!("IntersectionObserver" in window)) return;

  /* De mobiele knop verdwijnt zolang er al een formulier of eind-CTA in beeld is. */
  var sticky = document.querySelector(".sticky-cta");
  if (sticky) {
    var zichtbaar = new Set();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { zichtbaar.add(e.target); } else { zichtbaar.delete(e.target); } });
      sticky.classList.toggle("is-weg", zichtbaar.size > 0);
    }, { threshold: 0.15 });
    document.querySelectorAll(".formcard, .cta, .cta-midden, .prijskaart, .footer").forEach(function (el) { io.observe(el); });
  }

  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var doel = [].slice.call(document.querySelectorAll(".tablewrap, .faq details, .prose > .callout, .prose > .foto, .prijskaart, .kk-teaser, .hc-teaser"))
    .filter(function (el) { return !el.closest(".reveal") && el.getBoundingClientRect().top > window.innerHeight; });
  var io2 = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("rv-in"); io2.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
  doel.forEach(function (el, i) { el.classList.add("rv"); io2.observe(el); });
})();
'''


def css_klein(css):
    """Lichte verkleining voor de build: commentaar en overbodige witruimte eruit."""
    import re
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,])\s*", r"\1", css)
    return css.replace(";}", "}").strip()

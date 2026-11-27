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
.oc-rij{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px 8px;align-items:end;padding:10px 0 12px;border-bottom:1px solid var(--line)}
.oc-rij select,.oc-rij input[type=text]{padding:7px 8px;font-size:.88rem;height:38px;box-sizing:border-box}
.oc-rij .oc-oms{grid-column:1/-1;font-weight:600;width:calc(100% - 34px)}
.oc-rij .oc-weg{position:absolute;right:0;top:14px;border:0;background:none;color:var(--muted);font-size:1.3rem;cursor:pointer;line-height:1;align-self:center}
.oc-veld{display:flex;flex-direction:column;gap:2px;margin:0;font-weight:400;min-width:0}
.oc-veld span{font-size:.74rem;color:var(--muted);font-weight:600}
.oc-veld-type{grid-column:1/-1}
.oc-mee{grid-column:1/-1;display:flex;gap:8px;align-items:center;font-size:.84rem;font-weight:400;margin:2px 0 0}
.oc-mee input{accent-color:var(--accent);width:16px;height:16px}
.oc-label{grid-column:1/-1;color:#8a5200;font-size:.8rem}
@media(max-width:560px){.oc-rij{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}
.oc-totalen{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-bottom:6px}
.oc-totalen .field{margin:0}
.oc-totalen label{font-size:.8rem}
.oc-totalen input,.oc-totalen select{padding:8px;font-size:.9rem}
@media(max-width:420px){.oc-totalen{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.oc-totalen .field:nth-child(2){grid-column:1/-1;order:3}}
.oc-controle{font-size:.86rem;margin:6px 0 10px;padding:0}
.oc-controle.oc-ok{color:#1e6b3a;background:#e7f5ec;padding:8px 10px;border-radius:8px}
.oc-controle.oc-let,.oc-gevonden .oc-let{color:#8a3b00;background:#fff4e6;padding:8px 10px;border-radius:8px}
.oc-gevonden{background:var(--bg-soft);border-radius:10px;padding:12px 14px;margin:12px 0 4px;font-size:.86rem}
.oc-gevonden h4{font-size:.92rem;margin:0 0 6px}
.oc-gevonden dl{display:grid;grid-template-columns:max-content minmax(0,1fr);gap:3px 12px;margin:0}
.oc-gevonden dt{color:var(--muted);font-weight:600}
.oc-gevonden dd{margin:0;overflow-wrap:anywhere}
.oc-vraag{font-size:.84rem;margin:4px 0 0;color:var(--body)}
.oc-vraag::before{content:"Vraag: ";font-weight:700}
.oc-vragen li{margin-bottom:5px;font-size:.92rem}
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
    var keys = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "gbraid", "wbraid", "fbclid"];
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
      // Klik vanaf Facebook/Instagram zonder utm-tags: toch herkenbaar als Meta.
      payload.utm_source = attr.utm_source || (attr.fbclid ? "facebook" : "");
      payload.utm_medium = attr.utm_medium || (attr.fbclid ? "fbclid" : "");
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
// Het uitlezen zelf staat in /assets/js/offerte-parser.js (window.TSOfferte).
(function () {
  var box = document.querySelector("[data-offertecheck]");
  if (!box || !window.TSOfferte) return;
  var O = window.TSOfferte;
  var BANDEN = window.TS_PRIJSBANDEN || {};
  var hand = document.querySelector("[data-handcheck]");
  document.querySelectorAll("[data-check-uit]").forEach(function (e) { e.hidden = true; });
  document.querySelectorAll("[data-check-aan]").forEach(function (e) { e.hidden = false; });
  box.hidden = false;
  if (hand) hand.hidden = true;
  box.querySelector("[data-oc-hand]").addEventListener("click", function () { if (hand) hand.hidden = false; });

  var $ = function (s) { return box.querySelector(s); };
  var rijen = $("[data-oc-rijen]"), melding = $("[data-oc-melding]"), fout = $("[data-oc-fout]");
  var uitslag = $("[data-oc-uitslag]"), plaats = $("[name=plaats]"), gevonden = $("[data-oc-gevonden]");
  var vTex = $("[data-oc-tex]"), vTin = $("[data-oc-tin]"), vTarief = $("[data-oc-tarief]"), ctrl = $("[data-oc-controle]");
  var gelezen = null; // laatste uitleesresultaat, voor de extra gegevens

  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  var euro = O.euro, getal = O.getal;
  function nl(n) { return n == null ? "" : String(Math.round(n * 100) / 100).replace(".", ","); }
  function basis() { return box.querySelector("[name=btwsoort]:checked").value; }

  var typeOpties = Object.keys(O.TYPES).map(function (k) {
    return "<option value='" + k + "'>" + O.TYPES[k].naam + "</option>";
  }).join("");
  var eenheidOpties = "<option value=''>–</option>" + Object.keys(O.EENHEDEN).map(function (k) {
    return "<option value='" + k + "'>" + O.EENHEDEN[k] + "</option>";
  }).join("");

  /* --------------------------- posten (bewerkbaar) */
  function voegRijToe(p) {
    p = p || {};
    var r = document.createElement("div");
    r.className = "oc-rij";
    var labels = [];
    if (p.berekend && p.eenheidsprijs != null) labels.push("berekend: " + nl(p.aantal) + " × " + euro(p.eenheidsprijs));
    if (p.stelpost) labels.push("stelpost");
    if (p.optie) labels.push(p.variant ? "andere variant" : "optie, niet in het totaal");
    else if (p.naTotaal) labels.push("staat na het totaal");
    if (p.alleenTarief) labels.push("alleen een prijs per eenheid");
    r.innerHTML =
      "<input type='text' class='oc-oms' aria-label='Omschrijving' placeholder='Omschrijving'>" +
      "<button type='button' class='oc-weg' aria-label='Post verwijderen'>×</button>" +
      "<label class='oc-veld oc-veld-type'><span>Soort werk</span><select class='oc-type'>" + typeOpties + "</select></label>" +
      "<label class='oc-veld'><span>Aantal</span><input type='text' inputmode='decimal' class='oc-aantal'></label>" +
      "<label class='oc-veld'><span>Eenheid</span><select class='oc-eenheid'>" + eenheidOpties + "</select></label>" +
      "<label class='oc-veld'><span>Bedrag</span><input type='text' inputmode='decimal' class='oc-bedrag' placeholder='€'></label>" +
      "<label class='oc-veld'><span>Btw</span><select class='oc-btwp'><option value=''>–</option><option value='9'>9%</option><option value='21'>21%</option></select></label>" +
      "<label class='oc-mee'><input type='checkbox' class='oc-tel'> telt mee in het totaal</label>" +
      (labels.length ? "<small class='oc-label'>" + esc(labels.join(" · ")) + "</small>" : "");
    var q = function (s) { return r.querySelector(s); };
    q(".oc-oms").value = p.omschrijving || "";
    q(".oc-type").value = p.type || "wanden";
    if (p.aantal != null) q(".oc-aantal").value = nl(p.aantal);
    q(".oc-eenheid").value = p.eenheid || (p.type ? "" : O.TYPES.wanden.eenheid);
    var bedrag = p.bedrag != null ? p.bedrag : (p.alleenTarief ? null : null);
    if (bedrag != null) q(".oc-bedrag").value = nl(bedrag);
    else if (p.alleenTarief && p.eenheidsprijs != null) q(".oc-bedrag").placeholder = euro(p.eenheidsprijs) + " per " + (O.EENHEDEN[p.eenheid] || "eenheid");
    q(".oc-btwp").value = p.btw != null ? String(p.btw) : "";
    q(".oc-tel").checked = p.meetellen !== false;
    r._post = p;
    q(".oc-type").addEventListener("change", function () {
      var t = O.TYPES[this.value];
      if (t && t.eenheid && !q(".oc-eenheid").value) q(".oc-eenheid").value = t.eenheid;
      if (this.value === "korting") { var b = getal(q(".oc-bedrag").value); if (b > 0) q(".oc-bedrag").value = nl(-b); }
    });
    q(".oc-weg").addEventListener("click", function () { r.remove(); werkControleBij(); });
    rijen.appendChild(r);
  }
  function leesRijen() {
    return [].slice.call(rijen.children).map(function (r) {
      var q = function (s) { return r.querySelector(s); };
      var oud = r._post || {};
      var bedrag = getal(q(".oc-bedrag").value);
      var type = q(".oc-type").value;
      if (type === "korting" && bedrag > 0) bedrag = -bedrag;
      return {
        omschrijving: q(".oc-oms").value.trim(), type: type, aantal: getal(q(".oc-aantal").value),
        eenheid: q(".oc-eenheid").value || null, bedrag: bedrag, btw: q(".oc-btwp").value ? parseInt(q(".oc-btwp").value, 10) : null,
        meetellen: q(".oc-tel").checked, stelpost: !!oud.stelpost, optie: !!oud.optie,
        alleenTarief: bedrag == null && !!oud.alleenTarief, eenheidsprijs: bedrag == null ? oud.eenheidsprijs : null
      };
    });
  }
  $("[data-oc-plus]").addEventListener("click", function () { voegRijToe({ type: "wanden", eenheid: "m2" }); });
  rijen.addEventListener("input", werkControleBij);
  rijen.addEventListener("change", werkControleBij);
  [vTex, vTin, vTarief].forEach(function (e) { e.addEventListener("input", werkControleBij); });
  box.querySelectorAll("[name=btwsoort]").forEach(function (e) { e.addEventListener("change", werkControleBij); });
  voegRijToe({ type: "wanden", eenheid: "m2" });

  /* --------------------------- tellen ze op? */
  function controle() {
    var posten = leesRijen().filter(function (p) { return p.meetellen && p.bedrag != null; });
    var som = posten.reduce(function (s, p) { return s + p.bedrag; }, 0);
    var b = basis(), tex = getal(vTex.value), tin = getal(vTin.value);
    var tegen = b === "incl" ? tin : tex;
    return { n: posten.length, som: Math.round(som * 100) / 100, tegen: tegen, basis: b,
      klopt: tegen == null || !posten.length ? null : Math.abs(som - tegen) <= Math.max(1.5, tegen * 0.003) };
  }
  function werkControleBij() {
    var c = controle(), b = c.basis === "incl" ? "incl. btw" : "excl. btw";
    ctrl.className = "oc-controle";
    if (!c.n) { ctrl.textContent = ""; return; }
    if (c.klopt === true) {
      ctrl.classList.add("oc-ok");
      ctrl.textContent = "De posten tellen op tot " + euro(c.som) + " " + b + ". Dat is gelijk aan het totaal op de offerte.";
    } else if (c.klopt === false) {
      ctrl.classList.add("oc-let");
      ctrl.textContent = "Let op: de posten tellen op tot " + euro(c.som) + " " + b + ", maar het totaal is " + euro(c.tegen) +
        " (verschil " + euro(c.tegen - c.som) + "). Mist er een post, staat er een dubbel, of klopt incl./excl. btw niet? Pas het hieronder aan.";
    } else {
      ctrl.textContent = "De posten tellen op tot " + euro(c.som) + " " + b + ". Vul het totaal van de offerte in om te controleren of alles is gevonden.";
    }
  }

  /* --------------------------- uitlezen en invullen */
  function vulIn(res) {
    gelezen = res;
    rijen.innerHTML = "";
    res.posten.forEach(voegRijToe);
    if (!res.posten.length) voegRijToe({ type: "wanden", eenheid: "m2" });
    box.querySelector("[name=btwsoort][value=" + (res.basis === "incl" ? "incl" : "excl") + "]").checked = true;
    vTex.value = nl(res.totaal.excl); vTin.value = nl(res.totaal.incl);
    var t = res.btwTarieven || [];
    vTarief.value = t.length > 1 ? "gemengd" : t.length ? String(t[0]) : "";
    if (res.totaal.twijfel != null && res.totaal.incl == null && res.totaal.excl == null) vTin.value = nl(res.totaal.twijfel);
    Object.keys(res.lijst).forEach(function (k) {
      var c = box.querySelector("[name=lijst][value=" + k + "]");
      if (c) c.checked = res.lijst[k];
    });

    // Wat we lazen, zodat je het kunt nalopen.
    var bron = function (k) {
      var b = res.totaal.bron[k];
      return b === "berekend" ? " (berekend)" : b === "posten" ? " (opgeteld uit de posten)" : b === "betalingsschema" ? " (uit het betalingsschema)" : "";
    };
    var regels = [];
    if (res.totaal.excl != null) regels.push(["Totaal excl. btw", euro(res.totaal.excl) + bron("excl")]);
    if (res.totaal.btw != null && res.totaal.btw > 0) regels.push(["Btw", euro(res.totaal.btw) + (t.length ? " (" + t.join("% en ") + "%)" : "")]);
    if (res.totaal.incl != null) regels.push(["Totaal incl. btw", euro(res.totaal.incl) + bron("incl")]);
    if (res.totaal.twijfel != null && res.totaal.incl == null && res.totaal.excl == null)
      regels.push(["Totaal", euro(res.totaal.twijfel) + ". Er staat niet bij of dit incl. of excl. btw is. We hebben het als incl. btw ingevuld: pas het aan als dat niet klopt."]);
    if (res.varianten.length > 1) regels.push(["Varianten", res.varianten.map(function (v) { return v.naam + ": " + euro(v.totaal) + " " + v.soort + "."; }).join(" · ")]);
    if (res.merken.length) regels.push(["Verf", res.merken.join(", ")]);
    if (res.lagen.tekst) regels.push(["Lagen", res.lagen.tekst]);
    if (res.uurloon) regels.push(["Uurloon", euro(res.uurloon)]);
    if (res.garantie) regels.push(["Garantie", res.garantie]);
    if (res.geldigheid) regels.push(["Geldig", res.geldigheid]);
    if (res.termijnen.length) regels.push(["Betaling", res.termijnen.map(function (x) { return (x.procent != null ? x.procent + "% " : "") + x.omschrijving.toLowerCase() + " (" + euro(x.bedrag) + ")"; }).join(", ")]);
    if (res.betaaltermijn) regels.push(["Betaaltermijn", res.betaaltermijn]);
    if (res.doorlooptijd) regels.push(["Doorlooptijd", res.doorlooptijd]);
    gevonden.innerHTML = regels.length ? "<h4>Dit hebben we gelezen</h4><dl>" + regels.map(function (r) {
      return "<dt>" + esc(r[0]) + "</dt><dd>" + esc(r[1]) + "</dd>";
    }).join("") + "</dl>" + res.meldingen.map(function (m) { return "<p class='oc-let'>" + esc(m) + "</p>"; }).join("") : "";
    gevonden.hidden = !regels.length;

    var n = res.posten.length;
    melding.textContent = n
      ? n + (n === 1 ? " post" : " posten") + " gevonden. Loop ze hieronder na: klopt een bedrag of soort werk niet, pas het dan aan."
      : res.totaal.twijfel != null || res.totaal.incl != null || res.totaal.excl != null
        ? "We vonden een totaal maar geen losse posten. Vul de posten zelf in als je ze per stuk wilt vergelijken."
        : "We vonden geen posten met een bedrag. Vul ze hieronder zelf in.";
    werkControleBij();
    $("[data-oc-stap2]").scrollIntoView({ behavior: "smooth", block: "start" });
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
      for (var i = 1; i <= Math.min(doc.numPages, 10); i++) paginas.push(doc.getPage(i).then(function (pg) { return pg.getTextContent(); }));
      return Promise.all(paginas);
    }).then(function (inh) {
      return inh.map(function (c) { return O.regelsUitItems(c.items); }).join("\n");
    });
  }

  $("[data-oc-lees]").addEventListener("click", function () {
    var bestand = $("[name=bestand]").files[0];
    var tekst = $("[name=tekst]").value;
    melding.textContent = "";
    if (bestand) {
      if (bestand.type !== "application/pdf" && !/\.pdf$/i.test(bestand.name)) { melding.textContent = "Alleen pdf-bestanden kunnen we uitlezen. Heb je een foto, vul de posten dan zelf in."; return; }
      melding.textContent = "Bezig met uitlezen…";
      pdfNaarTekst(bestand).then(function (t) {
        if (t.replace(/\s/g, "").length < 30) {
          melding.textContent = "Deze pdf bevat geen leesbare tekst, waarschijnlijk een scan. Vul de posten zelf in.";
          return;
        }
        vulIn(O.leesOfferte(t));
      }).catch(function () { melding.textContent = "Deze pdf konden we niet openen. Vul de posten zelf in."; });
    } else if (tekst.trim().length > 10) {
      vulIn(O.leesOfferte(tekst));
    } else {
      melding.textContent = "Kies een pdf of plak eerst de tekst van de offerte.";
    }
  });

  /* --------------------------- uitslag */
  // Link naar het aanvraagformulier met klus en plaats alvast ingevuld.
  function aanvraagLink(posten) {
    var cats = posten.map(function (p) { return p.type; });
    var heeft = function (c) { return cats.indexOf(c) >= 0; };
    var dienst = (heeft("buitenkozijn") || heeft("steiger") || heeft("boeidelen") || heeft("buitendeur") || heeft("dakkapel")) ? "Buitenschilderwerk"
      : heeft("houtrot") ? "Houtrot reparatie"
      : (heeft("keukenfront") && cats.length === 1) ? "Spuitwerk"
      : (heeft("behang") && cats.length === 1) ? "Behangen"
      : "Binnenschilderwerk";
    var naam = plaats.value && plaats.value !== "1" ? plaats.options[plaats.selectedIndex].text : "";
    return "/offerte-aanvragen/?dienst=" + encodeURIComponent(dienst) +
      (naam ? "&plaats=" + encodeURIComponent(naam) : "") + "&via=offertecheck#offerte";
  }

  $("[data-oc-check]").addEventListener("click", function () {
    fout.classList.remove("show");
    if (!plaats.value) { fout.textContent = "Kies je plaats."; fout.classList.add("show"); return; }
    var index = parseFloat(plaats.value) || 1;
    var b = basis();
    var tarief = vTarief.value === "21" ? 21 : 9;
    var posten = leesRijen().filter(function (p) { return p.bedrag != null || p.alleenTarief; });
    var tex = getal(vTex.value), tin = getal(vTin.value);
    if (!posten.length && tex == null && tin == null) { fout.textContent = "Vul minstens één post of het totaal in."; fout.classList.add("show"); return; }

    var LABEL = { laag: "Onder de richtprijs", binnen: "Binnen de richtprijs", hoog: "Boven de richtprijs" };
    var tel = { laag: 0, binnen: 0, hoog: 0 }, html = "", postVragen = [];
    posten.forEach(function (p) {
      var o = O.beoordeelPost(p, BANDEN, index, b, tarief);
      var naam = p.omschrijving || O.TYPES[p.type].naam;
      var soort = O.TYPES[p.type].naam;
      var detail = [];
      if (p.aantal != null) detail.push(nl(p.aantal) + " " + (O.EENHEDEN[p.eenheid] || ""));
      if (p.bedrag != null) detail.push(euro(p.bedrag) + (b === "incl" ? " incl." : " excl.") + " btw" + (p.btw ? " (" + p.btw + "%)" : ""));
      else if (p.eenheidsprijs != null) detail.push(euro(p.eenheidsprijs) + " per " + (O.EENHEDEN[p.eenheid] || "eenheid"));
      if (!p.meetellen) detail.push("telt niet mee in het totaal");
      var badge;
      if (o.oordeel) {
        tel[o.oordeel]++;
        badge = "<span class='oc-oordeel oc-" + o.oordeel + "'>" + LABEL[o.oordeel] + "</span>";
        if (o.inclBtw && b === "excl") detail.push("met btw " + euro(Math.round(o.vergelijk)));
        detail.push("richtprijs " + euro(o.van) + " – " + euro(o.tot) + (o.inclBtw ? " incl." : " excl.") + " btw");
      } else {
        var waarom = { "geen richtprijs": "geen richtprijs voor dit soort werk", "geen aantal": "vul het aantal in om te vergelijken",
          "andere eenheid": "vergelijken kan in " + (O.EENHEDEN[(O.TYPES[p.type] || {}).eenheid] || "een andere eenheid"), "korting": "korting", "geen bedrag": "geen bedrag" }[o.reden] || "";
        badge = "<span class='oc-oordeel oc-geen'>Niet te vergelijken</span>";
        if (waarom && o.reden !== "korting") detail.push(waarom);
      }
      // In de lijst onderaan alleen de posten die opvallen; de rest staat bij de post zelf.
      if (o.oordeel === "hoog") postVragen.push(naam + ": waarom ligt deze post boven de richtprijs? Wat zit er precies in?");
      else if (o.oordeel === "laag") postVragen.push(naam + ": zitten alle lagen en het voorwerk in deze prijs?");
      o.vragen.forEach(function (v) { if (/stelpost|21% btw/.test(v) && postVragen.indexOf(v) < 0) postVragen.push(naam + ": " + v.charAt(0).toLowerCase() + v.slice(1)); });
      html += "<li><div class='oc-post'><strong>" + esc(naam) + "</strong>" + badge + "</div>" +
        "<small>" + esc(soort) + " · " + esc(detail.join(" · ")) + "</small>" +
        (o.vragen.length ? "<p class='oc-vraag'>" + esc(o.vragen[0]) + "</p>" : "") + "</li>";
    });

    var lijst = {};
    box.querySelectorAll("[name=lijst]").forEach(function (c) { lijst[c.value] = c.checked; });
    var res = gelezen || { posten: posten, termijnen: [], lijst: lijst };
    var buiten = posten.some(function (p) { return ["buitenkozijn", "buitendeur", "boeidelen", "dakkapel", "steiger", "houtrot"].indexOf(p.type) >= 0; });
    var c = controle();
    var info = { buiten: buiten || !!res.buiten, termijnen: res.termijnen || [], concept: res.concept, garantie: res.garantie,
      controle: c, btwTarieven: vTarief.value === "gemengd" ? [9, 21] : vTarief.value ? [parseInt(vTarief.value, 10)] : [], posten: posten };
    var algemeen = O.algemeneVragen(info, lijst);
    // Uurloon voor meerwerk naast de richtprijs leggen.
    if (gelezen && gelezen.uurloon && BANDEN.uurloon && !posten.some(function (p) { return p.type === "uren"; })) {
      var ul = O.beoordeelPost({ type: "uren", aantal: 1, eenheid: "uur", bedrag: gelezen.uurloon }, BANDEN, index, gelezen.basis, tarief);
      if (ul.oordeel === "hoog") algemeen.push("Het uurloon voor meerwerk (" + euro(gelezen.uurloon) + ") ligt boven de richtprijs. Vraag of daar iets over te zeggen valt.");
    }
    var vragen = algemeen.concat(postVragen.filter(function (v) { return algemeen.indexOf(v) < 0; }));

    var kop = tel.hoog > 0 ? "Een deel van je offerte ligt boven de richtprijs"
      : tel.laag > 0 ? "Je offerte ligt deels onder de richtprijs"
      : tel.binnen > 0 ? "Je offerte ligt binnen de richtprijzen" : "We konden de posten niet naast de richtprijs leggen";
    var uitleg = tel.hoog > 0 ? "Dat kan kloppen, bijvoorbeeld bij slecht hout of veel voorwerk. Vraag de schilder waar het verschil in zit, of leg er een tweede offerte naast."
      : tel.laag > 0 ? "Een lage prijs is niet altijd slecht. Check wel of alles erin zit, zoals het aantal lagen, de steiger en houtrot."
      : tel.binnen > 0 ? "Check hieronder of er niets ontbreekt. Dan weet je zeker dat je appels met appels vergelijkt."
      : "Vul bij de posten het soort werk en het aantal in, dan kunnen we ze naast de richtprijs leggen.";
    var totaalTekst = [tex != null ? euro(tex) + " excl. btw" : "", tin != null ? euro(tin) + " incl. btw" : ""].filter(Boolean).join(" · ");
    var tarTekst = vTarief.value === "gemengd" ? " (9% en 21% btw)" : vTarief.value ? " (" + vTarief.value + "% btw)" : "";

    uitslag.innerHTML = "<h2>" + kop + "</h2><p>" + uitleg + "</p>" +
      (totaalTekst ? "<p><strong>Totaal van de offerte:</strong> " + totaalTekst + tarTekst + "</p>" : "") +
      (c.n ? "<p class='oc-controle " + (c.klopt === false ? "oc-let" : c.klopt ? "oc-ok" : "") + "'>" + esc(ctrl.textContent) + "</p>" : "") +
      (html ? "<h3>Per post</h3><ul class='oc-posten'>" + html + "</ul>" : "") +
      "<h3>" + (vragen.length ? "Vraag de schilder" : "Alles staat erin") + "</h3>" +
      (vragen.length ? "<ul class='oc-vragen'>" + vragen.map(function (m) { return "<li>" + esc(m) + "</li>"; }).join("") + "</ul>" : "<p>De belangrijkste punten staan in de offerte. Goed teken.</p>") +
      "<p class='formfoot'>Vergeleken met onze richtprijzen voor jouw regio. Dit is een indicatie, geen oordeel over het bedrijf.</p>" +
      "<div class='formnav'><a class='btn btn-primary' href='" + aanvraagLink(posten) + "'>" +
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
    var bij = function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { zichtbaar.add(e.target); } else { zichtbaar.delete(e.target); } });
      sticky.classList.toggle("is-weg", zichtbaar.size > 0);
    };
    var io = new IntersectionObserver(bij, { threshold: 0.15 });
    document.querySelectorAll(".formcard, .cta, .cta-midden, .prijskaart").forEach(function (el) { io.observe(el); });
    /* De footer is hoog: 15% zichtbaar is pas na ruim 200px. Zo lang zou de knop de bovenkant
       van de footer bedekken. Daarom weg zodra de footer ook maar in beeld komt. */
    var voet = document.querySelector(".footer");
    if (voet) { new IntersectionObserver(bij, { threshold: 0 }).observe(voet); }
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


STYLE_CSS += r"""
/* =========================================================================
   Ronde 3 — visuele bouwstenen (componenten staan in components.py)
   ========================================================================= */

:root{--penseel:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 220 24' preserveAspectRatio='none'%3E%3Cpath d='M3 12C40 5 90 4 130 6s60 3 87 1l-1 10c-30 4-62 2-96 1S40 16 4 21z' fill='%23f4820b' fill-opacity='.4'/%3E%3C/svg%3E");--golf:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 28' preserveAspectRatio='none'%3E%3Cpath d='M0 28V16C140 5 260 1 390 6s250 18 380 16 250-16 380-17 210 6 290 12v11z'/%3E%3C/svg%3E")}

/* ---------- Typografie en ritme ---------- */
h1,h2,h3{text-wrap:balance}
p,li{text-wrap:pretty}
.lead{line-height:1.6}

/* ---------- Penseelstreek onder een woord: streep("woord") ---------- */
.section .center > h2:has(.streep)::after{display:none}
.streep{background:var(--penseel) 0 88%/100% .42em no-repeat;padding:0 .08em;margin:0 -.08em;-webkit-box-decoration-break:clone;box-decoration-break:clone}

/* ---------- Dienst-iconen: vlakken in de accentkleur ---------- */
.dicon .ia{fill:var(--accent);stroke:none;opacity:.9}
.badge-ic{display:inline-flex;align-items:center;gap:7px}
.badge-ic .dicon{color:#7a3f00}

/* ---------- Dienstkaarten: icoon op de foto ---------- */
.card-dienst > .foto{position:relative}
.card-chip{position:absolute;left:14px;bottom:14px;width:46px;height:46px;border-radius:14px;background:#fff;color:var(--navy);display:grid;place-items:center;box-shadow:0 6px 16px rgba(36,25,6,.22);transition:transform .3s ease}
.card-dienst:hover .card-chip{transform:translateY(-3px) rotate(-5deg)}
@media(max-width:600px){.card-chip{display:none}}

/* ---------- Feitenblok: feiten_blok([...]) ---------- */
.feiten{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));gap:14px;margin:34px 0 0}
.feit{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:18px 20px 16px;position:relative;overflow:hidden;box-shadow:0 1px 2px rgba(60,41,15,.04)}
.feit::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:linear-gradient(180deg,var(--accent),#ffcf94)}
.feit-getal{display:inline-block;font-size:clamp(1.8rem,3.4vw,2.3rem);font-weight:800;color:var(--ink);line-height:1.05;margin:0 0 6px;letter-spacing:-.03em;font-variant-numeric:tabular-nums;background:var(--penseel) 0 100%/100% .3em no-repeat;padding-bottom:.18em}
.feit-label{font-size:.9rem;margin:0;color:var(--body);line-height:1.45}
.feit-label a{color:#8a4500;font-size:.82rem}
.feiten-noot{font-size:.82rem;color:var(--muted);margin:10px 0 0}
.soft .feit{background:#fff}
.feiten-donker .feit{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.14);box-shadow:none}
.feiten-donker .feit-getal{color:#fff}
.feiten-donker .feit-label{color:#e3d6c2}
.prose .feiten{margin:24px 0 8px}
@media(max-width:560px){.feiten{grid-template-columns:1fr 1fr;gap:10px}.feit{padding:14px 14px 12px}.feit-getal{font-size:1.6rem}.feit-label{font-size:.84rem}.feit:last-child:nth-child(odd){grid-column:1/-1}}

/* ---------- Stappen-tijdlijn: stappen_blok([...]) ---------- */
.stappen{list-style:none;padding:0;margin:22px 0 26px}
ol.stappen > li{display:grid;grid-template-columns:44px minmax(0,1fr);column-gap:18px;margin:0;padding:0 0 22px;counter-increment:none;position:relative}
ol.stappen > li::before{content:"";counter-increment:none;border-radius:0;box-shadow:none;height:auto;display:block;font-size:0;position:absolute;left:21px;top:50px;bottom:4px;width:2px;background:repeating-linear-gradient(180deg,#eebd85 0 7px,transparent 7px 12px)}
ol.stappen > li:last-child{padding-bottom:0}
ol.stappen > li:last-child::before{display:none}
.stap-nr{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font-weight:800;font-size:1.05rem;color:#fff;background:var(--navy);box-shadow:0 0 0 4px var(--accent-soft),0 0 0 6px #f6c995;position:relative;z-index:1}
.stappen h3,.prose .stappen h3{margin:8px 0 .2em;font-size:1.1rem}
.stappen p{margin:0;font-size:.97rem}

/* ---------- Foto met bijschrift: foto_kader(...) ---------- */
.foto-kader{position:relative;isolation:isolate;margin:34px 0 30px}
.foto-kader::before{content:"";position:absolute;left:-10px;top:-10px;width:110px;height:110px;border-radius:16px;background:repeating-linear-gradient(-45deg,#fbd3a2 0 5px,transparent 5px 11px);z-index:-1}
.foto-kader img{box-shadow:var(--shadow-lg)}
.foto-kader figcaption{font-size:.86rem;color:var(--muted);margin-top:12px;padding-left:12px;border-left:3px solid var(--accent);line-height:1.5}
.foto-credit{display:block;font-size:.78rem;margin-top:2px}
.foto-credit a{color:var(--muted)}

/* ---------- Prijsbalken: prijs_balken([...]) ---------- */
.prijs-balken{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:18px 22px 14px;margin:20px 0 18px;box-shadow:var(--shadow)}
.prijs-balken ul{list-style:none;padding:0;margin:0}
.prijs-balken li{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1.4fr) 8.6em;gap:16px;align-items:center;margin:0;padding:10px 0;border-top:1px solid var(--line)}
.prijs-balken li:first-child{border-top:0}
.pb-eenheid{font-size:.78rem;font-weight:750;letter-spacing:.06em;text-transform:uppercase;color:#a35200;margin:0 0 4px}
.pb-label{font-weight:650;color:var(--ink);font-size:.93rem;line-height:1.35}
.pb-baan{height:12px;border-radius:99px;background:var(--bg-soft);box-shadow:inset 0 0 0 1px var(--line);overflow:hidden}
.pb-balk{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,#ffb15c,var(--accent));transform-origin:left center}
.pb-bedrag{font-variant-numeric:tabular-nums;font-weight:700;color:var(--ink);font-size:.92rem;white-space:nowrap;text-align:right}
.pb-noot{font-size:.82rem;color:var(--muted);margin:8px 0 0}
.prijs-balken.reveal .pb-balk{transform:scaleX(0);transition:transform .9s cubic-bezier(.2,.7,.2,1) .25s}
.prijs-balken.reveal.in .pb-balk{transform:none}
@media(max-width:560px){
  .prijs-balken{padding:16px 16px 12px}
  .prijs-balken li{grid-template-columns:minmax(0,1fr) auto;row-gap:7px;column-gap:10px}
  .pb-baan{grid-column:1/-1;grid-row:2}
}

/* ---------- Voor/na: label dat het een illustratie is ---------- */
.vn-soort{position:absolute;top:12px;left:12px;font-size:.72rem;font-weight:750;letter-spacing:.05em;text-transform:uppercase;background:rgba(255,255,255,.92);color:#6b3600;padding:4px 10px;border-radius:99px}

/* ---------- Mobiel menu ---------- */
.burger{width:44px;height:44px;padding:0;position:relative;border-radius:11px;background:#fff;font-size:0;color:var(--ink)}
.burger span{position:absolute;left:12px;right:12px;height:2px;border-radius:2px;background:currentColor;transition:transform .25s ease,opacity .2s ease}
.burger span:nth-child(1){top:15px}.burger span:nth-child(2){top:21px}.burger span:nth-child(3){top:27px}
.burger[aria-expanded="true"] span:nth-child(1){transform:translateY(6px) rotate(45deg)}
.burger[aria-expanded="true"] span:nth-child(2){opacity:0}
.burger[aria-expanded="true"] span:nth-child(3){transform:translateY(-6px) rotate(-45deg)}
.burger:focus-visible,.nav a:focus-visible{outline:3px solid #ffb15c;outline-offset:2px}
.nav-ic,.nav-noot{display:none}
.nav-scherm{display:none}
@media(max-width:900px){
  .nav{display:flex;visibility:hidden;opacity:0;transform:translateY(-10px);transition:opacity .2s ease,transform .2s ease,visibility 0s linear .2s;max-height:calc(100vh - 70px);overflow-y:auto;padding:10px 16px 18px;gap:2px;border-radius:0 0 18px 18px}
  .nav.open{visibility:visible;opacity:1;transform:none;transition:opacity .2s ease,transform .2s ease}
  .nav a:not(.btn){display:flex;align-items:center;gap:13px;padding:10px;border-radius:12px;font-size:1.04rem}
  .nav a:not(.btn)::after{display:block;content:"›";position:static;margin-left:auto;transform:none;background:none;height:auto;width:auto;font-size:1.4rem;line-height:1;color:var(--muted)}
  .nav-ic{display:grid;place-items:center;flex:0 0 38px;width:38px;height:38px;border-radius:11px;background:var(--accent-soft);color:#a35200}
  .nav .btn{padding:15px;margin-top:10px}
  .nav-noot{display:block;text-align:center;font-size:.85rem;color:var(--muted);margin:10px 0 0}
  .nav-scherm{display:block;position:fixed;inset:70px 0 0;background:rgba(36,25,6,.45);z-index:55;opacity:0;visibility:hidden;transition:opacity .2s ease,visibility 0s linear .2s}
  body.menu-open{overflow:hidden}
  body.menu-open .nav-scherm{opacity:1;visibility:visible;transition:opacity .2s ease}
}

/* ---------- Footer ---------- */
.footer{position:relative;background:linear-gradient(180deg,#3c290f 0%,#2a1d09 100%);color:#d9c9ae;padding-top:52px}
.footer-golf{position:absolute;left:0;right:0;top:-27px;height:28px;background:#3c290f;-webkit-mask:var(--golf) 0 0/100% 100% no-repeat;mask:var(--golf) 0 0/100% 100% no-repeat;pointer-events:none}
.footer a{color:#e8dcc8}
.footer a:hover{color:#fff}
.footer .fh{color:#fff;font-size:.82rem;text-transform:uppercase;letter-spacing:.08em}
.footer-cta{display:flex;align-items:center;justify-content:space-between;gap:22px;padding:22px 26px;margin:0 0 44px;border-radius:var(--radius-lg);background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12)}
.footer-cta p{margin:0;color:#e3d6c2}
.footer-cta .footer-cta-titel{color:#fff;font-weight:750;font-size:1.15rem;margin-bottom:2px}
.footer-cta .btn{flex:0 0 auto}
section:has(.cta) + .footer .footer-cta{display:none}
@media(max-width:620px){.footer-cta{flex-direction:column;align-items:stretch;padding:20px}}
.footer-diensten a,.footer-tools a{display:inline-flex;align-items:center;gap:10px}
.f-ic{display:grid;place-items:center;width:30px;height:30px;border-radius:9px;background:rgba(255,255,255,.08);color:#fff;flex:0 0 30px}
.footer-tools{margin-top:16px!important}
.footer-tools a{font-weight:650;color:#ffd9ab}
.footer-tools svg{color:#ffb15c}
.footer-plaatsen{display:grid;grid-template-columns:1fr 1fr;column-gap:14px}
.footer-meer{color:#ffd9ab!important;font-weight:700}
.footer-bot{border-top-color:rgba(255,255,255,.12);color:#c9b89c}
.footer-bot a{color:#d9c9ae}

@media(prefers-reduced-motion:reduce){
  .card-chip,.burger span,.nav,.nav-scherm{transition:none!important}
  .card-dienst:hover .card-chip{transform:none}
  .prijs-balken.reveal .pb-balk{transform:none;transition:none}
}
"""

APP_JS += r"""
/* ---------- Ronde 3: mobiel menu (scherm erachter, Esc, focus terug) ---------- */
(function () {
  "use strict";
  var burger = document.querySelector(".burger");
  var nav = document.getElementById("hoofdmenu");
  if (!burger || !nav) return;
  var scherm = document.createElement("div");
  scherm.className = "nav-scherm";
  document.body.appendChild(scherm);
  function sync() {
    var open = nav.classList.contains("open");
    burger.setAttribute("aria-expanded", open);
    burger.setAttribute("aria-label", open ? "Menu sluiten" : "Menu");
    document.body.classList.toggle("menu-open", open);
  }
  function sluit(focusTerug) {
    if (!nav.classList.contains("open")) return;
    nav.classList.remove("open");
    sync();
    if (focusTerug) burger.focus();
  }
  /* De klik zelf wordt al afgehandeld in het menublok hierboven; hier alleen de rest. */
  burger.addEventListener("click", function () {
    sync();
    if (nav.classList.contains("open")) { var a = nav.querySelector("a"); if (a) a.focus({ preventScroll: true }); }
  });
  scherm.addEventListener("click", function () { sluit(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") sluit(true); });
  nav.addEventListener("click", function (e) { if (e.target.closest("a")) sluit(false); });
  window.addEventListener("resize", function () { if (window.innerWidth > 900) sluit(false); });
})();
"""


def css_klein(css):
    """Lichte verkleining voor de build: commentaar en overbodige witruimte eruit."""
    import re
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,])\s*", r"\1", css)
    return css.replace(";}", "}").strip()


# =========================================================================
# PLAATSDATA — staafdiagram bouwjaren en wijktabel op plaatspagina's (plaats_content.py)
# (los blok aan het eind, zodat samenvoegen met andere branches makkelijk blijft)
# =========================================================================

STYLE_CSS += r'''
/* ---------- Plaatsdata: bouwjaren ---------- */
.pc-fig{margin:22px 0 26px;padding:18px 18px 12px;border:1px solid var(--line);border-radius:var(--radius);background:#fff}
.pc-fig figcaption{font-weight:700;color:var(--ink);margin-bottom:12px}
.pc-bars{list-style:none;margin:0;padding:0}
.pc-bars li{display:grid;grid-template-columns:7.2em 1fr 6.6em;gap:10px;align-items:center;padding:4px 0;margin:0;font-size:.92rem}
.prose .pc-bars > li{padding-left:0;margin-bottom:0;counter-increment:none}
.prose .pc-bars > li::before{content:none;display:none}
.pc-lab{color:var(--ink);white-space:nowrap}
.pc-bar{display:block;height:14px;background:var(--bg-soft);border-radius:7px;overflow:hidden}
.pc-bar span{display:block;height:100%;background:linear-gradient(90deg,var(--accent),#ffb15c);border-radius:7px}
.pc-val{font-variant-numeric:tabular-nums;font-weight:650;color:var(--ink);white-space:nowrap;text-align:right}
.pc-n{font-weight:400;color:var(--muted)}
.pc-bron{color:var(--muted);margin-top:18px}
.pc-wijken th{white-space:normal}
@media(max-width:560px){.pc-wijken th,.pc-wijken td{padding:10px 8px;font-size:.88rem}}
@media(max-width:480px){.pc-wijken .pc-groep{display:none}.pc-wijken th{letter-spacing:0;font-size:.72rem}.pc-wijken td:first-child{hyphens:auto;overflow-wrap:anywhere}}
@media(max-width:480px){.pc-bars li{grid-template-columns:6.4em 1fr 3em;gap:8px;font-size:.86rem}.pc-n{display:none}}
'''


# =========================================================================
# EFFECTEN (ronde 4) — scroll-onthulling, optellende cijfers, hero-diepte,
# hover/focus, sticky CTA, menu en micro-interacties in de tools.
# Eén los blok (CSS + JS) aan het eind, zodat samenvoegen makkelijk blijft.
# Alles respecteert prefers-reduced-motion; animaties gebruiken alleen
# transform/opacity (geen layout shift). LCP-elementen (hero-foto, h1) worden
# niet verborgen of vertraagd.
# =========================================================================

STYLE_CSS += r'''
/* ---------- Effecten: basis ---------- */
:root{--ease-uit:cubic-bezier(.2,.7,.2,1);--veer:cubic-bezier(.34,1.56,.64,1);
  --penseel-vol:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 220 24' preserveAspectRatio='none'%3E%3Cpath d='M3 13C38 6 88 4 129 6s61 2 88 0l-2 9c-29 5-61 4-95 3S41 16 5 21z' fill='%23f4820b'/%3E%3Cpath d='M30 17c40-3 90-4 150-2' stroke='%23ffb15c' stroke-width='1.6' fill='none' stroke-linecap='round' opacity='.7'/%3E%3C/svg%3E")}
h1{font-weight:800;letter-spacing:-.03em}
h2{letter-spacing:-.025em}

/* ---------- Hero (home): diepte, bewegende gloed, verfstreek ---------- */
.hero-foto .hero-bg{will-change:transform;transform:translate3d(0,var(--hero-y,0px),0) scale(1.06);transform-origin:50% 30%}
.hero-foto::after{inset:auto -15% -70% 30%;height:640px;background:radial-gradient(closest-side,rgba(244,130,11,.30),transparent);animation:ts-drift 16s ease-in-out infinite alternate}
.hero-foto .hero-in::before{content:"";position:absolute;width:420px;height:420px;left:-180px;top:-160px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,177,92,.16),transparent);pointer-events:none;z-index:-1;animation:ts-drift 20s ease-in-out -6s infinite alternate-reverse}
@keyframes ts-drift{0%{transform:translate3d(0,0,0) scale(1)}100%{transform:translate3d(-60px,-40px,0) scale(1.12)}}
.hero h1::after,.section-sm:has(> .wrap > .g2 .formcard) h1::after,.kosten-kop h1::after,.tool-hero h1::after{
  content:"";display:block;width:min(230px,58%);height:13px;margin-top:.32em;background:var(--penseel-vol) 0 0/100% 100% no-repeat;
  clip-path:inset(0 100% 0 0);animation:ts-streep .9s var(--ease-uit) .25s forwards}
@keyframes ts-streep{to{clip-path:inset(0 0 0 0)}}
.hero-usps li,.hero-tags{animation:ts-op .6s var(--ease-uit) both}
.hero-usps li:nth-child(1){animation-delay:.1s}.hero-usps li:nth-child(2){animation-delay:.18s}.hero-usps li:nth-child(3){animation-delay:.26s}.hero-tags{animation-delay:.34s}
.hero .formcard{animation:ts-kaart .7s var(--ease-uit) .05s both}
@keyframes ts-op{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes ts-kaart{from{transform:translateY(22px)}to{transform:none}}
.hero .check{animation:ts-pop .45s var(--veer) both}
.hero-usps li:nth-child(1) .check{animation-delay:.3s}.hero-usps li:nth-child(2) .check{animation-delay:.38s}.hero-usps li:nth-child(3) .check{animation-delay:.46s}
@keyframes ts-pop{from{transform:scale(.4)}to{transform:none}}

/* ---------- Pagina-intro's (dienst, plaats, kosten, tools): gradient-mesh ---------- */
.section-sm:has(> .wrap > .g2 .formcard),.kosten-kop,.tool-hero{position:relative;isolation:isolate;overflow:clip;
  background:radial-gradient(620px 380px at 92% 18%,rgba(255,214,166,.55),transparent 70%),
             radial-gradient(520px 340px at 70% 100%,rgba(255,232,204,.6),transparent 70%),
             radial-gradient(460px 300px at 0% 0%,rgba(251,239,222,.9),transparent 70%),
             linear-gradient(180deg,#fffaf3 0%,#fff 85%)}
/* overflow:clip (geen hidden) zodat het sticky formulier blijft werken; zonder clip-ondersteuning geen streep */
@supports not (overflow:clip){.section-sm:has(> .wrap > .g2 .formcard)::before,.kosten-kop::before,.tool-hero::before{display:none!important}}
.section-sm:has(> .wrap > .g2 .formcard)::before,.kosten-kop::before,.tool-hero::before{content:"";position:absolute;right:-60px;top:24px;width:340px;height:60px;z-index:-1;pointer-events:none;
  background:var(--penseel-vol) 0 0/100% 100% no-repeat;opacity:.13;transform:rotate(-8deg)}
@media(max-width:900px){.section-sm:has(> .wrap > .g2 .formcard)::before,.kosten-kop::before,.tool-hero::before{width:200px;height:36px;right:-50px;top:10px}}

/* ---------- Kaarten: lift, spotlicht onder de muis, focus = hover ---------- */
a.card::before,.tool-kaart::before{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;z-index:0;opacity:0;transition:opacity .25s ease;
  background:radial-gradient(260px circle at var(--mx,50%) var(--my,0%),rgba(244,130,11,.10),transparent 70%)}
.tool-kaart{position:relative}
a.card:hover::before,.tool-kaart:hover::before,a.card:focus-visible::before{opacity:1}
a.card > *,.tool-kaart > *{position:relative;z-index:1}
a.card > .card-chip{position:absolute}
a.card{transition:box-shadow .25s var(--ease-uit),transform .25s var(--ease-uit),border-color .2s}
a.card:focus-visible{box-shadow:var(--shadow-lg);transform:translateY(-4px);border-color:#ecd9bd;outline:3px solid #ffb15c;outline-offset:3px}
a.card:focus-visible::after{transform:scaleX(1)}
a.card:active{transform:translateY(-1px) scale(.995);transition-duration:.08s}
.tool-kaart:focus-visible{transform:translateY(-6px);outline:3px solid #ffb15c;outline-offset:3px}
.g4 > .card,.feit{transition:transform .25s var(--ease-uit),box-shadow .25s,border-color .2s}
.g4 > .card:hover,.feit:hover{transform:translateY(-3px)}
.card .ic{transition:transform .35s var(--veer)}
.card:hover .ic{transform:rotate(-6deg) scale(1.06)}
a.card .go{transition:gap .2s ease,color .2s}
a.card:hover .go,a.card:focus-visible .go{gap:10px}

/* ---------- Knoppen: indrukken, ghost-lift, focus ---------- */
.btn{transition:transform .15s var(--ease-uit),box-shadow .15s ease,background .15s ease,border-color .15s,color .15s}
.btn:active{transform:translateY(1px)}
.btn-primary:active{box-shadow:0 1px 0 var(--accent-dark)}
.btn-ghost:hover{box-shadow:0 6px 16px rgba(60,41,15,.08);background:#fff}
.btn:focus-visible{outline:3px solid #ffb15c;outline-offset:3px}
.chips a:focus-visible{outline:3px solid #ffb15c;outline-offset:2px;border-color:var(--accent)}
.choice label:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(60,41,15,.07)}
.choice label:active{transform:scale(.985)}

/* ---------- Sectiekoppen: accentstreep groeit bij in beeld komen ---------- */
.section .center > h2.rv::after{transform:scaleX(0);transition:transform .6s var(--ease-uit) .2s}
.section .center > h2.rv-in::after{transform:none}

/* ---------- Scroll-onthulling: kleine vertraging per kaart in een rij ---------- */
.rv{transition-delay:calc(var(--rv-i,0) * 70ms)}
.reveal.in .pb-balk{transition-delay:.25s}
.prijs-balken.reveal li:nth-child(2) .pb-balk{transition-delay:.35s}.prijs-balken.reveal li:nth-child(3) .pb-balk{transition-delay:.45s}
.prijs-balken.reveal li:nth-child(4) .pb-balk{transition-delay:.55s}.prijs-balken.reveal li:nth-child(n+5) .pb-balk{transition-delay:.65s}

/* ---------- Bouwjaargrafiek (plaatsen): balken vullen ---------- */
.pc-fig.rv .pc-bar span{transform:scaleX(0);transform-origin:left center;transition:transform .9s var(--ease-uit)}
.pc-fig.rv-in .pc-bar span{transform:none}
.pc-fig.rv-in li:nth-child(2) .pc-bar span{transition-delay:.06s}.pc-fig.rv-in li:nth-child(3) .pc-bar span{transition-delay:.12s}
.pc-fig.rv-in li:nth-child(4) .pc-bar span{transition-delay:.18s}.pc-fig.rv-in li:nth-child(5) .pc-bar span{transition-delay:.24s}
.pc-fig.rv-in li:nth-child(n+6) .pc-bar span{transition-delay:.3s}

/* ---------- Optellende cijfers ---------- */
.telt{font-variant-numeric:tabular-nums}

/* ---------- Leesvoortgang (pagina's met lopende tekst) ---------- */
@supports (animation-timeline: scroll()){
  body:has(.prose) .header::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:3px;background:linear-gradient(90deg,var(--accent),#ffb15c);
    transform-origin:0 50%;transform:scaleX(0);animation:ts-voortgang linear both;animation-timeline:scroll(root)}
  @keyframes ts-voortgang{to{transform:scaleX(1)}}
}

/* ---------- Mobiel menu: items schuiven één voor één in ---------- */
@media(max-width:900px){
  .nav.open > a,.nav.open > .nav-noot{animation:ts-menu .32s var(--ease-uit) both}
  .nav.open > :nth-child(2){animation-delay:.03s}.nav.open > :nth-child(3){animation-delay:.06s}.nav.open > :nth-child(4){animation-delay:.09s}
  .nav.open > :nth-child(5){animation-delay:.12s}.nav.open > :nth-child(6){animation-delay:.15s}.nav.open > :nth-child(7){animation-delay:.18s}
  .nav a:not(.btn):active{background:var(--accent-soft)}
  .nav a:not(.btn) .nav-ic{transition:transform .25s var(--veer)}
  .nav a:not(.btn):hover .nav-ic{transform:scale(1.08) rotate(-4deg)}
}
@keyframes ts-menu{from{opacity:0;transform:translateX(-12px)}to{opacity:1;transform:none}}

/* ---------- Sticky CTA (mobiel): leesbare achtergrond, veer-in en glans ---------- */
@media(max-width:760px){
  .sticky-cta::before{content:"";position:absolute;inset:-18px 0 0;background:linear-gradient(180deg,rgba(255,255,255,0),rgba(255,255,255,.92) 55%);z-index:-1;pointer-events:none;transition:opacity .3s}
  .sticky-cta{transition:transform .45s var(--veer),opacity .25s ease}
  .sticky-cta.is-weg::before{opacity:0}
  .sticky-cta:not(.is-weg) .btn::after{animation:ts-glans 1.1s ease .5s}
  .sticky-cta .pijl{display:inline-block;margin-left:6px;transition:transform .2s}
  .sticky-cta .btn:active .pijl{transform:translateX(3px)}
}
.sticky-cta .pijl{display:inline-block;margin-left:6px}
@keyframes ts-glans{from{transform:translateX(0) skewX(-18deg)}to{transform:translateX(450%) skewX(-18deg)}}

/* ---------- Tools: micro-interacties ---------- */
.ts-tik{animation:ts-tik .45s var(--veer)}
@keyframes ts-tik{0%{transform:scale(1)}40%{transform:scale(1.045)}100%{transform:scale(1)}}
[data-vc-uitkomst].ts-tik,.kk-kleurinfo.ts-tik,.sw-conclusie.ts-tik{animation-name:ts-tik-klein}
@keyframes ts-tik-klein{0%{transform:scale(1)}40%{transform:scale(1.015);box-shadow:0 8px 24px rgba(217,111,0,.14)}100%{transform:scale(1)}}
.calc-uit .bedrag,.hc-regel,.ohc-teller,.sw-conclusie{display:inline-block}
.calc-uit .bedrag{display:block}
.hc-opts label,.ohc-opts label,.ohc-opts button,.kk-stijl,.sw-dag{transition:transform .15s var(--ease-uit),box-shadow .15s,border-color .15s,background .15s}
.hc-opts label:hover,.ohc-opts label:hover,.ohc-opts button:hover,.kk-stijl:hover,.sw-dag:hover{transform:translateY(-2px);box-shadow:0 6px 16px rgba(60,41,15,.08)}
.hc-opts label:active,.ohc-opts label:active,.ohc-opts button:active,.kk-stijl:active,.sw-dag:active{transform:scale(.97)}
.kk-kleur i{transition:transform .2s var(--veer),box-shadow .2s}
.kk-kleur:hover i{transform:scale(1.14)}
.kk-kleur.on i{animation:ts-pop .4s var(--veer)}
input[type=range]{cursor:pointer}
input[type=range]:active{accent-color:var(--accent-dark)}

@media(prefers-reduced-motion:reduce){
  .hero-foto .hero-bg{transform:none;will-change:auto}
  .hero-foto::after,.hero-foto .hero-in::before,.hero-usps li,.hero-tags,.hero .formcard,.hero .check,
  .nav.open > a,.nav.open > .nav-noot,.sticky-cta .btn::after,.ts-tik,.kk-kleur.on i{animation:none!important}
  .hero h1::after,.section-sm:has(> .wrap > .g2 .formcard) h1::after,.kosten-kop h1::after,.tool-hero h1::after{animation:none;clip-path:none}
  .section .center > h2.rv::after,.pc-fig.rv .pc-bar span{transform:none;transition:none}
  a.card,a.card:focus-visible,a.card:active,.g4 > .card:hover,.feit:hover,.card:hover .ic,.tool-kaart:focus-visible,.btn:active,
  .choice label:hover,.hc-opts label:hover,.ohc-opts label:hover,.ohc-opts button:hover,.kk-stijl:hover,.sw-dag:hover,.kk-kleur:hover i{transform:none}
  .sticky-cta{transition:none}
  body:has(.prose) .header::after{display:none}
}
'''

APP_JS += r'''
/* ---------- Effecten (ronde 4): parallax, onthulling, optellen, spotlicht, tools ---------- */
(function () {
  "use strict";
  var rust = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var heeftIO = "IntersectionObserver" in window;

  /* Vangnet: heel hoge .reveal-blokken (lange teksten) halen de drempel van 5% soms nooit.
     Elke zichtbare pixel is hier genoeg. */
  if (heeftIO && !rust) {
    var vang = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); vang.unobserve(e.target); } });
    }, { threshold: 0 });
    document.querySelectorAll(".reveal:not(.in)").forEach(function (el) { vang.observe(el); });
  }

  if (rust || !heeftIO) return;

  /* Hero-foto beweegt iets langzamer mee dan de pagina (alleen desktop). */
  var bg = document.querySelector(".hero-foto .hero-bg");
  if (bg && window.matchMedia("(min-width: 921px)").matches) {
    var hero = bg.closest(".hero"), wacht = false;
    var zetY = function () {
      wacht = false;
      var y = window.scrollY;
      if (y < hero.offsetHeight + 100) hero.style.setProperty("--hero-y", (y * 0.22).toFixed(1) + "px");
    };
    window.addEventListener("scroll", function () { if (!wacht) { wacht = true; requestAnimationFrame(zetY); } }, { passive: true });
  }

  /* Meer onderdelen onthullen bij scrollen; alleen wat bij het laden onder de vouw staat. */
  var buiten = function (el) { return document.querySelector(".ip-galerij") || el.closest(".reveal, .rv, [class*='ip-'], [data-oc], .oc-uitslag"); };
  var sel = ".section .center > h2, .grid > .card:not(.reveal), .tools-grid > .tool-kaart, .chips, .places, .pc-fig, .kaart-grid, .cta, .stat, .steps3 > li:not(.reveal)";
  var vouw = window.innerHeight;
  var lijst = [].slice.call(document.querySelectorAll(sel)).filter(function (el) {
    return !buiten(el.parentElement || el) && el.getBoundingClientRect().top > vouw;
  });
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("rv-in"); io.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -6% 0px", threshold: 0 });
  lijst.forEach(function (el) {
    var p = el.parentElement, i = 0;
    if (p && (p.classList.contains("grid") || p.classList.contains("tools-grid") || p.classList.contains("steps3"))) {
      i = Math.min([].indexOf.call(p.children, el) % 4, 3);
    }
    if (i) el.style.setProperty("--rv-i", i);
    el.classList.add("rv");
    io.observe(el);
  });

  /* Cijfers in het feitenblok tellen op zodra ze in beeld komen. */
  var getal = /\d{1,3}(?:\.\d{3})+|\d+/g;
  var nl = function (n) { return n.toLocaleString("nl-NL"); };
  var tellers = [].slice.call(document.querySelectorAll(".feit-getal, .stat .n")).filter(function (el) {
    var t = el.textContent;
    return el.children.length === 0 && getal.test(t) && !/,\d|\b(1[89]|20)\d\d\b/.test(t.replace(/\./g, "")) &&
           el.getBoundingClientRect().top > vouw;
  });
  var tel = function (el) {
    var doel = el.textContent, delen = [], m;
    getal.lastIndex = 0;
    while ((m = getal.exec(doel))) delen.push({ i: m.index, s: m[0], n: parseInt(m[0].replace(/\./g, ""), 10) });
    if (!delen.length) return;
    el.style.minWidth = el.getBoundingClientRect().width + "px";
    el.classList.add("telt");
    var t0 = performance.now(), duur = 1100;
    (function stap(t) {
      var f = Math.min(1, (t - t0) / duur), e = 1 - Math.pow(1 - f, 3), uit = "", pos = 0;
      delen.forEach(function (d) {
        uit += doel.slice(pos, d.i) + (f < 1 ? nl(Math.round(d.n * e)) : d.s);
        pos = d.i + d.s.length;
      });
      el.textContent = uit + doel.slice(pos);
      if (f < 1) requestAnimationFrame(stap); else el.style.minWidth = "";
    })(t0);
  };
  if (tellers.length) {
    var tio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { tio.unobserve(e.target); setTimeout(function () { tel(e.target); }, 150); } });
    }, { threshold: 0.6 });
    tellers.forEach(function (el) { tio.observe(el); });
  }

  /* Zacht spotlicht onder de muis op kaarten (alleen bij een echte muis). */
  if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    document.addEventListener("pointermove", function (ev) {
      var k = ev.target.closest && ev.target.closest("a.card, .tool-kaart");
      if (!k) return;
      var r = k.getBoundingClientRect();
      k.style.setProperty("--mx", (ev.clientX - r.left) + "px");
      k.style.setProperty("--my", (ev.clientY - r.top) + "px");
    }, { passive: true });
  }

  /* Tools: uitkomst wipt even op als die verandert. */
  var uitkomst = ".calc-uit .bedrag, .hc-regel, .ohc-teller, .kk-kleurinfo, .sw-conclusie, [data-vc-uitkomst]";
  var tik = function (el) {
    el.classList.remove("ts-tik"); void el.offsetWidth; el.classList.add("ts-tik");
  };
  var gezien = new WeakMap();
  var mo = new MutationObserver(function (ms) {
    ms.forEach(function (m) {
      var n = m.target.nodeType === 1 ? m.target : m.target.parentElement;
      var kand = [n && n.closest && n.closest(uitkomst)];
      [].forEach.call(m.addedNodes, function (a) {
        if (a.nodeType !== 1) return;
        if (a.matches(uitkomst)) kand.push(a);
        else kand.push(a.querySelector(uitkomst));
      });
      kand.forEach(function (el) {
        if (!el || gezien.get(el) === el.textContent) return;
        gezien.set(el, el.textContent);
        tik(el);
      });
    });
  });
  document.querySelectorAll(".calc, .hc-pagina, .kk-tool, .ohc-quiz, .ohc-card, .sw-app, [data-verfcalc]").forEach(function (root) {
    mo.observe(root, { subtree: true, childList: true, characterData: true });
  });
})();
'''


# =========================================================================
# UITLIJNING (ronde 5) — nagelopen op 375, 768, 1024 en 1440 px.
# Los blok aan het eind, zodat het de eerdere regels gericht overschrijft.
# =========================================================================

STYLE_CSS += r'''
/* ---------- Header 901-1120 px: menu paste niet op één regel ---------- */
/* Logo kromp en menu-items braken af op twee regels; nu compacter en zonder afbreken. */
.logo{flex:0 0 auto}
.nav a{white-space:nowrap}
@media(min-width:901px) and (max-width:1120px){
  .header-in{gap:16px}
  .nav{gap:2px}
  .nav a{font-size:.9rem;padding:9px 9px}
  .nav a:not(.btn)::after{left:9px;right:9px}
  .nav .btn{margin-left:6px;padding:9px 14px}
}

/* ---------- Sticky CTA (mobiel): geen witte strook onder de footer ---------- */
/* De ruimte voor de knop zat als padding op body, dus wit onder de donkere footer.
   Nu zit die ruimte in de footer zelf. */
@media(max-width:760px){
  body{padding-bottom:0}
  .footer{padding-bottom:calc(26px + 76px + env(safe-area-inset-bottom))}
}

/* ---------- Gecentreerde kop: penseelstreek ook gecentreerd ---------- */
.center h1::after,h1.center::after{margin-left:auto;margin-right:auto}

/* ---------- Tools: vast beeldvlak 16:11 (klaar voor renders als <img>) ---------- */
.tool-beeld{height:auto;aspect-ratio:16/11;overflow:hidden}
.tool-beeld img{width:100%;height:100%;object-fit:cover;display:block}
.tool-beeld img{transition:transform .5s ease}
.tool-kaart:hover .tool-beeld img{transform:scale(1.05)}
@media (prefers-reduced-motion:reduce){.tool-beeld img{transition:none}.tool-kaart:hover .tool-beeld img{transform:none}}
/* De huidige SVG-illustraties (viewBox 160x110 = 16:11) vullen het vlak, met lucht rondom
   en bovenin ruimte voor het label. */
.tool-beeld > svg{width:100%;height:100%;display:block;padding:46px 15% 22px}
.tool-label{z-index:2}

/* ---------- Voorbeeldberekeningen (calculator) mobiel: rijen in plaats van losse cellen ---------- */
/* De tabelrijen worden op mobiel flexrijen; de zebra- en kopkleuren zaten op de cellen
   en vielen daardoor als losse vlakken. Nu kleurt de hele rij. */
@media(max-width:560px){
  .hc-vb-tabel td,.hc-vb-tabel th,.hc-vb-tabel tbody tr:hover td{background:transparent}
  .hc-vb-tabel tbody tr:nth-child(even){background:#fdfbf7}
  .hc-vb-tabel tfoot tr{background:linear-gradient(180deg,#fbf3e6,#f7ecdb);border-bottom:0}
  .hc-vb-tabel tfoot th{border:0}
}

/* ---------- Feitenblok met vier cijfers op tabletbreedte: 2x2 in plaats van 3+1 ---------- */
@media(min-width:561px) and (max-width:900px){
  .feiten:has(> .feit:nth-child(4):last-child){grid-template-columns:repeat(2,minmax(0,1fr))}
}

/* ---------- Inspiratie-teaser in lopende tekst: kop sluit aan op de bovenrand ---------- */
.prose .ip-teaser > h3:first-child{margin-top:0}

/* ---------- Galerij: illustraties (16:11) niet afsnijden in het 3:2-vlak ---------- */
.gl-illu .gl-open img.gl-svg{object-fit:contain}
'''

STYLE_CSS += r'''
/* ---------- Kaarten met een 'Lees meer'-link (kennisbank): link onderaan op één lijn ---------- */
.grid > div.card:has(> p:last-child > .go:only-child){display:flex;flex-direction:column}
.grid > div.card > p:last-child:has(> .go:only-child){margin-top:auto;margin-bottom:0;padding-top:4px}
'''

# --- LOKAAL (lokale gids top 10 en dienstuitleg; lokaal_top.py, dienst_uitleg.py) ---
STYLE_CSS += r'''
.lt-klimaat th{white-space:normal;text-transform:none;letter-spacing:0;font-size:.92rem;width:65%}
.lt-wijken td small{display:block;margin-top:4px;color:var(--muted,#6b5a45)}
.lt-wijken tbody th{white-space:nowrap;vertical-align:top;text-transform:none;letter-spacing:0}
.du-kort ul{margin:6px 0 0;padding-left:1.1em}
.du-kort li{margin:4px 0}
@media (max-width:640px){
  .lt-wijken thead{display:none}
  .lt-wijken,.lt-wijken tbody,.lt-wijken tr,.lt-wijken td{display:block;width:100%}
  .lt-wijken tr{padding:12px 14px;border-bottom:1px solid var(--line)}
  .lt-wijken td{padding:2px 0;border:0;white-space:normal}
  .lt-wijken tbody th{display:block;width:100%;padding:0 0 4px;border:0;font-size:1rem}
  .lt-wijken td.lt-naam{font-weight:750;font-size:1rem}
  .lt-wijken td.num{display:inline-block;width:auto;margin-right:14px;font-size:.9rem}
  .lt-wijken td.num::before{content:attr(data-label) ": ";font-weight:500;color:var(--muted,#6b5a45)}
  .du-tabel thead{display:none}
  .du-tabel,.du-tabel tbody,.du-tabel tr,.du-tabel td{display:block;width:100%}
  .du-tabel tr{padding:12px 14px;border-bottom:1px solid var(--line)}
  .du-tabel td{padding:3px 0;border:0;white-space:normal}
  .du-tabel td:first-child{font-weight:750;color:var(--ink)}
  .du-tabel td+td::before{content:attr(data-label) ": ";font-weight:650;color:var(--muted,#6b5a45)}
}
'''
# --- einde LOKAAL ---
from stijl_v2 import CSS as _STIJL_V2, FAVICON_SVG; STYLE_CSS += _STIJL_V2  # design v2: logo-favicon en site-brede opmaak

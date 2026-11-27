# -*- coding: utf-8 -*-
"""
Design v2 (november 2026): site-brede verfijning van de huisstijl.

Wordt onderaan assets.py met één regel aan STYLE_CSS geplakt en komt dus na alle
eerdere rondes. Alleen opmaak: geen nieuwe kleuren buiten het merk (bruin #3c290f,
oranje #f4820b, room/zand), geen animaties van layout-eigenschappen en alles wat
beweegt staat uit bij prefers-reduced-motion.

Wat het doet, kort:
- koppen strakker: zwaarder gewicht, kleinere regelafstand, oranje accent in de hero;
- pilknoppen met een zachte schaduw in plaats van de harde onderrand;
- header met groter, leesbaar logo en een rustige hover-streep in het menu;
- homepage-hero (.hero-v2): de foto is zichtbaar, tekst blijft goed leesbaar;
- kaarten, badges, tabellen, callouts en checklists één familie;
- een subtiel stippenraster op de zachte secties;
- vertrouwensbalk op mobiel als nette 2×2-tegels.

zachte_spaties(html) zorgt dat bedragen als "€300 – €660" niet middenin afbreken.
"""
import re

from merk_data import FAVICON_SVG  # noqa: F401  (assets.py geeft hem door aan build.py)

_BEDRAG = re.compile(r"(€\s?[\d.,]+) (–|-|tot) (€\s?[\d.,]+)")


def zachte_spaties(html):
    """'€300 – €660' → met harde spaties, zodat het bedrag op één regel blijft."""
    # Na een streepje mag een browser altijd afbreken, ook vóór een harde spatie.
    # De woordverbinder (U+2060) direct na het streepje verbiedt dat.
    return _BEDRAG.sub(lambda m: m.group(1) + "\u00a0" + m.group(2) + "\u2060\u00a0" + m.group(3), html)


CSS = r'''
/* =====================================================================
   DESIGN V2 (stijl_v2.py)
   ===================================================================== */
:root{
  --kop:-apple-system,BlinkMacSystemFont,"Segoe UI Variable Display","Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --zand:#f6efe3;
  --zand-2:#efe4d2;
  --radius:14px;
  --radius-lg:20px;
  --shadow:0 1px 2px rgba(60,41,15,.05),0 10px 30px -12px rgba(60,41,15,.16);
  --shadow-lg:0 2px 4px rgba(60,41,15,.05),0 28px 60px -20px rgba(60,41,15,.32);
  --raster:radial-gradient(rgba(60,41,15,.075) 1px,transparent 1.4px);
}

/* ---------- Typografie ---------- */
h1,h2,h3,.formcard h2,.feit-getal,.footer-cta-titel,.cta-midden-titel{font-family:var(--kop)}
h1{font-weight:800;letter-spacing:-.025em;line-height:1.08}
h2{font-weight:780;letter-spacing:-.02em;line-height:1.14}
h3{font-weight:720;letter-spacing:-.01em}
.lead{line-height:1.6}
/* penseelstreep onder een woord: lager, zodat hij de letters niet doorkruist */
.streep{background-position:0 100%;background-size:100% .34em;padding-bottom:.06em}

/* ---------- Knoppen: pil, zachte diepte ---------- */
.btn{border-radius:999px;font-weight:720;letter-spacing:.005em}
.btn-primary{background:linear-gradient(180deg,#f78d1f 0%,var(--accent) 55%,#ea7806 100%);
  box-shadow:0 1px 0 rgba(255,255,255,.35) inset,0 8px 20px -8px rgba(217,111,0,.75),0 2px 0 #c96600}
.btn-primary:hover{background:linear-gradient(180deg,#f0840f 0%,var(--accent-dark) 100%);
  box-shadow:0 1px 0 rgba(255,255,255,.3) inset,0 12px 24px -10px rgba(217,111,0,.85),0 2px 0 #b85e00}
.btn-dark{box-shadow:0 8px 20px -10px rgba(36,25,6,.7)}
.btn-ghost{border-width:1.5px}
.formcard .btn,.formcard button[type=submit]{border-radius:999px}

/* ---------- Header ---------- */
.header{background:rgba(255,255,255,.9);border-bottom-color:rgba(233,226,214,.8)}
.header-in{height:74px}
.logo img{height:36px}
.nav > a:not(.btn){position:relative}
@media(min-width:981px){
  .nav > a:not(.btn)::after{content:"";position:absolute;left:12%;right:12%;bottom:-4px;height:2px;border-radius:2px;
    background:var(--accent);transform:scaleX(0);transform-origin:50% 50%;transition:transform .2s ease}
  .nav > a:not(.btn):hover::after{transform:scaleX(1)}
  .nav .btn{padding:11px 20px}
}
@media(max-width:520px){.header-in{height:64px}.logo img{height:30px}}
.footer .logo img{height:38px}

/* ---------- Badges ---------- */
.badge{border-radius:999px;letter-spacing:.06em;font-size:.74rem;padding:6px 12px}
.badge:not(.badge-dark){background:linear-gradient(180deg,#fff7ec,#ffefdb);box-shadow:inset 0 0 0 1px rgba(217,111,0,.22)}

/* ---------- Zachte secties: warm zand met een stippenraster ---------- */
.soft{background-color:var(--bg-soft);background-image:var(--raster),linear-gradient(180deg,#faf5ec 0%,var(--bg-soft) 100%);
  background-size:22px 22px,100% 100%}

/* ---------- Kaarten ---------- */
.card{border-radius:var(--radius);border-color:rgba(233,226,214,.9);box-shadow:0 1px 2px rgba(60,41,15,.04)}
a.card:hover,.card:has(.go):hover{box-shadow:var(--shadow);border-color:#e3d5bf}
.card .foto img{border-radius:12px}

/* ---------- Formulierkaart ---------- */
.formcard{border-radius:var(--radius-lg);border:1px solid rgba(233,226,214,.9)}
.choice label{border-radius:12px}
.choice label:has(input:checked){box-shadow:0 0 0 3px rgba(244,130,11,.16)}
.steps div{height:6px}

/* ---------- Callouts en checklists ---------- */
.callout{border-radius:var(--radius);border-left-width:0;box-shadow:inset 4px 0 0 var(--accent),0 1px 2px rgba(60,41,15,.04)}
.checklist li::before{content:"";top:.28em;width:18px;height:18px;border-radius:50%;
  background:#e4f4ec url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M4 8.4l2.6 2.5L12 5.4' fill='none' stroke='%230f8a5f' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/14px no-repeat}

/* ---------- Tabellen ---------- */
th{font-family:var(--kop);letter-spacing:.01em}
td{font-variant-numeric:tabular-nums}

/* ---------- Kennisbank en lange teksten: rustiger ritme ---------- */
.prose p,.prose li{line-height:1.72}
.prose h2{margin-top:2.4em}
.prose h3{margin-top:1.8em}
.prose figure.foto img{border-radius:var(--radius-lg)}

/* ---------- Homepage-hero v2 ---------- */
.hero-v2{background:#21170a}
.hero-v2 .hero-bg{object-position:72% 38%}
.hero-v2::before{background:
  linear-gradient(90deg,rgba(28,19,5,.94) 0%,rgba(28,19,5,.86) 34%,rgba(28,19,5,.42) 62%,rgba(28,19,5,.28) 100%),
  linear-gradient(0deg,rgba(28,19,5,.55) 0%,transparent 30%)}
.hero-v2 .hero-in{padding-top:80px;padding-bottom:88px;align-items:center}
.hero-v2 h1{font-size:clamp(2.15rem,5vw,3.7rem);max-width:13ch}
.hero-v2 h1 .hero-accent{color:#ffb766}
.hero-v2 .lead{font-size:1.18rem;max-width:44ch;color:#f1e7d8}
.hero-v2 .hero-usps{margin:24px 0 28px}
.hero-v2 .hero-usps li{font-weight:500}
.hero-routes{display:flex;flex-wrap:wrap;gap:10px;margin:0;padding:0;list-style:none}
.hero-routes li{margin:0}
.hero-routes a{display:inline-flex;align-items:center;gap:9px;padding:10px 16px 10px 12px;border-radius:999px;
  background:rgba(255,255,255,.08);box-shadow:inset 0 0 0 1px rgba(255,255,255,.22);color:#fff;font-weight:650;font-size:.93rem;
  text-decoration:none;backdrop-filter:blur(6px);transition:background .15s ease,box-shadow .15s ease}
.hero-routes a:hover{background:rgba(255,255,255,.16);box-shadow:inset 0 0 0 1px rgba(255,183,102,.6);text-decoration:none}
.hero-routes svg{width:26px;height:26px;padding:5px;border-radius:50%;background:rgba(244,130,11,.95);color:#fff;flex:0 0 26px}
.hero-routes .pijl{opacity:.7;margin-left:2px}
.hero-v2 .formcard{border:0;border-top:4px solid var(--accent)}
@media(max-width:920px){
  .hero-v2::before{background:linear-gradient(180deg,rgba(28,19,5,.78) 0%,rgba(28,19,5,.9) 40%,rgba(28,19,5,.97) 100%)}
  .hero-v2 .hero-in{padding-top:40px;padding-bottom:44px}
  .hero-v2 h1{max-width:none}
  .hero-v2 .lead{font-size:1.06rem}
  .hero-routes{display:none}
}
@media(max-width:520px){
  .hero-v2 .hero-usps{margin:18px 0 4px}
  .hero-v2 .hero-usps li{font-size:.95rem;margin-bottom:8px}
}

/* ---------- Vertrouwensbalk ---------- */
.trustbar li{font-size:.92rem}
@media(max-width:900px){
  .trustbar ul{gap:10px;padding:14px 0}
  .trustbar li{background:var(--bg-soft);border:1px solid var(--line);border-radius:12px;padding:10px 12px;align-items:center;min-height:62px}
}
@media(max-width:420px){
  .trustbar li{gap:9px;padding:9px 10px;font-size:.84rem;line-height:1.3}
  .trustbar svg{flex-basis:30px;width:30px;height:30px;padding:7px}
}

@media (prefers-reduced-motion:reduce){
  .nav > a:not(.btn)::after,.hero-routes a{transition:none}
}
'''

CSS += r'''
/* ---------- Prijscallout: rij losse kostenlinks als rustige chips ---------- */
.callout-prijs p:has(> a + a + a){font-size:0 !important;display:flex;flex-wrap:wrap;gap:6px;margin-top:12px !important}
.callout-prijs p:has(> a + a + a) > a{font-size:.82rem;line-height:1.3;font-weight:600;color:#7a3f00;text-decoration:none;
  background:rgba(255,255,255,.75);border:1px solid rgba(217,111,0,.22);border-radius:999px;padding:5px 11px}
.callout-prijs p:has(> a + a + a) > a:hover{background:#fff;border-color:var(--accent);text-decoration:none}
'''

CSS += r'''
/* ---------- Contrast: donkere tekst op de oranje knop (AA, ±6,8:1) ----------
   Wit op oranje haalde maar 2,4–2,6:1. De header-knop deed het al zo. */
.btn.btn-primary,.btn.btn-primary:hover,.btn.btn-primary:focus,.dark a.btn-primary,.formcard .btn-primary{color:var(--ink)}
.btn.btn-primary svg{color:inherit}
'''

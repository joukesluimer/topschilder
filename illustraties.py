# -*- coding: utf-8 -*-
"""
Sfeerbeelden in SVG.

Waarom SVG en geen foto's: dit zijn vectorbeelden van een paar kilobyte die
oneindig scherp blijven, in jouw huisstijlkleuren staan en geen enkel
licentierisico geven. Ze worden rechtstreeks in de HTML gezet, dus ze kosten
geen extra laadverzoek.

Wil je later echte foto's? Zie FOTO_SLOTS onderaan — dan is het één regel per
plek om een illustratie te vervangen door een <img>.
"""

# huisstijl, gelijk aan STYLE_CSS in assets.py
BRUIN      = "#3c290f"
BRUIN_ZACHT= "#6b5024"
ACCENT     = "#f4820b"
ACCENT_D   = "#d96f00"
CREME      = "#faf7f1"
LICHT      = "#efe7d8"
WIT        = "#ffffff"
GLAS       = "#cfe0ea"
GLAS_D     = "#a9c6d6"


def _wrap(inner, vb="0 0 640 420", extra=""):
    return (f'<svg class="illu" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" aria-hidden="true" preserveAspectRatio="xMidYMid slice"{extra}>{inner}</svg>')


# ---------------------------------------------------------------------------
# Hero: rijtjeswoning met schilder op een ladder
# ---------------------------------------------------------------------------

def hero():
    return _wrap(f'''
<rect width="640" height="420" fill="{CREME}"/>
<circle cx="520" cy="86" r="46" fill="{ACCENT}" opacity=".14"/>
<path d="M0 358h640v62H0z" fill="{LICHT}"/>

<!-- linkerbuur, op de achtergrond -->
<path d="M18 150 118 92l100 58v208H18z" fill="{LICHT}"/>
<rect x="48" y="196" width="46" height="54" rx="4" fill="{GLAS}"/>
<rect x="140" y="196" width="46" height="54" rx="4" fill="{GLAS}"/>

<!-- hoofdwoning -->
<path d="M196 148 356 44l160 104v210H196z" fill="{WIT}" stroke="{BRUIN}" stroke-width="6" stroke-linejoin="round"/>
<path d="M180 152 356 38l176 114" fill="none" stroke="{BRUIN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>

<!-- kozijnen: het werk zelf, in accentkleur -->
<g stroke="{ACCENT}" stroke-width="7">
  <rect x="238" y="184" width="74" height="80" rx="3" fill="{GLAS}"/>
  <rect x="400" y="184" width="74" height="80" rx="3" fill="{GLAS}"/>
  <path d="M275 184v80M238 224h74M437 184v80M400 224h74" stroke-width="5"/>
</g>
<rect x="316" y="272" width="80" height="86" rx="3" fill="{BRUIN_ZACHT}" stroke="{ACCENT}" stroke-width="7"/>
<circle cx="382" cy="316" r="5" fill="{ACCENT}"/>

<!-- dakkapel -->
<path d="M300 108h112v40H300z" fill="{WIT}" stroke="{BRUIN}" stroke-width="6"/>
<rect x="330" y="118" width="52" height="30" rx="3" fill="{GLAS_D}"/>

<!-- ladder -->
<g stroke="{BRUIN}" stroke-width="7" stroke-linecap="round">
  <path d="M508 358 470 168M556 358 518 168"/>
  <path d="M480 214h40M486 250h40M492 286h40M498 322h40" stroke-width="6"/>
</g>

<!-- schilder -->
<g>
  <circle cx="472" cy="150" r="22" fill="{BRUIN}"/>
  <path d="M448 150a24 24 0 0 1 48 0z" fill="{ACCENT}"/>
  <path d="M456 172h34l10 62h-54z" fill="{ACCENT}"/>
  <path d="M490 186l34-26" stroke="{BRUIN}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <rect x="514" y="132" width="46" height="16" rx="8" fill="{ACCENT_D}"/>
  <path d="M528 148v14" stroke="{BRUIN}" stroke-width="6" stroke-linecap="round"/>
</g>

<!-- verfemmer -->
<path d="M120 322h54l-7 36h-40z" fill="{ACCENT}"/>
<path d="M120 322h54" stroke="{BRUIN}" stroke-width="6" stroke-linecap="round"/>
<path d="M128 322a19 19 0 0 1 38 0" fill="none" stroke="{BRUIN}" stroke-width="4"/>
''')


# ---------------------------------------------------------------------------
# Per dienst
# ---------------------------------------------------------------------------

def binnenschilderwerk():
    return _wrap(f'''
<rect width="640" height="420" fill="{CREME}"/>
<path d="M0 340h640v80H0z" fill="{LICHT}"/>
<rect x="60" y="40" width="330" height="300" fill="{WIT}"/>
<path d="M60 40h330v300" fill="none" stroke="{BRUIN}" stroke-width="5"/>
<!-- half geverfde muur -->
<rect x="60" y="40" width="176" height="300" fill="{ACCENT}" opacity=".2"/>
<path d="M236 40v300" stroke="{ACCENT}" stroke-width="6" stroke-dasharray="14 10"/>
<!-- plint -->
<rect x="60" y="326" width="330" height="14" fill="{BRUIN_ZACHT}"/>
<!-- deur -->
<rect x="430" y="120" width="122" height="220" rx="4" fill="{WIT}" stroke="{BRUIN}" stroke-width="6"/>
<rect x="450" y="146" width="82" height="76" rx="3" fill="{CREME}" stroke="{BRUIN}" stroke-width="4"/>
<rect x="450" y="240" width="82" height="76" rx="3" fill="{CREME}" stroke="{BRUIN}" stroke-width="4"/>
<circle cx="442" cy="234" r="6" fill="{ACCENT}"/>
<!-- roller op steel -->
<g transform="rotate(-24 250 200)">
  <rect x="196" y="150" width="104" height="30" rx="14" fill="{ACCENT}"/>
  <path d="M300 165h30" stroke="{BRUIN}" stroke-width="9" stroke-linecap="round"/>
  <path d="M330 165v120" stroke="{BRUIN}" stroke-width="11" stroke-linecap="round"/>
</g>
<!-- verfblik -->
<path d="M96 292h60l-8 48h-44z" fill="{ACCENT_D}"/>
<path d="M96 292h60" stroke="{BRUIN}" stroke-width="6" stroke-linecap="round"/>
''')


def buitenschilderwerk():
    return _wrap(f'''
<rect width="640" height="420" fill="{CREME}"/>
<path d="M0 352h640v68H0z" fill="{LICHT}"/>
<rect x="70" y="60" width="500" height="292" fill="{WIT}" stroke="{BRUIN}" stroke-width="6"/>
<!-- baksteenritme -->
<g stroke="{LICHT}" stroke-width="3">
  <path d="M70 118h500M70 176h500M70 234h500M70 292h500"/>
</g>
<!-- kozijnen -->
<g stroke="{ACCENT}" stroke-width="8">
  <rect x="118" y="108" width="116" height="112" rx="3" fill="{GLAS}"/>
  <rect x="406" y="108" width="116" height="112" rx="3" fill="{GLAS}"/>
  <path d="M176 108v112M118 164h116M464 108v112M406 164h116" stroke-width="5"/>
</g>
<!-- voordeur -->
<rect x="266" y="196" width="108" height="156" rx="3" fill="{BRUIN_ZACHT}" stroke="{ACCENT}" stroke-width="8"/>
<circle cx="356" cy="278" r="6" fill="{ACCENT}"/>
<!-- boeideel dat geschilderd wordt -->
<rect x="70" y="60" width="500" height="22" fill="{ACCENT}"/>
<!-- kwast -->
<g transform="rotate(18 540 120)">
  <rect x="516" y="60" width="34" height="52" rx="5" fill="{BRUIN}"/>
  <rect x="520" y="106" width="26" height="34" rx="3" fill="{ACCENT_D}"/>
  <path d="M533 34v28" stroke="{BRUIN}" stroke-width="10" stroke-linecap="round"/>
</g>
''')


def houtrot():
    return _wrap(f'''
<rect width="640" height="420" fill="{CREME}"/>
<rect x="80" y="60" width="480" height="300" rx="6" fill="{WIT}" stroke="{BRUIN}" stroke-width="6"/>
<rect x="122" y="100" width="396" height="180" rx="4" fill="{GLAS}" stroke="{ACCENT}" stroke-width="8"/>
<path d="M320 100v180M122 190h396" stroke="{ACCENT}" stroke-width="6"/>
<!-- onderdorpel met aantasting -->
<rect x="104" y="292" width="432" height="42" rx="4" fill="{BRUIN_ZACHT}"/>
<path d="M150 292c18 26 34 6 54 26s34-4 52 16h-118z" fill="#8a6a34"/>
<path d="M150 292c18 26 34 6 54 26s34-4 52 16" fill="none" stroke="{ACCENT_D}" stroke-width="5" stroke-linecap="round"/>
<!-- markering van de reparatieplek -->
<circle cx="204" cy="312" r="62" fill="none" stroke="{ACCENT}" stroke-width="5" stroke-dasharray="12 9"/>
<path d="M266 258l70-58" stroke="{ACCENT}" stroke-width="5" stroke-linecap="round"/>
<circle cx="344" cy="194" r="7" fill="{ACCENT}"/>
<!-- beitel -->
<g transform="rotate(38 470 300)">
  <rect x="452" y="238" width="30" height="60" rx="6" fill="{BRUIN}"/>
  <path d="M452 298h30l-15 30z" fill="{ACCENT_D}"/>
</g>
''')


def spuitwerk():
    return _wrap(f'''
<rect width="640" height="420" fill="{CREME}"/>
<path d="M0 348h640v72H0z" fill="{LICHT}"/>
<!-- keukenfronten -->
<g stroke="{BRUIN}" stroke-width="5">
  <rect x="70" y="70" width="130" height="120" rx="4" fill="{WIT}"/>
  <rect x="210" y="70" width="130" height="120" rx="4" fill="{WIT}"/>
  <rect x="70" y="200" width="130" height="146" rx="4" fill="{ACCENT}" opacity=".92"/>
  <rect x="210" y="200" width="130" height="146" rx="4" fill="{ACCENT}" opacity=".92"/>
</g>
<g fill="{BRUIN}">
  <rect x="150" y="122" width="40" height="7" rx="3.5"/>
  <rect x="290" y="122" width="40" height="7" rx="3.5"/>
  <rect x="150" y="252" width="40" height="7" rx="3.5"/>
  <rect x="290" y="252" width="40" height="7" rx="3.5"/>
</g>
<!-- spuitnevel -->
<g fill="{ACCENT}" opacity=".5">
  <circle cx="392" cy="150" r="5"/><circle cx="414" cy="132" r="4"/><circle cx="410" cy="172" r="3.5"/>
  <circle cx="436" cy="152" r="5"/><circle cx="440" cy="118" r="3"/><circle cx="452" cy="186" r="4"/>
  <circle cx="470" cy="142" r="3"/><circle cx="386" cy="196" r="3"/>
</g>
<!-- spuitpistool -->
<g>
  <path d="M496 128h84v40h-84z" fill="{BRUIN}"/>
  <path d="M496 148l-32 10 32 10z" fill="{BRUIN}"/>
  <path d="M540 168l-14 74h44l-12-74z" fill="{BRUIN_ZACHT}"/>
  <rect x="524" y="88" width="46" height="42" rx="6" fill="{ACCENT_D}"/>
  <path d="M580 140h30" stroke="{BRUIN}" stroke-width="9" stroke-linecap="round"/>
</g>
''')


def behangen():
    return _wrap(f'''
<rect width="640" height="420" fill="{CREME}"/>
<path d="M0 346h640v74H0z" fill="{LICHT}"/>
<rect x="60" y="50" width="520" height="296" fill="{WIT}" stroke="{BRUIN}" stroke-width="5"/>
<!-- banen behang -->
<rect x="60" y="50" width="128" height="296" fill="{ACCENT}" opacity=".18"/>
<rect x="188" y="50" width="128" height="296" fill="{ACCENT}" opacity=".3"/>
<path d="M188 50v296M316 50v296" stroke="{ACCENT}" stroke-width="3"/>
<!-- patroon -->
<g fill="{ACCENT}" opacity=".55">
  <circle cx="124" cy="112" r="9"/><circle cx="124" cy="204" r="9"/><circle cx="124" cy="296" r="9"/>
  <circle cx="252" cy="158" r="9"/><circle cx="252" cy="250" r="9"/><circle cx="252" cy="66" r="9"/>
</g>
<!-- baan die wordt afgerold -->
<path d="M316 50h128v230l-128 66z" fill="{WIT}" stroke="{BRUIN}" stroke-width="5"/>
<path d="M444 280l-128 66" stroke="{BRUIN}" stroke-width="5"/>
<!-- rol -->
<g>
  <ellipse cx="510" cy="296" rx="34" ry="34" fill="{ACCENT}"/>
  <ellipse cx="510" cy="296" rx="12" ry="12" fill="{CREME}"/>
  <path d="M476 296c0-18 15-34 34-34" fill="none" stroke="{ACCENT_D}" stroke-width="5"/>
</g>
<!-- plakspaan -->
<g transform="rotate(-30 400 150)">
  <rect x="366" y="108" width="76" height="16" rx="4" fill="{BRUIN}"/>
  <rect x="394" y="124" width="20" height="46" rx="6" fill="{BRUIN_ZACHT}"/>
</g>
''')


def zakelijk():
    return _wrap(f'''
<rect width="640" height="420" fill="{CREME}"/>
<path d="M0 356h640v64H0z" fill="{LICHT}"/>
<!-- kantoorpand -->
<rect x="88" y="52" width="250" height="304" fill="{WIT}" stroke="{BRUIN}" stroke-width="6"/>
<g fill="{GLAS}" stroke="{ACCENT}" stroke-width="4">
  <rect x="116" y="82" width="82" height="58" rx="3"/><rect x="228" y="82" width="82" height="58" rx="3"/>
  <rect x="116" y="164" width="82" height="58" rx="3"/><rect x="228" y="164" width="82" height="58" rx="3"/>
  <rect x="116" y="246" width="82" height="58" rx="3"/><rect x="228" y="246" width="82" height="58" rx="3"/>
</g>
<!-- tweede pand -->
<rect x="356" y="128" width="196" height="228" fill="{WIT}" stroke="{BRUIN}" stroke-width="6"/>
<g fill="{GLAS_D}">
  <rect x="382" y="158" width="60" height="46" rx="3"/><rect x="466" y="158" width="60" height="46" rx="3"/>
  <rect x="382" y="226" width="60" height="46" rx="3"/><rect x="466" y="226" width="60" height="46" rx="3"/>
</g>
<rect x="424" y="294" width="60" height="62" rx="3" fill="{BRUIN_ZACHT}"/>
<!-- steiger -->
<g stroke="{ACCENT}" stroke-width="6" fill="none" stroke-linecap="round">
  <path d="M78 356V72M348 356V72"/>
  <path d="M78 130h270M78 208h270M78 286h270"/>
</g>
<rect x="88" y="196" width="250" height="12" fill="{ACCENT}" opacity=".55"/>
''')


ILLUSTRATIES = {
    "hero": hero,
    "binnenschilderwerk": binnenschilderwerk,
    "buitenschilderwerk": buitenschilderwerk,
    "houtrot-reparatie": houtrot,
    "spuitwerk": spuitwerk,
    "behangen": behangen,
    "zakelijk-schilderwerk": zakelijk,
}


def illustratie(sleutel):
    fn = ILLUSTRATIES.get(sleutel)
    return fn() if fn else ""


# ---------------------------------------------------------------------------
# Voor/na — verweerde gevel tegenover een verse
# ---------------------------------------------------------------------------

def _gevel(vers):
    kozijn = ACCENT if vers else "#9c8f78"
    glas = GLAS if vers else "#b9c4c9"
    muur = WIT if vers else "#eae4d8"
    deur = BRUIN_ZACHT if vers else "#7d7159"
    vlek = "" if vers else f'''
      <path d="M120 250c26 12 40-8 66 6s34-6 58 10" fill="none" stroke="#a99878" stroke-width="7" opacity=".7"/>
      <path d="M330 96c30 8 44 26 74 22" fill="none" stroke="#a99878" stroke-width="6" opacity=".6"/>
      <circle cx="470" cy="300" r="26" fill="#bdae90" opacity=".45"/>'''
    return f'''
<rect width="640" height="360" fill="{CREME}"/>
<path d="M0 316h640v44H0z" fill="{LICHT}"/>
<rect x="60" y="48" width="520" height="268" fill="{muur}" stroke="{BRUIN}" stroke-width="6"/>
<rect x="60" y="48" width="520" height="20" fill="{kozijn}"/>
<g stroke="{kozijn}" stroke-width="8">
  <rect x="108" y="98" width="116" height="106" rx="3" fill="{glas}"/>
  <rect x="416" y="98" width="116" height="106" rx="3" fill="{glas}"/>
  <path d="M166 98v106M108 151h116M474 98v106M416 151h116" stroke-width="5"/>
</g>
<rect x="266" y="176" width="108" height="140" rx="3" fill="{deur}" stroke="{kozijn}" stroke-width="8"/>
<circle cx="356" cy="248" r="6" fill="{kozijn}"/>{vlek}'''


def voor_na():
    """Interactieve schuif: sleep om het verschil te zien."""
    return f'''<div class="vn" data-vn>
  <svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Gevel voor het schilderwerk">{_gevel(False)}</svg>
  <div class="vn-na"><svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Gevel na het schilderwerk">{_gevel(True)}</svg></div>
  <span class="vn-label l">Voor</span>
  <span class="vn-label r">Na</span>
  <div class="vn-greep" role="slider" tabindex="0" aria-label="Sleep om voor en na te vergelijken" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50"></div>
</div>'''


# ---------------------------------------------------------------------------
# Later echte foto's gebruiken?
# ---------------------------------------------------------------------------

FOTO_SLOTS = """
Elke illustratie is te vervangen door een foto. Zet het bestand in
site/assets/foto/ en vervang in build.py de aanroep, bijvoorbeeld:

    illustratie("buitenschilderwerk")
->  '<img class="illu" src="/assets/foto/gevel-lelystad.jpg" width="640" height="420"
     alt="Geschilderde kozijnen aan een woning in Lelystad" loading="lazy">'

Waar foto's het meest opleveren, in volgorde:
  1. Hero op de homepage        — een echte klus zegt meer dan welke illustratie ook
  2. De zes dienstpagina's      — binnen, buiten, houtrot, spuitwerk, behang, zakelijk
  3. Voor/na op buitenwerk      — twee foto's van dezelfde gevel, zelfde standpunt

Vraag ze op bij de schilders die je aansluit: zij hebben mappen vol
opleveringsfoto's en geven die meestal graag, want hun werk komt in beeld.
Laat wel even vastleggen dat je ze mag gebruiken.
"""

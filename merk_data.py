# -*- coding: utf-8 -*-
"""
Logo van Topschilder als SVG — design v2 (november 2026).

Het logo wordt hier opgebouwd uit lijnen en bogen; er zit geen lettertype in.
Daardoor is het overal scherp, licentievrij en klein (± 3 kB).

- Beeldmerk "roller-T": de rollerkop is de dwarsbalk van een T, de steel de poot.
  Bruin vlak (#3c290f), oranje roller (#f4820b), roomkleurige beugel.
- Woordmerk: eigen ronde, geometrische letters met een vaste lijndikte.
  "topschilder" in bruin, ".nl" in oranje.
- Favicon: apart getekend op een raster van 16×16, zodat elke rand op een hele
  pixel valt en hij op 16 px scherp blijft.

Het oude logo (het nagetekende PNG met poppetje) staat in de git-geschiedenis.
De og-image (merk/og-image.png) wordt gemaakt met `python3 merk_maken.py`.
"""
import math

BRUIN = "#3c290f"
ORANJE = "#f4820b"
ROOM = "#fbe7cc"

W = 14            # lijndikte
ASC, XH, MID, BASE, DESC = 23, 51, 72, 93, 121
R = 21


def _f(v):
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s


def letter(ch, x):
    """Geeft (paden, breedte) voor één letter; x = linker inktrand."""
    s = x + 7
    if ch == "t":
        c = x + 15
        d = f"M{c} 30V80A13 13 0 0 0 {c+13} {BASE}H{c+19}M{c-8} {XH}H{c+18}"
        return [d], 41
    if ch == "o":
        c = x + 28
        return [f"M{c-R} {MID}a{R} {R} 0 1 0 {2*R} 0a{R} {R} 0 1 0 {-2*R} 0Z"], 56
    if ch == "p":
        c = s + R
        return [f"M{s} {XH}V{DESC}", f"M{c-R} {MID}a{R} {R} 0 1 0 {2*R} 0a{R} {R} 0 1 0 {-2*R} 0Z"], 56
    if ch == "d":
        c = x + 28
        return [f"M{c+R} {ASC}V{BASE}", f"M{c-R} {MID}a{R} {R} 0 1 0 {2*R} 0a{R} {R} 0 1 0 {-2*R} 0Z"], 56
    if ch == "s":
        d = (f"M{x+36} 58C{x+31} 52.5 {x+26.5} 51 {x+21.5} 51C{x+12.5} 51 {x+7} 55.5 {x+7} 62"
             f"C{x+7} 69.5 {x+14} 71 {x+22} 72.2C{x+31} 73.5 {x+37} 76 {x+37} 83"
             f"C{x+37} 89.5 {x+31} 93 {x+22} 93C{x+15} 93 {x+9.5} 90.5 {x+6} 86")
        return [d], 44
    if ch == "c":
        c = x + 28
        a = math.radians(42)
        dx, dy = R * math.cos(a), R * math.sin(a)
        return [f"M{_f(c+dx)} {_f(MID-dy)}A{R} {R} 0 1 0 {_f(c+dx)} {_f(MID+dy)}"], 51
    if ch == "e":
        c = x + 28
        a = math.radians(42)
        dx, dy = R * math.cos(a), R * math.sin(a)
        return [f"M{c-R} {MID}H{c+R}A{R} {R} 0 1 0 {_f(c+dx)} {_f(MID+dy)}"], 56
    if ch == "h":
        return [f"M{s} {ASC}V{BASE}M{s} {BASE}V{MID}a{R} {R} 0 0 1 {2*R} 0V{BASE}"], 56
    if ch == "n":
        return [f"M{s} {XH}V{BASE}M{s} {BASE}V{MID}a{R} {R} 0 0 1 {2*R} 0V{BASE}"], 56
    if ch == "i":
        return [f"M{s} {XH}V{BASE}", ("stip", s, 26)], 14
    if ch == "l":
        return [f"M{s} {ASC}V{BASE}"], 14
    if ch == "r":
        return [f"M{s} {XH}V{BASE}M{s} {BASE}V{MID}a{R} {R} 0 0 1 {R} {-R}H{s+25}"], 39
    if ch == ".":
        return [("stip", x + 8.5, BASE - 1.5)], 17
    raise KeyError(ch)


# spatiëring tussen inktranden (optisch bijgesteld)
GAP = {"to": 6, "op": 8, "ps": 8, "sc": 8, "ch": 8, "hi": 10, "il": 11, "ld": 9,
       "de": 8, "er": 8, "r.": 4, ".n": 6, "nl": 10}


def woord(tekst, x0, kleur):
    paden, stippen = [], []
    x = x0
    for i, ch in enumerate(tekst):
        p, w = letter(ch, x)
        for d in p:
            if isinstance(d, tuple):
                stippen.append((d[1], d[2]))
            else:
                paden.append(d)
        if i + 1 < len(tekst):
            x += w + GAP.get(ch + tekst[i + 1], 9)
        else:
            x += w
    lijn = (f'<path fill="none" stroke="{kleur}" stroke-width="{W}" stroke-linecap="round" '
            f'stroke-linejoin="round" d="{"".join(paden)}"/>')
    stip = "".join(f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="8.5" fill="{kleur}"/>' for cx, cy in stippen)
    return lijn + stip, x


def beeldmerk_inhoud(x=0, y=0, bg=BRUIN, roller=ORANJE, draad=ROOM):
    """Roller-T: de rollerkop is de dwarsbalk van een T, de steel de poot."""
    return (f'<g transform="translate({x} {y})">'
            f'<rect width="112" height="112" rx="27" fill="{bg}"/>'
            f'<path d="M80 36H90V58H50V64" fill="none" stroke="{draad}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<rect x="18" y="24" width="64" height="24" rx="12" fill="{roller}"/>'
            f'<path d="M50 71V90" stroke="{roller}" stroke-width="16" stroke-linecap="round"/>'
            f'</g>')


def logo(wit=False):
    tk = "#ffffff" if wit else BRUIN
    nl = "#ffb55e" if wit else ORANJE
    merk = beeldmerk_inhoud(0, 16, bg=("#ffffff" if wit else BRUIN), draad=(BRUIN if wit else ROOM))
    w1, x = woord("topschilder", 140, tk)
    w2, x = woord(".nl", x + 4, nl)
    breed = int(math.ceil(x + 2))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {breed} 144" role="img" '
            f'aria-label="Topschilder.nl">{merk}{w1}{w2}</svg>')


def beeldmerk():
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 112 112">{beeldmerk_inhoud()}</svg>'


def favicon():
    """Op een raster van 16×16: elke rand valt op een hele pixel."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">'
            f'<rect width="16" height="16" rx="3.5" fill="{BRUIN}"/>'
            f'<rect x="2" y="3" width="10" height="4" rx="2" fill="{ORANJE}"/>'
            f'<path d="M12 4.5h1.5v4H7.5" fill="none" stroke="{ROOM}" stroke-width="1"/>'
            f'<rect x="6" y="9" width="3" height="5" rx="1.5" fill="{ORANJE}"/>'
            '</svg>')


LOGO_SVG = logo()
LOGO_WIT_SVG = logo(wit=True)
BEELDMERK_SVG = beeldmerk()
FAVICON_SVG = favicon()

# afmetingen voor <img width/height> (voorkomt layout shift)
LOGO_BREED, LOGO_HOOG = (int(v) for v in LOGO_SVG.split('viewBox="0 0 ')[1].split('"')[0].split())

BESTANDEN = {
    "logo.svg": LOGO_SVG,
    "logo-wit.svg": LOGO_WIT_SVG,
    "beeldmerk.svg": BEELDMERK_SVG,
}

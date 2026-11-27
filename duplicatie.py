# -*- coding: utf-8 -*-
"""Meet duplicatie tussen lokale pagina's in de gebouwde site/ (los te draaien na build.py).

Drie groepen:
  plaats         /schilder/<plaats>/                (35 pagina's, onderling vergeleken)
  plaats-dienst  /schilder/<plaats>/<dienst>/       (per dienst onderling vergeleken)
  dienst         /schilderwerk/<dienst>/            (6 pagina's, onderling vergeleken)

Per pagina:
  - uniek%     aandeel woord-8-grammen dat op geen andere pagina van de groep staat
  - duplicatie 100 - uniek%
  - max-overlap het hoogste Jaccard-percentage met één andere pagina uit de groep

Plaatsnamen, gemeenten en provincies worden vervangen door X en getallen door 0, zodat
'Schilder in Zwolle' en 'Schilder in Kampen' niet als uniek tellen (zelfde regels als uniek.py).
Header, footer, nav, scripts en styles tellen niet mee.

Met --met-cijfers blijven getallen staan. Dan telt een zin met een echt lokaal cijfer (bouwjaar,
aantal woningen, windsnelheid) als uniek. Zoekmachines vergelijken teksten ook mét cijfers.

Gebruik: python3 duplicatie.py [--detail] [--met-cijfers]
"""
import os
import re
import sys
import html as H
from collections import Counter

from data import PLAATSEN, DIENSTEN

ROOT = os.path.dirname(os.path.abspath(__file__))
DETAIL = "--detail" in sys.argv
MET_CIJFERS = "--met-cijfers" in sys.argv
namen = sorted({p["naam"] for p in PLAATSEN} | {p["gemeente"] for p in PLAATSEN}
               | {p["provincie"] for p in PLAATSEN}, key=len, reverse=True)
naam_re = re.compile("|".join(re.escape(n) for n in namen))


def woorden(pad):
    h = open(os.path.join(ROOT, "site", pad.strip("/"), "index.html"), encoding="utf-8").read()
    h = re.sub(r"<(script|style|header|footer|nav)\b.*?</\1>", " ", h, flags=re.S)
    h = H.unescape(re.sub(r"<[^>]+>", " ", h))
    h = naam_re.sub("X", h)
    if not MET_CIJFERS:
        h = re.sub(r"\d[\d.,]*", "0", h)
    return re.findall(r"\w+", h.lower())


def grams(w, n=8):
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def meet(paden):
    """paden: {label: pad} -> {label: (uniek%, max_overlap%, woorden)}"""
    w = {k: woorden(v) for k, v in paden.items()}
    g = {k: grams(v) for k, v in w.items()}
    tel = Counter(x for s in g.values() for x in s)
    uit = {}
    for k, s in g.items():
        uniek = 100 * sum(1 for x in s if tel[x] == 1) / max(1, len(s))
        mx = max((100 * len(s & t) / max(1, len(s | t)) for j, t in g.items() if j != k), default=0)
        uit[k] = (uniek, mx, len(w[k]))
    return uit


def samenvatting(naam, res, filt=None):
    rij = {k: v for k, v in res.items() if not filt or k in filt}
    if not rij:
        return
    u = sum(v[0] for v in rij.values()) / len(rij)
    m = sum(v[1] for v in rij.values()) / len(rij)
    wd = sum(v[2] for v in rij.values()) / len(rij)
    print(f"{naam:34s} uniek {u:5.1f}%  duplicatie {100 - u:5.1f}%  max-overlap {m:5.1f}%  "
          f"gem. {wd:5.0f} woorden  ({len(rij)} pagina's)")
    if DETAIL:
        for k, v in sorted(rij.items(), key=lambda x: x[1][0]):
            print(f"    {k:32s} uniek {v[0]:5.1f}%  max-overlap {v[1]:5.1f}%  {v[2]} woorden")


TOP10 = None
try:
    from lokaal_top import TOP10  # noqa: E402  (bestaat na de lokale ronde)
except ImportError:
    pass

if __name__ == "__main__":
    plaats = meet({p["slug"]: f"/schilder/{p['slug']}/" for p in PLAATSEN})
    samenvatting("Plaatspagina's (alle)", plaats)
    if TOP10:
        samenvatting("Plaatspagina's (top 10)", plaats, set(TOP10))
        samenvatting("Plaatspagina's (overige)", plaats, {p["slug"] for p in PLAATSEN} - set(TOP10))
    alle = {}
    for d in DIENSTEN:
        res = meet({p["slug"]: f"/schilder/{p['slug']}/{d['slug']}/" for p in PLAATSEN})
        alle.update({f"{k}/{d['slug']}": v for k, v in res.items()})
    samenvatting("Plaats-dienstpagina's (alle)", alle)
    if TOP10:
        samenvatting("Plaats-dienstpagina's (top 10)", alle,
                     {k for k in alle if k.split("/")[0] in TOP10})
    dienst = meet({d["slug"]: f"/schilderwerk/{d['slug']}/" for d in DIENSTEN})
    samenvatting("Dienstpagina's", dienst)

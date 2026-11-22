# -*- coding: utf-8 -*-
"""Meet hoeveel tekst op de plaats-dienstpagina's uniek is (los te draaien na build.py).

Per pagina: aandeel woord-8-grammen dat op geen enkele andere pagina van dezelfde dienst
voorkomt. Plaatsnamen worden vervangen door X, zodat 'Schilder in Zwolle' en 'Schilder
in Kampen' niet als uniek tellen. Gebruik: python3 uniek.py [minimum] [maximum] [--met-cijfers]. Zonder die vlag tellen
getallen niet mee, zodat alleen echt andere zinnen als uniek tellen.
"""
import os, re, sys, html as H
from collections import Counter, defaultdict
from data import PLAATSEN, DIENSTEN

ROOT = os.path.dirname(os.path.abspath(__file__))
MET_CIJFERS = "--met-cijfers" in sys.argv  # cijfers laten staan: data telt dan als uniek
args = [a for a in sys.argv[1:] if not a.startswith("--")]
lo = int(args[0]) if len(args) > 0 else 5000
hi = int(args[1]) if len(args) > 1 else 50000
namen = sorted({p["naam"] for p in PLAATSEN} | {p["gemeente"] for p in PLAATSEN} | {p["provincie"] for p in PLAATSEN}, key=len, reverse=True)
naam_re = re.compile("|".join(re.escape(n) for n in namen))

def tekst(pad):
    h = open(os.path.join(ROOT, "site", pad.strip("/"), "index.html"), encoding="utf-8").read()
    h = re.sub(r"<(script|style|header|footer|nav)\b.*?</\1>", " ", h, flags=re.S)
    h = H.unescape(re.sub(r"<[^>]+>", " ", h))
    h = naam_re.sub("X", h)
    if not MET_CIJFERS:
        h = re.sub(r"\d[\d.,]*", "0", h)
    return re.findall(r"\w+", h.lower())

def grams(w, n=8):
    return [" ".join(w[i:i + n]) for i in range(len(w) - n + 1)]

uit = defaultdict(list)
for d in DIENSTEN:
    pg = {p["slug"]: set(grams(tekst(f"/schilder/{p['slug']}/{d['slug']}/"))) for p in PLAATSEN}
    tel = Counter(g for s in pg.values() for g in s)
    for p in PLAATSEN:
        if lo <= p["inwoners"] < hi:
            s = pg[p["slug"]]
            uniek = sum(1 for g in s if tel[g] == 1)
            uit[p["slug"]].append(100 * uniek / max(1, len(s)))
gem = {k: sum(v) / len(v) for k, v in uit.items()}
for k, v in sorted(gem.items(), key=lambda x: x[1]):
    print(f"  {k:24s} {v:5.1f}% uniek")
if gem:
    print(f"Gemiddeld {sum(gem.values()) / len(gem):.1f}% unieke tekst over {len(gem)} plaatsen ({lo}–{hi} inwoners)")

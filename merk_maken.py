# -*- coding: utf-8 -*-
"""
Maakt de PNG-bestanden van het merk met headless Chrome (alleen lokaal nodig).

    python3 merk_maken.py

Schrijft naar merk/:
- og-image.png          1200×630, voor WhatsApp, Facebook, LinkedIn en X
- apple-touch-icon.png  180×180, voor het beginscherm van iPhone/iPad
- icon-192.png, icon-512.png

build.py kopieert merk/ naar site/assets/merk/. De PNG's staan in git, zodat de
build op GitHub geen Chrome nodig heeft. Pas je het logo aan in merk_data.py,
draai dit script dan opnieuw.
"""
import os
import subprocess
import sys
import tempfile

from merk_data import LOGO_SVG, beeldmerk_inhoud

ROOT = os.path.dirname(os.path.abspath(__file__))
UIT = os.path.join(ROOT, "merk")
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

OG_HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
body{{font-family:ui-rounded,"SF Pro Rounded",-apple-system,"Segoe UI",sans-serif;color:#241906;
  background:#fbf6ee;position:relative}}
.raster{{position:absolute;inset:0;background-image:linear-gradient(rgba(60,41,15,.05) 1px,transparent 1px),
  linear-gradient(90deg,rgba(60,41,15,.05) 1px,transparent 1px);background-size:40px 40px}}
.paneel{{position:absolute;right:0;top:0;bottom:0;width:430px;background:#3c290f;overflow:hidden}}
.paneel::before{{content:"";position:absolute;left:-60px;top:250px;width:620px;height:120px;background:#f4820b;
  border-radius:60px;transform:rotate(-14deg);opacity:.95}}
.paneel svg{{position:absolute;left:95px;top:150px;width:300px;height:300px;filter:drop-shadow(0 24px 40px rgba(0,0,0,.35))}}
.tekst{{position:absolute;left:72px;top:64px;width:640px}}
.logo{{height:64px;display:block}}
h1{{font-size:66px;line-height:1.04;letter-spacing:-.02em;margin:66px 0 22px;font-weight:800}}
h1 span{{background:linear-gradient(transparent 62%,rgba(244,130,11,.35) 62%)}}
p{{font-size:28px;color:#57492f;margin:0;font-weight:600}}
.pillen{{position:absolute;left:72px;bottom:62px;display:flex;gap:12px}}
.pil{{background:#fff;border:2px solid #eadfcd;border-radius:99px;padding:10px 20px;font-size:22px;font-weight:700;color:#3c290f}}
.pil b{{color:#c25e00}}
</style></head><body><div class="raster"></div>
<div class="paneel"><svg viewBox="0 0 112 112">{beeldmerk_inhoud(bg="#fbf6ee", draad="#3c290f")}</svg></div>
<div class="tekst"><img class="logo" src="data:image/svg+xml;utf8,{LOGO_SVG.replace('#', '%23').replace('"', "'")}">
<h1>Vergelijk schilders <span>bij jou in de buurt</span></h1>
<p>Eén aanvraag, tot drie offertes uit jouw regio.</p></div>
<div class="pillen"><span class="pil"><b>✓</b> Gratis</span><span class="pil"><b>✓</b> Vrijblijvend</span><span class="pil"><b>✓</b> Maximaal 3 schilders</span></div>
</body></html>"""


def icoon_html(px, rand):
    # Chrome heeft een minimale vensterbreedte: icoon in het midden, daarna bijsnijden met sips
    return (f'<!doctype html><html><head><style>html,body{{margin:0;width:600px;height:600px;overflow:hidden;'
            f'display:grid;place-items:center;background:#fff}}'
            f'svg{{display:block;width:{px}px;height:{px}px}}</style></head><body>'
            f'<svg viewBox="{-rand} {-rand} {112 + 2 * rand} {112 + 2 * rand}" preserveAspectRatio="none">'
            f'<rect x="{-rand}" y="{-rand}" width="{112 + 2 * rand}" height="{112 + 2 * rand}" fill="#3c290f"/>'
            f'{beeldmerk_inhoud()}</svg></body></html>')


def schiet(html, naam, b, h, snij=None):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        pad = f.name
    doel = os.path.join(UIT, naam)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", f"--window-size={b},{h}",
                    f"--screenshot={doel}", "file://" + pad],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.unlink(pad)
    if snij:
        subprocess.run(["sips", "-c", str(snij), str(snij), doel], check=True, stdout=subprocess.DEVNULL)
    print("  ✓", naam)


def main():
    if not os.path.exists(CHROME):
        sys.exit("Chrome niet gevonden; zet het pad in de omgevingsvariabele CHROME.")
    os.makedirs(UIT, exist_ok=True)
    schiet(OG_HTML, "og-image.png", 1200, 630)
    # iOS rondt zelf af: een vol vlak met wat extra rand rond het beeldmerk
    schiet(icoon_html(180, 6), "apple-touch-icon.png", 600, 600, snij=180)
    schiet(icoon_html(192, 6), "icon-192.png", 600, 600, snij=192)
    schiet(icoon_html(512, 6), "icon-512.png", 600, 600, snij=512)


if __name__ == "__main__":
    main()

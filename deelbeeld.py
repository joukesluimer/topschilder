# -*- coding: utf-8 -*-
"""
Deelbare uitslag als afbeelding (canvas), gedeeld door de onderhoudskalender en de verfcalculator.

Schrijft /assets/js/deelbeeld.js. Die zet window.TSDeel neer met drie functies:
- kaart(teken): maakt een canvas van 1200 × 630 px in de huisstijl en laat `teken(ctx, kader)`
  de inhoud tekenen. Kader = {x, y, b, h}: het vlak tussen kop en voet.
- opslaan(canvas, bestandsnaam): download als PNG. Alleen na een klik van de bezoeker.
- delen(canvas, bestandsnaam, titel, tekst, url): deelt de afbeelding via het deelmenu van
  de telefoon als dat kan, anders slaat hij de afbeelding op.

Er wordt niets geüpload: de afbeelding wordt in de browser gemaakt.
"""

import os

DEEL_JS = r"""(function () {
  "use strict";
  var B = 1200, H = 630;
  var FONT = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif';

  function rondRect(ctx, x, y, b, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y); ctx.arcTo(x + b, y, x + b, y + h, r); ctx.arcTo(x + b, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + b, y, r); ctx.closePath();
  }

  function kaart(teken, kop) {
    var c = document.createElement("canvas");
    c.width = B; c.height = H;
    var ctx = c.getContext("2d");
    ctx.fillStyle = "#faf7f1"; ctx.fillRect(0, 0, B, H);
    /* kopbalk */
    ctx.fillStyle = "#3c290f"; ctx.fillRect(0, 0, B, 96);
    ctx.fillStyle = "#f4820b"; ctx.fillRect(0, 96, B, 6);
    ctx.fillStyle = "#ffffff"; ctx.font = "800 34px " + FONT; ctx.textBaseline = "middle";
    ctx.fillText(kop || "Topschilder", 48, 50);
    ctx.font = "600 22px " + FONT; ctx.fillStyle = "#ffd9ab"; ctx.textAlign = "right";
    ctx.fillText("topschilder.nl", B - 48, 50);
    ctx.textAlign = "left";
    /* voet */
    ctx.fillStyle = "#6f6047"; ctx.font = "500 19px " + FONT; ctx.textBaseline = "alphabetic";
    ctx.fillText("Richtprijzen, prijspeil 2026. Een schilder die je huis ziet, geeft de echte prijs.", 48, H - 28);
    teken(ctx, { x: 48, y: 128, b: B - 96, h: H - 128 - 64 }, FONT);
    return c;
  }

  function opslaan(c, naam) {
    function klaar(url, opruimen) {
      var a = document.createElement("a");
      a.href = url; a.download = naam;
      document.body.appendChild(a); a.click(); a.remove();
      if (opruimen) setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
    }
    if (c.toBlob) c.toBlob(function (blob) { klaar(URL.createObjectURL(blob), true); }, "image/png");
    else klaar(c.toDataURL("image/png"), false);
  }

  function delen(c, naam, titel, tekst, url) {
    if (!c.toBlob || !navigator.canShare || !window.File) { opslaan(c, naam); return; }
    c.toBlob(function (blob) {
      var f = new File([blob], naam, { type: "image/png" });
      var data = { files: [f], title: titel, text: tekst + (url ? " " + url : "") };
      if (navigator.canShare(data)) navigator.share(data).catch(function () {});
      else opslaan(c, naam);
    }, "image/png");
  }

  window.TSDeel = { kaart: kaart, opslaan: opslaan, delen: delen, rondRect: rondRect, B: B, H: H };
})();
"""


def schrijf_deelbeeld(out):
    pad = os.path.join(out, "assets", "js", "deelbeeld.js")
    os.makedirs(os.path.dirname(pad), exist_ok=True)
    with open(pad, "w", encoding="utf-8") as f:
        f.write(DEEL_JS)

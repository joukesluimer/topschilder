#!/usr/bin/env node
/* Test voor de offerteparser (offerte_parser.js).
   Draai:  node tests/test_offerteparser.js
   Met een echte pdf erbij (wordt niet in de repo gezet):
           OFFERTE_PDF=/pad/naar/offerte.pdf node tests/test_offerteparser.js
   Voor de pdf moeten de totalen gelijk zijn aan die van 00-echte-offerte-geanonimiseerd.txt. */
"use strict";
var fs = require("fs"), path = require("path");
var P = require("../offerte_parser.js");
var MAP = path.join(__dirname, "offertes");

// Per testgeval: wat er minimaal uit moet komen. posten = types van de posten die meetellen.
var VERWACHT = {
  "00-echte-offerte-geanonimiseerd.txt": {
    excl: 6608, incl: 7283.36, btw: 675.36, tarieven: [9, 21], basis: "excl", klopt: true,
    posten: ["voorbereiding", "voorbereiding", "voorbereiding", "wanden", "plafonds", "wanden", "wanden", "plafonds",
             "deur", "binnenkozijn", "plinten", "voorbereiding", "behang", "materiaal"],
    details: [
      { i: 3, aantal: 62, eenheid: "m2", eenheidsprijs: 12, bedrag: 744 },
      { i: 10, aantal: 24, eenheid: "m", bedrag: 216 },
      { i: 13, aantal: 8, eenheid: "rol", btw: 21, bedrag: 672 }
    ],
    termijnen: [2185.01, 5098.35], garantie: "12 maanden", geldigheid: "t/m 22 dec. 2026",
    lagen: 2, merken: ["Sikkens"], doorlooptijd: "8 tot 10 werkdagen", concept: true
  },
  "01-subtotaal-btw-totaal.txt": {
    excl: 2881, incl: 3140.29, btw: 259.29, tarieven: [9], basis: "excl", klopt: true,
    posten: ["buitenkozijn", "buitendeur", "boeidelen", "steiger", "houtrot"],
    details: [
      { i: 0, aantal: 8, eenheid: "st", eenheidsprijs: 150, bedrag: 1200 },
      { i: 2, aantal: 18, eenheid: "m", bedrag: 396 },
      { i: 4, aantal: 3, eenheid: "st", bedrag: 285 }
    ],
    garantie: "2 jaar", merken: ["Sikkens"], lagen: 2, buiten: true
  },
  "02-tabel-op-een-regel.txt": {
    excl: 1930, incl: 2103.7, btw: 173.7, tarieven: [9], basis: "excl", klopt: true,
    posten: ["buitenkozijn", "buitenkozijn", "buitendeur", "glaslatten"],
    details: [{ i: 1, aantal: 5, eenheidsprijs: 135, bedrag: 675 }, { i: 3, aantal: 14, eenheid: "m", bedrag: 175 }]
  },
  "03-korting-incl-btw.txt": {
    incl: 2800, excl: 2568.81, tarieven: [9], basis: "incl", klopt: true, subtotaal: 2936,
    posten: ["wanden", "plafonds", "trap", "deur", "korting"],
    details: [{ i: 1, aantal: 36, eenheid: "m2", bedrag: 648 }, { i: 3, aantal: 5, eenheid: "st" }, { i: 4, bedrag: -136 }]
  },
  "04-stelpost-uurloon.txt": {
    excl: 3456, incl: 4181.76, tarieven: [21], basis: "excl", klopt: true, uurloon: 52.5,
    posten: ["buitenkozijn", "dakkapel", "houtrot", "kitwerk", "boeidelen"],
    details: [
      { i: 0, aantal: 9, eenheid: "st", omschrijvingBegint: "Kozijnen" },
      { i: 2, stelpost: true, bedrag: 400 },
      { i: 3, aantal: 32, eenheid: "m" },
      { i: 4, aantal: 22, eenheid: "m" }
    ],
    vraagBevat: "21% btw"
  },
  "05-varianten.txt": {
    excl: 2890, incl: 3150.1, tarieven: [9], klopt: true, varianten: [2890, 3900],
    posten: ["buitenkozijn", "boeidelen", "steiger"],
    nietMeetellen: 3, garantie: "5 jaar"
  },
  "06-opties-na-totaal.txt": {
    excl: 2430, incl: 2648.7, btw: 218.7, tarieven: [9], basis: "excl", klopt: true,
    posten: ["wanden", "plafonds", "wanden", "binnenkozijn", "voorbereiding"],
    nietMeetellen: 2, geldigheid: "30 dagen"
  },
  "07-eenheidsprijs-zonder-totaal.txt": {
    incl: 1772, excl: null, basis: "incl",
    posten: ["keukenfront", "uren", "plafonds", "materiaal"],
    details: [
      { i: 0, aantal: 16, eenheid: "st", eenheidsprijs: 70, bedrag: 1120, berekend: true },
      { i: 1, aantal: 6, eenheid: "uur", bedrag: 297 },
      { i: 2, aantal: 14, eenheid: "m2", bedrag: 210 }
    ],
    uurloon: 49.5
  },
  "08-alleen-totaal.txt": {
    excl: null, incl: null, twijfel: 2450, posten: [], lagen: 2, buiten: true
  },
  "09-termijnen-en-21-procent.txt": {
    excl: 3117, incl: 3771.57, btw: 654.57, tarieven: [21], basis: "excl", klopt: true,
    posten: ["wanden", "binnenkozijn", "uren"], termijnen: [1885.79, 1885.78], uurloon: 55,
    geldigheid: "tot 31-12-2026", vraagBevat: "50%"
  }
};

var fouten = 0, getest = 0;
function check(naam, wat, kreeg, wilde) {
  getest++;
  var ok = JSON.stringify(kreeg) === JSON.stringify(wilde) ||
    (typeof wilde === "number" && typeof kreeg === "number" && Math.abs(kreeg - wilde) < 0.011);
  if (!ok) { fouten++; console.log("  FOUT " + naam + " · " + wat + ": kreeg " + JSON.stringify(kreeg) + ", verwacht " + JSON.stringify(wilde)); }
}

function test(naam, tekst, v) {
  var r = P.leesOfferte(tekst);
  var tellen = r.posten.filter(function (p) { return p.meetellen; });
  if ("excl" in v) check(naam, "totaal excl", r.totaal.excl, v.excl);
  if ("incl" in v) check(naam, "totaal incl", r.totaal.incl, v.incl);
  if ("btw" in v) check(naam, "btw-bedrag", r.totaal.btw, v.btw);
  if (v.tarieven) check(naam, "btw-tarieven", r.btwTarieven, v.tarieven);
  if (v.basis) check(naam, "basis", r.basis, v.basis);
  if ("klopt" in v) check(naam, "posten tellen op tot totaal", r.controle.klopt, v.klopt);
  if ("subtotaal" in v) check(naam, "subtotaal", r.subtotaal, v.subtotaal);
  if (v.posten) check(naam, "post-types", tellen.map(function (p) { return p.type; }), v.posten);
  if ("nietMeetellen" in v) check(naam, "posten die niet meetellen", r.posten.length - tellen.length, v.nietMeetellen);
  (v.details || []).forEach(function (d) {
    var p = tellen[d.i] || {};
    Object.keys(d).forEach(function (k) {
      if (k === "i") return;
      if (k === "omschrijvingBegint") check(naam, "post " + d.i + " omschrijving", (p.omschrijving || "").indexOf(d[k]) === 0, true);
      else check(naam, "post " + d.i + " " + k, p[k], d[k]);
    });
  });
  if (v.termijnen) check(naam, "termijnen", r.termijnen.map(function (t) { return t.bedrag; }), v.termijnen);
  if (v.varianten) check(naam, "varianten", r.varianten.map(function (x) { return x.totaal; }), v.varianten);
  if ("twijfel" in v) check(naam, "totaal zonder btw-aanduiding", r.totaal.twijfel, v.twijfel);
  ["garantie", "geldigheid", "uurloon", "doorlooptijd", "concept", "buiten"].forEach(function (k) {
    if (k in v) check(naam, k, r[k], v[k]);
  });
  if ("lagen" in v) check(naam, "aantal lagen", r.lagen.aantal, v.lagen);
  if (v.merken) check(naam, "verfmerk", r.merken, v.merken);
  if (v.vraagBevat) {
    var vragen = P.algemeneVragen(r).concat.apply(P.algemeneVragen(r), r.posten.map(function (p) {
      return P.beoordeelPost(p, {}, 1, r.basis, r.btwTarieven[0]).vragen;
    }));
    check(naam, "vraag met '" + v.vraagBevat + "'", vragen.some(function (q) { return q.indexOf(v.vraagBevat) >= 0; }), true);
  }
  return r;
}

Object.keys(VERWACHT).forEach(function (naam) {
  var voor = fouten;
  test(naam, fs.readFileSync(path.join(MAP, naam), "utf8"), VERWACHT[naam]);
  console.log((fouten === voor ? "ok   " : "FOUT ") + naam);
});

// Losse controles op getallen en soorten.
[["1.234,50", 1234.5], ["€ 1234", 1234], ["1.250", 1250], ["12,5", 12.5], ["1.250,-", 1250], ["-150", -150], ["€ 6.608,00", 6608]]
  .forEach(function (x) { check("getal", x[0], P.getal(x[0]), x[1]); });
[["Boeiboorden en windveren schilderen", "boeidelen"], ["Glaslatten kitten", "glaslatten"], ["Trapgat wanden sausen", "wanden"],
 ["Vloeren en keuken afdekken", "voorbereiding"], ["Behang verwijderen op geselecteerde wanden", "voorbereiding"], ["Hal en trap nieuw behang", "behang"], ["Voordeur lakken", "buitendeur"]]
  .forEach(function (x) { check("soort", x[0], P.bepaalType(x[0], "binnen"), x[1]); });

// Richtprijs-oordeel: 4 binnendeuren à € 125 excl. 9% btw = € 545 incl., band € 65–185 per deur.
var b = P.beoordeelPost({ type: "deur", aantal: 4, eenheid: "st", bedrag: 500, btw: 9 },
  { deur: { van: 65, tot: 185 } }, 1, "excl", 9);
check("oordeel", "binnendeuren", b.oordeel, "binnen");

function klaar() {
  console.log("\n" + (getest - fouten) + " van " + getest + " controles goed.");
  process.exit(fouten ? 1 : 0);
}

// Optioneel: de echte pdf via pdf.js uitlezen, op dezelfde manier als de site.
if (process.env.OFFERTE_PDF) {
  var lib = require("../vendor/pdfjs/pdf.min.js");
  lib.GlobalWorkerOptions.workerSrc = path.join(__dirname, "../vendor/pdfjs/pdf.worker.min.js");
  lib.getDocument({ data: new Uint8Array(fs.readFileSync(process.env.OFFERTE_PDF)), verbosity: 0 }).promise.then(function (doc) {
    var p = [];
    for (var i = 1; i <= doc.numPages; i++) p.push(doc.getPage(i).then(function (pg) { return pg.getTextContent(); }));
    return Promise.all(p);
  }).then(function (inh) {
    var tekst = inh.map(function (c) { return P.regelsUitItems(c.items); }).join("\n");
    var v = VERWACHT["00-echte-offerte-geanonimiseerd.txt"];
    var voor = fouten;
    test("echte pdf", tekst, { excl: v.excl, incl: v.incl, btw: v.btw, tarieven: v.tarieven, klopt: true, posten: v.posten });
    console.log((fouten === voor ? "ok   " : "FOUT ") + "echte pdf (" + path.basename(process.env.OFFERTE_PDF).replace(/./g, "*").slice(0, 8) + ")");
    klaar();
  }).catch(function (e) { console.log("pdf niet te lezen: " + e.message); fouten++; klaar(); });
} else {
  klaar();
}

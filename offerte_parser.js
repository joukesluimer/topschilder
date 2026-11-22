/* Offerteparser voor topschilder.nl.
   Leest de tekst van een schildersofferte uit: posten, aantallen, totalen, btw en
   afspraken. Draait in de browser (window.TSOfferte) en in Node (tests/).
   Alles gebeurt lokaal; er wordt niets verstuurd. */
(function (root, maak) {
  var api = maak();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.TSOfferte = api;
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  /* ------------------------------------------------------------ soorten werk */
  // band: sleutel in TS_PRIJSBANDEN. eenheid: waarin de richtprijs geldt.
  var TYPES = {
    wanden:        { naam: "Wanden",                 band: "muren_plafonds_m2", eenheid: "m2" },
    plafonds:      { naam: "Plafonds",               band: "plafond",           eenheid: "m2" },
    buitenkozijn:  { naam: "Kozijnen buiten",        band: "buitenkozijn",      eenheid: "st" },
    binnenkozijn:  { naam: "Kozijnen binnen",        band: "binnenkozijn",      eenheid: "st" },
    deur:          { naam: "Binnendeuren",           band: "deur",              eenheid: "st" },
    buitendeur:    { naam: "Buitendeuren",           band: "buitendeur",        eenheid: "st" },
    dakkapel:      { naam: "Dakkapel",               band: "dakkapel",          eenheid: "st" },
    boeidelen:     { naam: "Boeidelen en windveren", eenheid: "m" },
    glaslatten:    { naam: "Glaslatten",             eenheid: "m" },
    kitwerk:       { naam: "Kitwerk",                eenheid: "m" },
    plinten:       { naam: "Plinten",                eenheid: "m" },
    keukenfront:   { naam: "Keukenfronten",          band: "keukenfront",       eenheid: "st" },
    trap:          { naam: "Trap",                   band: "trap",              eenheid: "st" },
    behang:        { naam: "Behangen",               band: "behang_m2",         eenheid: "m2" },
    houtrot:       { naam: "Houtrot",                band: "houtrot_plek",      eenheid: "st" },
    steiger:       { naam: "Steiger of hoogwerker",  band: "steiger",           eenheid: "post" },
    voorbereiding: { naam: "Voorbereiding en afdekken" },
    uren:          { naam: "Uren (regie)",           band: "uurloon",           eenheid: "uur" },
    materiaal:     { naam: "Materiaal",              materiaal: true },
    overig:        { naam: "Overig" },
    korting:       { naam: "Korting" }
  };
  var EENHEDEN = { m2: "m²", m: "meter", st: "stuks", uur: "uur", rol: "rol", post: "post", dag: "dag" };

  /* ------------------------------------------------------------ getallen */
  // Nederlandse notatie: 1.250,50 · 1250,50 · € 1.250 · € 1250 · 1.250,- · 12,5
  function getal(t) {
    t = String(t == null ? "" : t).replace(/\s|€|euro|eur/gi, "");
    var neg = /^-/.test(t) || /^-\/-/.test(t);
    t = t.replace(/^-\/-|^-/, "").replace(/,-{1,2}$/, "");
    if (!t) return null;
    if (/,\d+$/.test(t)) t = t.replace(/\./g, "").replace(",", ".");
    else if (/^\d{1,3}(\.\d{3})+$/.test(t)) t = t.replace(/\./g, "");
    else if (!/^\d+\.\d{1,2}$/.test(t)) t = t.replace(/\./g, "");
    if (!/^\d+(\.\d+)?$/.test(t)) return null;
    var n = parseFloat(t);
    return isNaN(n) ? null : (neg ? -n : n);
  }
  function rond(n) { return Math.round(n * 100) / 100; }
  function gelijk(a, b, marge) {
    if (a == null || b == null) return false;
    return Math.abs(a - b) <= Math.max(marge == null ? 1 : marge, Math.abs(b) * 0.003);
  }

  var NUM_EURO = "\\d{1,3}(?:\\.\\d{3})+(?:,(?:\\d{1,2}|-{1,2}))?|\\d+(?:,(?:\\d{1,2}|-{1,2})|\\.\\d{2}(?!\\d))?";
  var NUM_DEC = "\\d{1,3}(?:\\.\\d{3})+,(?:\\d{2}|-{1,2})|\\d+,(?:\\d{2}|-{1,2})";
  var RE_BEDRAG = new RegExp("(-\\/-\\s*|-(?=\\s*€))?\\s*(?:(?:€|\\beur\\b|\\beuro\\b)\\s*(-\\s*)?(" + NUM_EURO + ")|(" + NUM_DEC + ")(?:\\s*(?:€|\\beuro\\b|\\beur\\b))?)", "gi");
  var RE_NA_EENHEID = /^\s*(m²|m2|m1|m\b|st\b|st\.|stuks?\b|uur\b|uren\b|meter|mtr|%|x\b|keer\b|rol|plek|kozijn|deur|liter|ltr|l\b|mm\b|cm\b|dagen\b|dag\b)/i;
  var RE_PER_EENHEID = /^\s*(?:excl\.?\s*(?:btw)?\s*)?(?:per|\/|p\/|p\.)\s*(m²|m2|m1|m\b|meter|mtr|str|st\b|st\.|stuk|uur|u\b|kozijn|deur|front|plek|raam|dag|rol)/i;

  function zoekBedragen(regel) {
    var uit = [], m;
    RE_BEDRAG.lastIndex = 0;
    while ((m = RE_BEDRAG.exec(regel))) {
      var start = m.index + (m[0].length - m[0].replace(/^\s+/, "").length);
      var voor = regel.charAt(start - 1);
      var na = regel.slice(m.index + m[0].length);
      var euro = m[3] != null;
      if (/[\d.,a-z]/i.test(voor) && !euro) continue;
      if (/^\s*%/.test(na) || /^\d/.test(na)) continue;
      if (!euro && RE_NA_EENHEID.test(na)) continue;
      var w = getal(euro ? m[3] : m[4]);
      if (w == null) continue;
      if (m[1] || m[2]) w = -Math.abs(w);
      uit.push({
        waarde: w, start: start, eind: m.index + m[0].length, euro: euro,
        perEenheid: RE_PER_EENHEID.test(na) ? eenheidVan(RE_PER_EENHEID.exec(na)[1]) : null,
        a: /(?:^|\s)(?:à|á|a|@|x|per)\s*$/i.test(regel.slice(Math.max(0, start - 6), start))
      });
    }
    return uit;
  }

  /* ------------------------------------------------------------ aantallen */
  var RE_AANTAL = /(\d+(?:[.,]\d+)?)\s*(m²|m2|m\^2|vierkante\s+meters?|m1|str(?:\.|ekkende)?\s*m(?:eter|tr|1)?\.?|meters?|mtr\.?|m|stuks|stuk|st\.?|uren|uur|rollen|rol|posten|post|kozijnen|kozijn|ramen|raam|deuren|deur|fronten|front|plekken|plek|trappen|trap|dagen|dag|gevels|gevel|dakkapellen|dakkapel)(?![a-zà-ÿ0-9²])/gi;
  var RE_AANTAL_X = /(\d+)\s*x\s+(?=kozijn|deur|raam|ramen|front|plek|dakkapel|trap|gevel|binnendeur|buitendeur)/gi;
  function eenheidVan(e) {
    e = String(e || "").toLowerCase();
    if (/^(m²|m2|m\^2|vierkant)/.test(e)) return "m2";
    if (/^(m1|str|meter|mtr|m)$|^(str|meter|mtr)/.test(e) || e === "m") return "m";
    if (/^(uur|uren|u)$/.test(e)) return "uur";
    if (/^rol/.test(e)) return "rol";
    if (/^post/.test(e)) return "post";
    if (/^dag/.test(e)) return "dag";
    return "st";
  }
  function zoekAantallen(regel, bedragen) {
    var uit = [], m;
    function inBedrag(i) { return bedragen.some(function (b) { return i >= b.start && i < b.eind; }); }
    RE_AANTAL.lastIndex = 0;
    while ((m = RE_AANTAL.exec(regel))) {
      if (inBedrag(m.index)) continue;
      var voor = regel.charAt(m.index - 1);
      if (/[\d.,\/a-z]/i.test(voor)) continue;
      uit.push({ aantal: getal(m[1]), eenheid: eenheidVan(m[2]), start: m.index, eind: m.index + m[0].length });
    }
    if (!uit.length) {
      RE_AANTAL_X.lastIndex = 0;
      while ((m = RE_AANTAL_X.exec(regel))) {
        if (!inBedrag(m.index)) uit.push({ aantal: getal(m[1]), eenheid: "st", start: m.index, eind: m.index + m[0].length });
      }
    }
    return uit;
  }

  /* ------------------------------------------------------------ soort herkennen */
  var REGELS_TYPE = [
    ["steiger", /steiger|hoogwerker|ladderlift|rolsteiger/],
    ["houtrot", /houtrot|rotte?\s+(hout|plek)|inzetstuk|epoxy|houtreparatie|hout\s+(herstel|vervang)|dorpel\s+vervang|vervangen\s+(van\s+)?(onder)?dorpel/],
    ["materiaal", /\b(leveren|levering|materiaal|materialen|verf\s+en\s+materiaal)\b/],
    ["voorbereiding", /(behang|verf|verflagen)\s+(verwijderen|afstomen|weghalen|afbijten)|afstomen|afbijten|verwijderen\s+(van\s+)?(het\s+)?(oude?\s+)?(behang|verf)/],
    ["voorbereiding", /afdek|afplak|beschermen|voorstrijk|voorbehandel|gaten\s+vullen|kleine\s+(gaten|reparaties)|voorbereid|reinig|ontvet|schoonmak|opstart|aan-?\s*en\s+afvoer/, /\b(sausen|sauzen|lakken|aflakken|schilderen|verven|spuiten)\b/],
    ["glaslatten", /glaslat|glaslijst/],
    ["kitwerk", /\bkit(ten|werk|voeg|voegen)?\b|beglazingskit|afkitten/],
    ["boeidelen", /boeid|boeiboord|windveer|windveren|daktrim|gootlijst|overstek|dakgoot|goot\b/],
    ["keukenfront", /keukenfront|keukenkast|keukendeur|keukenlad|fronten|kastdeur/],
    ["behang", /behang|glasvlies|vliesbehang/],
    ["dakkapel", /dakkapel/],
    ["plinten", /plint/],
    ["trap", /\btrap(pen|treden|hek|leuning)?\b|traptreden|stootbord/],
    ["buitendeur", /voordeur|achterdeur|buitendeur|garagedeur|tuindeur|schuurdeur|bergingdeur|deur(en)?\s+buiten/],
    ["kozijn", /kozijn|ramen|\braam|deurstijl|draaiende\s+delen|onderdorpel|lijstwerk/],
    ["deur", /\bdeur|deuren/],
    ["plafonds", /plafond/, /wand|muur|muren/],
    ["wanden", /wand|muur|muren|sausen|sauzen|latex|muurverf|spuitwerk|stucwerk/],
    ["uren", /\bregie|uurloon|uurtarief|\buren\b|manuren/],
    ["korting", /korting|reductie|vermindering|kortings/]
  ];
  function bepaalType(tekst, context) {
    var t = tekst.toLowerCase();
    for (var i = 0; i < REGELS_TYPE.length; i++) {
      var r = REGELS_TYPE[i];
      if (!r[1].test(t)) continue;
      if (r[2] && r[2].test(t)) continue;
      if (r[0] === "kozijn") {
        if (/binnen|deurkozijn|deurstijl|binnendeur/.test(t)) return "binnenkozijn";
        if (/buiten|gevel|ramen|\braam|dorpel|draaiende/.test(t)) return "buitenkozijn";
        return context === "binnen" ? "binnenkozijn" : "buitenkozijn";
      }
      if (r[0] === "deur" && context === "buiten" && !/binnen/.test(t)) return "buitendeur";
      return r[0];
    }
    return "overig";
  }

  /* ------------------------------------------------------------ regels voorbereiden */
  // pdf.js zet soms meerdere tabelrijen op één regel. Knip na een bedrag als er
  // daarna een nieuwe omschrijving (hoofdletter) én nog een bedrag volgt.
  function knipRegel(regel) {
    var b = zoekBedragen(regel);
    if (b.length < 2) return [regel];
    for (var i = 0; i < b.length - 1; i++) {
      var rest = regel.slice(b[i].eind);
      var m = /^\s*(?:\d{1,2}\s*%\s*)?(?=[A-ZÀ-Ý][a-zà-ÿ]{2,})/.exec(rest);
      if (!m) continue;
      var woord = /^\s*(?:\d{1,2}\s*%\s*)?([A-Za-zÀ-ÿ]+)/.exec(rest)[1].toLowerCase();
      if (/^(excl|incl|exclusief|inclusief|per|euro|eur)$/.test(woord)) continue;
      var heeftTekstVoor = /[a-zà-ÿ]{3,}/i.test(regel.slice(0, b[i].start));
      var restBedrag = zoekBedragen(rest).length > 0;
      if (heeftTekstVoor && restBedrag) {
        var knip = b[i].eind + m[0].length;
        return [regel.slice(0, knip)].concat(knipRegel(regel.slice(knip)));
      }
    }
    return [regel];
  }

  function letters(t) { return (t.match(/[a-zà-ÿ]/gi) || []).length; }
  function zonderBedragen(regel, bedragen) {
    var s = regel;
    for (var i = bedragen.length - 1; i >= 0; i--) s = s.slice(0, bedragen[i].start) + " " + s.slice(bedragen[i].eind);
    return s;
  }
  function schoon(t) {
    return t.replace(/^\s*\d{1,2}[.)]\s+/, "").replace(/\s*\|\s*/g, " – ").replace(/\s{2,}/g, " ").replace(/^[\s–\-:•*.]+|[\s–\-:•*=]+$/g, "").trim();
  }

  var RE_TOTAAL = /(sub\s*-?\s*totaal|totaal|eindbedrag|te\s+betalen|aanneemsom|offertebedrag|totale\s+prijs|prijs\s+totaal|totaalprijs|totaalbedrag)/i;
  var RE_BTW = /\bbtw\b|b\.t\.w|omzetbelasting/i;
  var RE_TERMIJN = /(termijn|aanbetaling|bij\s+(de\s+)?(start|aanvang|opdracht|akkoord|ondertekening|levering)|na\s+(de\s+)?(oplevering|afronding|voltooiing|gereedmelding)|bij\s+oplevering|halverwege|na\s+\d+\s*%|eindafrekening)/i;
  var RE_STELPOST = /stelpost|\bp\.?\s?m\.?\b|voorlopige?\s+(post|raming)|nacalculatie/i;
  var RE_OPTIE = /\boptie\b|optioneel|meerprijs|desgewenst|indien\s+gewenst|op\s+verzoek|alternatief|\bkeuze\b|niet\s+inbegrepen|meerwerk\s*:/i;
  var RE_UUR = /per\s+uur|\/\s*uur|uurloon|uurtarief|\bp\/u\b|regie(tarief)?|manuur/i;

  /* ------------------------------------------------------------ hoofdfunctie */
  function leesOfferte(tekst) {
    tekst = String(tekst || "").replace(/ /g, " ").replace(/\r/g, "");
    var ruw = tekst.split("\n");
    var regels = [];
    ruw.forEach(function (r) { knipRegel(r).forEach(function (k) { if (k.trim()) regels.push(k); }); });
    var laag = tekst.toLowerCase();

    var context = (laag.match(/buiten(schilder)?werk|buitenzijde|gevel|buitenkozijn|voordeur|boeid|dakkapel|windveer/g) || []).length >
                  (laag.match(/binnen(schilder)?werk|interieur|woonkamer|slaapkamer/g) || []).length ? "buiten" : "binnen";
    var posten = [], totalen = [], btwRegels = [], termijnen = [], tarieven = [], losseBedragen = [];
    var sectie = null, variant = null, varianten = [], wachtTotaal = null, meldingen = [];

    regels.forEach(function (regel, i) {
      var r = regel.toLowerCase();
      var bedragen = zoekBedragen(regel);
      var kaal = zonderBedragen(regel, bedragen);
      var tekstLetters = letters(kaal.replace(/[€]|eur(o)?/gi, ""));

      // Regels zonder bedrag: kopjes en totaal-labels.
      if (!bedragen.length) {
        if (wachtTotaal && --wachtTotaal.ttl <= 0) wachtTotaal = null;
        var kop = r.trim();
        if (/^(betalingsschema|betaalschema|betalingsvoorwaarden|betalingstermijnen|termijnen|betaling)\b/.test(kop)) sectie = "betaling";
        else if (/^(opties|optioneel|meerprijzen|extra\s+opties|aanvullende\s+opties|optionele|niet\s+inbegrepen|meerwerk\b)/.test(kop)) sectie = "opties";
        else if (/^stelposten?\b/.test(kop)) sectie = "stelposten";
        else if (/^(variant|alternatief|offerte|prijsvariant)\s+([a-d1-4])\b/.test(kop) && kop.length < 70) {
          variant = kop.match(/^(variant|alternatief|offerte|prijsvariant)\s+([a-d1-4])/)[0];
          if (varianten.indexOf(variant) < 0) varianten.push(variant);
          sectie = null;
        } else if (/^(werkzaamheden|prijsopgave|specificatie|omschrijving)\b/.test(kop)) sectie = null;
        if (/buiten(schilder)?werk|buitenzijde|^buiten\b|gevel/.test(kop) && kop.length < 60) context = "buiten";
        else if (/binnen(schilder)?werk|^binnen\b|interieur/.test(kop) && kop.length < 60) context = "binnen";
        var tm = RE_TOTAAL.exec(regel);
        if (tm) {
          var soort = totaalSoort(regel.slice(tm.index));
          if (soort) {
            var los = losseBedragen.length && losseBedragen[losseBedragen.length - 1];
            if (los && i - los.regel <= 2 && !los.gebruikt) { los.gebruikt = true; voegTotaalToe(soort, los.waarde, i); }
            else wachtTotaal = { soort: soort, ttl: 6, regel: i };
          }
        }
        return;
      }

      // Alleen een bedrag op de regel: hoort bij een totaal-label erboven of eronder.
      if (tekstLetters < 3) {
        var w = bedragen[bedragen.length - 1].waarde;
        if (wachtTotaal) { voegTotaalToe(wachtTotaal.soort, w, i); wachtTotaal = null; }
        else losseBedragen.push({ waarde: w, regel: i });
        return;
      }
      wachtTotaal = null;
      var bedrag = bedragen[bedragen.length - 1].waarde;
      var procent = (/(\d{1,2}(?:[.,]\d+)?)\s*%/.exec(kaal) || [])[1];
      procent = procent != null ? getal(procent) : null;

      // Betalingstermijnen (een korting 'bij opdracht' is geen termijn)
      if (!/korting|reductie/.test(r) && (sectie === "betaling" || RE_TERMIJN.test(r)) && !RE_BTW.test(r.replace(/(incl|excl)\.?\s*btw/g, "")) && !RE_TOTAAL.test(r)) {
        termijnen.push({ omschrijving: schoon(kaal.replace(/\d{1,3}\s*%/, "")), procent: procent, bedrag: bedrag });
        return;
      }
      // Totalen
      var tm2 = RE_TOTAAL.exec(regel);
      if (tm2 && !(sectie === "opties" && /optie/i.test(r))) {
        var s2 = totaalSoort(regel.slice(tm2.index));
        if (s2) { voegTotaalToe(s2, bedrag, i); return; }
      }
      var aantallen = zoekAantallen(regel, bedragen);
      // Btw-regels
      if (RE_BTW.test(r) && !aantallen.length && !/korting/.test(r) && (procent != null || /^\s*(btw|b\.t\.w|omzetbelasting)/.test(r))) {
        var grond = bedragen.length > 1 ? Math.abs(bedragen[0].waarde) : null;
        var tarief = procent;
        if (tarief == null && grond) tarief = Math.round(bedrag / grond * 100);
        btwRegels.push({ tarief: tarief, grondslag: grond, bedrag: Math.abs(bedrag), regel: i });
        return;
      }

      var a = aantallen.length ? kiesAantal(aantallen, bedragen) : null;
      var oms = schoon(zonderAantallen(kaal, a ? [a] : []).replace(/\b\d{1,2}\s*%/g, "").replace(/\s(à|á|a|x|@|per\s+\S+)\s*$/i, ""));
      var type = bepaalType(oms + " " + kaal, context);
      if (a && a.eenheid === "uur" && type !== "korting") type = "uren";

      // Kortingen
      if (type === "korting" || /korting|reductie|-\/-|actieprijs/.test(r)) {
        posten.push(maakPost({ omschrijving: oms, type: "korting", bedrag: -Math.abs(bedrag), regel: i, btw: btwVan(kaal) }));
        return;
      }

      // Alleen een tarief, zonder aantal: uurloon of prijs per eenheid.
      var eenheidsprijs = null, berekend = false;
      var b0 = bedragen[0], bl = bedragen[bedragen.length - 1];
      if (bedragen.length === 1 && (b0.perEenheid || (b0.a && a))) {
        if (!a) {
          if (b0.perEenheid === "uur" || RE_UUR.test(r)) tarieven.push({ soort: "uurloon", bedrag: Math.abs(bedrag), omschrijving: oms });
          else tarieven.push({ soort: type, eenheid: b0.perEenheid, bedrag: Math.abs(bedrag), omschrijving: oms });
          if (type !== "overig" && type !== "uren" && b0.perEenheid !== "uur") {
            posten.push(maakPost({ omschrijving: oms, type: type, eenheid: b0.perEenheid, eenheidsprijs: Math.abs(bedrag), bedrag: null, regel: i, meetellen: false, alleenTarief: true }));
          }
          return;
        }
        eenheidsprijs = Math.abs(bedrag);
        bedrag = rond(a.aantal * eenheidsprijs);
        berekend = true;
      } else if (bedragen.length === 1 && RE_UUR.test(r) && !a) {
        tarieven.push({ soort: "uurloon", bedrag: Math.abs(bedrag), omschrijving: oms });
        return;
      } else if (bedragen.length >= 2) {
        var eerste = Math.abs(b0.waarde);
        if (a && gelijk(a.aantal * eerste, Math.abs(bl.waarde), 1.5)) eenheidsprijs = eerste;
        else if (b0.perEenheid || b0.a) eenheidsprijs = eerste;
      }

      var stel = RE_STELPOST.test(r) || sectie === "stelposten";
      var optie = sectie === "opties" || RE_OPTIE.test(r) || (variant && varianten.indexOf(variant) > 0);
      var naTotaal = totalen.some(function (t) { return t.soort !== "sub" && t.soort !== "groep"; }) && !variant;
      var p = maakPost({
        omschrijving: oms, type: type, aantal: a ? a.aantal : null, eenheid: a ? a.eenheid : null,
        eenheidsprijs: eenheidsprijs, bedrag: rond(bedrag), berekend: berekend, btw: btwVan(kaal),
        stelpost: stel, optie: !!optie, naTotaal: naTotaal && !optie, variant: variant, regel: i
      });
      if (p.type === "uren" && p.eenheid === "uur" && p.aantal && !p.eenheidsprijs) p.eenheidsprijs = rond(p.bedrag / p.aantal);
      if (p.type === "steiger" && !p.aantal) { p.aantal = 1; p.eenheid = "post"; }
      if ((p.type === "trap" || p.type === "dakkapel") && !p.aantal) { p.aantal = 1; p.eenheid = "st"; }
      posten.push(p);
    });

    function voegTotaalToe(soort, waarde, regel) {
      totalen.push({ soort: soort, waarde: Math.abs(waarde), regel: regel, variant: variant });
    }

    return verzoen({
      tekst: laag, regels: regels, posten: posten, totalen: totalen, btwRegels: btwRegels,
      termijnen: termijnen, tarieven: tarieven, varianten: varianten, context: context, meldingen: meldingen
    });
  }

  function zonderAantallen(s, aantallen) {
    // aantallen zijn gemeten op de oorspronkelijke regel; zonderBedragen behoudt de posities niet
    // exact, dus we verwijderen ze op tekst.
    aantallen.forEach(function (a) {
      s = s.replace(new RegExp("(^|[^\\d.,])" + String(a.aantal).replace(".", "[.,]") + "\\s*(m²|m2|m\\^2|vierkante\\s+meters?|m1|str\\S*\\s*m\\S*|meters?|mtr\\.?|m|stuks|stuk|st\\.?|uren|uur|rollen|rol|posten|post|dagen|dag)(?![a-zà-ÿ0-9²])", "i"), "$1 ");
    });
    return s;
  }
  function kiesAantal(aantallen, bedragen) {
    // Neem het aantal dat het dichtst vóór het eerste bedrag staat (de kolom 'aantal').
    var eerste = bedragen.length ? bedragen[0].start : Infinity;
    var voor = aantallen.filter(function (a) { return a.start < eerste; });
    return voor.length ? voor[voor.length - 1] : aantallen[0];
  }
  function btwVan(t) {
    var m = /(?:^|[^\d,.])(9|21|0)\s*%/.exec(t);
    return m ? parseInt(m[1], 10) : null;
  }
  function totaalSoort(t) {
    var l = t.toLowerCase();
    if (/^sub/.test(l)) return "sub";
    var incl = /incl|inclusief|inc\.\s*btw|met\s+btw/.test(l), excl = /excl|exclusief|ex\.?\s+btw|zonder\s+btw|exc\.\s*btw/.test(l);
    var rest = l.replace(/\(.*?\)/g, " ").replace(/totaal(prijs|bedrag)?|eindbedrag|te\s+betalen|aanneemsom|offertebedrag|totale\s+prijs|prijs|incl\w*|excl\w*|inc\.|ex\.|btw|b\.t\.w\.?|bedrag|generaal|offerte|alles|in|met|zonder|de|het|van|deze|voor|over|euro|eur|€|[\d.,%:=\-–]+/g, " ");
    if (letters(rest) >= 4) return incl ? "incl" : excl ? "excl" : "groep";
    return incl ? "incl" : excl ? "excl" : "onbekend";
  }
  function maakPost(p) {
    return {
      omschrijving: p.omschrijving || "", type: p.type || "overig",
      aantal: p.aantal != null ? p.aantal : null, eenheid: p.eenheid || null,
      eenheidsprijs: p.eenheidsprijs != null ? p.eenheidsprijs : null,
      bedrag: p.bedrag != null ? p.bedrag : null, berekend: !!p.berekend,
      btw: p.btw != null ? p.btw : null, stelpost: !!p.stelpost, optie: !!p.optie,
      naTotaal: !!p.naTotaal, alleenTarief: !!p.alleenTarief, variant: p.variant || null,
      meetellen: p.meetellen === false ? false : !(p.optie || p.naTotaal), regel: p.regel
    };
  }

  /* ------------------------------------------------------------ totalen kloppend maken */
  function verzoen(d) {
    var t = d.tekst, uit = {
      posten: d.posten, termijnen: d.termijnen, btwRegels: d.btwRegels.map(function (b) { return { tarief: b.tarief, grondslag: b.grondslag, bedrag: b.bedrag }; }),
      totaal: { excl: null, incl: null, btw: null, bron: {} }, subtotaal: null, varianten: [],
      basis: null, btwTarieven: [], context: d.context, meldingen: d.meldingen
    };
    var btwSom = d.btwRegels.length ? rond(d.btwRegels.reduce(function (s, b) { return s + b.bedrag; }, 0)) : null;
    var eersteBtw = d.btwRegels.length ? d.btwRegels[0].regel : null;
    var tarieven = [];
    d.btwRegels.forEach(function (b) { if (b.tarief != null && tarieven.indexOf(b.tarief) < 0) tarieven.push(b.tarief); });
    if (!tarieven.length) {
      var m = /(\d{1,2})\s*%\s*(btw|b\.t\.w|omzetbelasting)|(?:btw|b\.t\.w\.?)\s*(?:tarief|:)?\s*(?:van\s*)?(\d{1,2})\s*%/.exec(t);
      if (m) tarieven.push(parseInt(m[1] || m[3], 10));
      d.posten.forEach(function (p) { if (p.btw != null && p.btw > 0 && tarieven.indexOf(p.btw) < 0) tarieven.push(p.btw); });
    }

    // Varianten: per variant het eerste totaal; de eerste variant telt.
    var totalen = d.totalen;
    if (d.varianten.length > 1) {
      d.varianten.forEach(function (v) {
        var tv = totalen.filter(function (x) { return x.variant === v && x.soort !== "sub" && x.soort !== "groep"; });
        if (tv.length) uit.varianten.push({ naam: v.charAt(0).toUpperCase() + v.slice(1), totaal: tv[tv.length - 1].waarde, soort: tv[tv.length - 1].soort });
      });
      if (uit.varianten.length > 1) {
        totalen = totalen.filter(function (x) { return !x.variant || x.variant === d.varianten[0]; });
        uit.meldingen.push("De offerte heeft meerdere varianten. We rekenen met " + uit.varianten[0].naam.toLowerCase() + "; de andere posten tellen niet mee.");
      }
    }
    function laatste(soort) {
      var l = totalen.filter(function (x) { return x.soort === soort; });
      return l.length ? l[l.length - 1] : null;
    }
    var sub = laatste("sub"), ex = laatste("excl"), inc = laatste("incl");
    var onbekend = totalen.filter(function (x) { return x.soort === "onbekend"; });
    if (sub) uit.subtotaal = sub.waarde;
    var kortingNaSub = rond(d.posten.filter(function (p) { return p.type === "korting" && p.meetellen && sub && p.regel > sub.regel; })
      .reduce(function (s, p) { return s + p.bedrag; }, 0));

    var excl = ex ? ex.waarde : null, incl = inc ? inc.waarde : null;
    if (ex) uit.totaal.bron.excl = "offerte";
    if (inc) uit.totaal.bron.incl = "offerte";
    var basisHint = /(bedragen|prijzen|tarieven)\b[^\n.]{0,40}?(excl|exclusief)/.test(t) ? "excl"
      : /(bedragen|prijzen|tarieven)\b[^\n.]{0,40}?(incl|inclusief)/.test(t) ? "incl" : null;
    var RE_IN = /incl(\.|usief)?\s*(\d{1,2}\s*%\s*)?(btw|b\.t\.w)/, RE_EX = /excl(\.|usief)?\s*(\d{1,2}\s*%\s*)?(btw|b\.t\.w)/;

    // Totaal zonder incl/excl: bepaal wat het is.
    onbekend.forEach(function (o) {
      var soort = null;
      if (excl != null && btwSom != null && gelijk(o.waarde, excl + btwSom)) soort = "incl";
      else if (eersteBtw != null) soort = o.regel > eersteBtw ? "incl" : "excl";
      else if (excl != null && (gelijk(o.waarde, excl * 1.09) || gelijk(o.waarde, excl * 1.21))) soort = "incl";
      else if (incl != null && (gelijk(o.waarde * 1.09, incl) || gelijk(o.waarde * 1.21, incl))) soort = "excl";
      else if (basisHint) soort = basisHint;
      else if (RE_IN.test(t) && !RE_EX.test(t)) soort = "incl";
      else if (RE_EX.test(t) && !RE_IN.test(t)) soort = "excl";
      if (soort === "incl" && incl == null) { incl = o.waarde; uit.totaal.bron.incl = "offerte"; }
      else if (soort === "excl" && excl == null) { excl = o.waarde; uit.totaal.bron.excl = "offerte"; }
      else if (!soort && incl == null && excl == null) { o.twijfel = true; uit.totaal.twijfel = o.waarde; }
    });
    if (sub && basisHint === "incl") {
      if (incl == null) { incl = rond(sub.waarde + kortingNaSub); uit.totaal.bron.incl = kortingNaSub ? "berekend" : "offerte"; }
    } else if (excl == null && sub) { excl = rond(sub.waarde + kortingNaSub); uit.totaal.bron.excl = kortingNaSub ? "berekend" : "offerte"; }
    if (excl == null && incl != null && btwSom != null) { excl = rond(incl - btwSom); uit.totaal.bron.excl = "berekend"; }
    if (incl == null && excl != null && btwSom != null) { incl = rond(excl + btwSom); uit.totaal.bron.incl = "berekend"; }
    if (excl != null && incl != null && !tarieven.length) {
      var f = incl / excl;
      if (Math.abs(f - 1.09) < 0.003) tarieven.push(9); else if (Math.abs(f - 1.21) < 0.003) tarieven.push(21);
    }
    if (tarieven.length === 1) {
      var fac = 1 + tarieven[0] / 100;
      if (incl == null && excl != null) { incl = rond(excl * fac); uit.totaal.bron.incl = "berekend"; }
      if (excl == null && incl != null) { excl = rond(incl / fac); uit.totaal.bron.excl = "berekend"; }
    }
    // Termijnen bevestigen het totaal incl. btw.
    var termSom = rond(d.termijnen.reduce(function (s, x) { return s + x.bedrag; }, 0));
    if (incl == null && d.termijnen.length > 1 && termSom > 0 && /incl/.test(t)) { incl = termSom; uit.totaal.bron.incl = "betalingsschema"; }

    // Posten optellen en kijken op welke basis ze staan.
    var tellen = d.posten.filter(function (p) { return p.meetellen && p.bedrag != null; });
    var som = rond(tellen.reduce(function (s, p) { return s + p.bedrag; }, 0));
    var basis = basisHint;
    if (!basis) {
      if (gelijk(som, excl) || (sub && gelijk(som, sub.waarde + kortingNaSub))) basis = "excl";
      else if (gelijk(som, incl)) basis = "incl";
      else if (d.btwRegels.length || (excl != null && incl == null)) basis = "excl";
      else if (incl != null && excl == null) basis = "incl";
      else basis = "excl";
    }
    // Geen totaal op de offerte: gebruik de som van de posten.
    if (excl == null && incl == null && som > 0) {
      if (basis === "incl") { incl = som; uit.totaal.bron.incl = "posten"; } else { excl = som; uit.totaal.bron.excl = "posten"; }
      if (tarieven.length === 1) {
        var fc = 1 + tarieven[0] / 100;
        if (incl == null) { incl = rond(excl * fc); uit.totaal.bron.incl = "berekend"; }
        else { excl = rond(incl / fc); uit.totaal.bron.excl = "berekend"; }
      }
    }
    uit.totaal.excl = excl; uit.totaal.incl = incl;
    uit.totaal.btw = btwSom != null ? btwSom : (excl != null && incl != null ? rond(incl - excl) : null);
    uit.btwTarieven = tarieven.sort(function (a, b) { return a - b; });
    uit.basis = basis;
    uit.somPosten = som;
    uit.controle = controle(som, basis, uit.totaal, uit.subtotaal, kortingNaSub);
    if (d.termijnen.length > 1 && incl != null && !gelijk(termSom, incl, 2)) uit.meldingen.push("De betaaltermijnen tellen op tot " + euro(termSom) + ", het totaal is " + euro(incl) + ".");

    // Overige gegevens uit de hele tekst.
    var uurloon = d.tarieven.filter(function (x) { return x.soort === "uurloon"; })[0];
    var uurpost = d.posten.filter(function (p) { return p.type === "uren" && p.eenheidsprijs; })[0];
    uit.uurloon = uurloon ? uurloon.bedrag : uurpost ? uurpost.eenheidsprijs : null;
    uit.merken = zoekMerken(t);
    uit.lagen = zoekLagen(t);
    uit.garantie = zoekGarantie(t);
    uit.geldigheid = zoekGeldigheid(t);
    uit.betaaltermijn = (/betaal(?:termijn|tijd)[^\n]{0,30}?(\d+)\s*dagen/.exec(t) || /binnen\s*(\d+)\s*dagen\s*na\s*factuur/.exec(t) || [])[1] || null;
    if (uit.betaaltermijn) uit.betaaltermijn += " dagen";
    var dl = /(doorlooptijd|duur\s+van\s+het\s+werk|uitvoeringsduur)[^\n]{0,30}?(\d+(?:\s*(?:tot|à|a|-|–)\s*\d+)?)\s*(werkdagen|dagen|weken)/.exec(t);
    uit.doorlooptijd = dl ? dl[2].replace(/\s*[-–à]\s*/, " tot ") + " " + dl[3] : null;
    uit.concept = /\bconcept\b|indicatie(f|ve)|geschatte\s+hoeveelheden|onder\s+voorbehoud/.test(t);
    var buiten = d.context === "buiten" || d.posten.some(function (p) { return ["buitenkozijn", "buitendeur", "boeidelen", "dakkapel", "steiger", "houtrot"].indexOf(p.type) >= 0; });
    uit.buiten = buiten;
    uit.lijst = {
      lagen: uit.lagen.aantal != null || uit.lagen.grond,
      merk: uit.merken.length > 0,
      voorbereiding: /schuren|ontvet|plamu|kitten|reinig|afplak|afdek|vullen|matteren/.test(t),
      steiger: /steiger|hoogwerker|ladder/.test(t),
      houtrot: /houtrot/.test(t),
      garantie: !!uit.garantie,
      btw: tarieven.length > 0,
      planning: /planning|startdatum|uitvoering|doorlooptijd|oplever|\bweek\s*\d/.test(t),
      geldigheid: !!uit.geldigheid,
      betaling: d.termijnen.length > 0 || !!uit.betaaltermijn || /betaling|betalen|factuur/.test(t)
    };
    return uit;
  }

  function controle(som, basis, totaal, sub, kortingNaSub) {
    var tegen = basis === "incl" ? totaal.incl : totaal.excl;
    if (tegen == null || !som) return { klopt: null, som: som, tegen: tegen, basis: basis };
    var klopt = gelijk(som, tegen, 1.5) || (sub != null && gelijk(som, sub + kortingNaSub, 1.5));
    return { klopt: klopt, som: som, tegen: tegen, verschil: rond(tegen - som), basis: basis };
  }

  var MERKEN = ["sikkens", "sigma", "flexa", "histor", "wijzonol", "trimetal", "boss paints", "rambo", "herbol", "caparol",
    "alpina", "koopmans", "osmo", "ralston", "jotun", "tikkurila", "levis", "copagro", "teknos", "gori", "brillux", "drost", "painting the past", "little greene", "farrow"];
  function zoekMerken(t) {
    var uit = [];
    MERKEN.forEach(function (m) {
      if (new RegExp("\\b" + m + "\\b").test(t)) uit.push(m.replace(/\b\w/g, function (c) { return c.toUpperCase(); }));
    });
    return uit;
  }
  var TELWOORD = { een: 1, "één": 1, twee: 2, drie: 3, vier: 4 };
  function zoekLagen(t) {
    var re = /(\b\d|\been|één|twee|drie|vier)\s*(?:x|keer|maal)?\s*(?:dekkende?\s+|volle\s+)?(?:lagen|laag|laags|aflak(?:ken)?|lakken\b)/g, m, max = null;
    while ((m = re.exec(t))) {
      var n = TELWOORD[m[1]] || parseInt(m[1], 10);
      if (n >= 1 && n <= 4 && (max == null || n > max)) max = n;
    }
    var grond = /grondlaag|grondverf|gronden|primer|voorstrijk|voorlak/.test(t);
    var tekst = max ? max + (max === 1 ? " laag" : " lagen") : "";
    if (grond) tekst += (tekst ? ", " : "") + "met grondlaag of primer";
    return { aantal: max, grond: grond, tekst: tekst || null };
  }
  function zoekGarantie(t) {
    if (/geen\s+garantie/.test(t)) return "geen";
    var m = /(\d+)\s*(jaar|jaren|maanden|mnd)\.?\s*(?:volledige\s+|schriftelijke\s+)?garantie/.exec(t) ||
      /garantie(?:termijn)?[^\n.]{0,45}?(\d+)\s*(jaar|jaren|maanden|mnd)/.exec(t);
    if (!m) return /garantie/.test(t) ? "genoemd, zonder termijn" : null;
    return m[1] + " " + (m[2] === "mnd" ? "maanden" : m[2] === "jaren" ? "jaar" : m[2]);
  }
  function zoekGeldigheid(t) {
    var m = /geldig(?:heid)?[^\n]{0,20}?(t\/m|tot\s+en\s+met|tot|:)?\s*(\d{1,2}[-\/ .]\s?(?:\d{1,2}|[a-z]{3,9}\.?)[-\/ .]\s?\d{2,4})/.exec(t);
    if (m) return (m[1] && m[1] !== ":" ? m[1] + " " : "t/m ") + m[2];
    m = /geldig(?:heid)?[^\n]{0,25}?(\d+)\s*(dagen|weken|maanden)/.exec(t);
    return m ? m[1] + " " + m[2] : null;
  }
  function euro(n) {
    if (n == null || isNaN(n)) return "–";
    var r = Math.round(n * 100) / 100, heel = Math.abs(r) % 1 === 0;
    return (r < 0 ? "−" : "") + "€\u00a0" + Math.abs(r).toLocaleString("nl-NL", { minimumFractionDigits: heel ? 0 : 2, maximumFractionDigits: 2 });
  }

  /* ------------------------------------------------------------ beoordelen */
  var VRAGEN_TYPE = {
    wanden: "Zit gaten vullen en voorstrijken in de prijs per m²?",
    plafonds: "Wordt het plafond in twee lagen gesausd, en zit afplakken van de randen erbij?",
    buitenkozijn: "Gaat het om de buitenkant of beide zijden, en zitten glaslatten en kitwerk erbij?",
    binnenkozijn: "Worden de kozijnen aan beide zijden gelakt?",
    deur: "Worden de deuren aan beide zijden en op de kanten gelakt?",
    buitendeur: "Wordt de deur aan beide zijden en op de kanten gelakt, en met welke buitenlak?",
    dakkapel: "Zit de steiger of hoogwerker voor de dakkapel in deze prijs?",
    boeidelen: "Hoeveel strekkende meter boeidelen is het, en wat kost een meter?",
    glaslatten: "Worden de glaslatten alleen geschilderd, of ook vervangen of opnieuw gekit?",
    kitwerk: "Hoeveel meter kitwerk is het, en wordt de oude kit eerst verwijderd?",
    plinten: "Hoeveel meter plint is het, en wordt er tegen de vloer afgeplakt?",
    keukenfront: "Worden de fronten in de werkplaats gespoten, en zitten de laden erbij?",
    trap: "Gaat het om treden, stootborden én leuning, of maar een deel daarvan?",
    behang: "Zit het behang zelf in de prijs, of alleen het behangen?",
    houtrot: "Hoeveel plekken zijn het, en wat kost een extra plek als er meer rot zit?",
    steiger: "Voor welke gevels en hoeveel dagen is de steiger, en wat als het langer duurt?",
    voorbereiding: "Wat valt er precies onder deze post?",
    uren: "Hoeveel uur is ingeschat, en wat gebeurt er als het meer wordt?",
    materiaal: "Welk merk en hoeveel wordt er geleverd, en wat gebeurt er met wat overblijft?"
  };

  // banden: TS_PRIJSBANDEN (bedragen incl. btw, behalve excl_btw). index: regionale factor.
  function beoordeelPost(p, banden, index, basis, standaardBtw) {
    var type = TYPES[p.type] || TYPES.overig;
    var band = type.band && banden ? banden[type.band] : null;
    var uit = { oordeel: null, reden: null, van: null, tot: null, vergelijk: null, vragen: [] };
    var bedrag = p.bedrag, q = p.aantal;
    if (p.alleenTarief && p.eenheidsprijs != null) { bedrag = p.eenheidsprijs; q = 1; }
    if (VRAGEN_TYPE[p.type]) uit.vragen.push(VRAGEN_TYPE[p.type]);
    if (p.stelpost) uit.vragen.push("Dit is een stelpost: wat gebeurt er als het meer of minder wordt?");
    if (p.btw === 21 && !type.materiaal && p.type !== "korting" && p.type !== "overig")
      uit.vragen.push("Waarom staat hier 21% btw op? Voor schilderwerk aan een woning ouder dan twee jaar geldt 9%.");
    if (!band) { uit.reden = p.type === "korting" ? "korting" : "geen richtprijs"; return uit; }
    if (bedrag == null) { uit.reden = "geen bedrag"; return uit; }
    var eenheid = p.eenheid || (p.type === "steiger" ? "post" : null);
    if (p.type === "steiger") { q = q || 1; eenheid = type.eenheid; }
    if (p.type === "trap" && !q) { q = 1; eenheid = "st"; }
    if (p.type === "houtrot" && eenheid === "post") eenheid = null;
    if (!q || q <= 0) { uit.reden = "geen aantal"; return uit; }
    if (eenheid !== type.eenheid && !(p.alleenTarief && (p.eenheid === type.eenheid || !p.eenheid))) { uit.reden = "andere eenheid"; return uit; }
    var tarief = (p.btw != null ? p.btw : (standaardBtw || 9)) / 100;
    var vgl = band.excl_btw ? (basis === "incl" ? bedrag / (1 + tarief) : bedrag) : (basis === "incl" ? bedrag : bedrag * (1 + tarief));
    index = index || 1;
    uit.van = Math.round(band.van * index * q); uit.tot = Math.round(band.tot * index * q); uit.vergelijk = vgl;
    uit.inclBtw = !band.excl_btw;
    uit.oordeel = vgl < uit.van * 0.9 ? "laag" : vgl > uit.tot * 1.1 ? "hoog" : "binnen";
    if (uit.oordeel === "hoog") uit.vragen.unshift("Deze post ligt boven de richtprijs. Vraag wat er precies in zit, bijvoorbeeld extra voorwerk of slecht hout.");
    if (uit.oordeel === "laag") uit.vragen.unshift("Deze post ligt onder de richtprijs. Check of alle lagen en het voorwerk erin zitten.");
    return uit;
  }

  // Vragen over de offerte als geheel. lijst: wat er volgens de gebruiker in staat.
  function algemeneVragen(res, lijst) {
    lijst = lijst || res.lijst;
    var v = [];
    if (!lijst.lagen) v.push("Hoeveel lagen worden er gezet, en komt er een grondlaag op kale plekken?");
    if (!lijst.merk) v.push("Welk verfmerk en welk type verf gebruik je?");
    if (!lijst.voorbereiding) v.push("Wat zit er aan voorbereiding in de prijs: schuren, ontvetten, gaten vullen, kitten?");
    if (res.buiten && !lijst.steiger) v.push("Zit de steiger of hoogwerker in de prijs?");
    if (res.buiten && !lijst.houtrot) v.push("Hoe reken je houtrot af als je het tegenkomt: per plek, per uur of als stelpost?");
    if (!lijst.garantie) v.push("Hoe lang is de garantie, en waarop geldt die?");
    else if (res.garantie === "genoemd, zonder termijn") v.push("Er staat garantie, maar geen termijn. Hoe lang geldt die, en waarop?");
    if (!lijst.btw) v.push("Welk btw-tarief reken je? Voor schilderwerk aan een woning ouder dan twee jaar is dat 9%.");
    if (!lijst.planning) v.push("Wanneer kun je beginnen en hoe lang duurt het werk?");
    if (lijst.geldigheid === false) v.push("Hoe lang is deze offerte geldig?");
    if (lijst.betaling === false) v.push("Wanneer betaal ik: in termijnen of na oplevering?");
    var vooraf = (res.termijnen || []).filter(function (x) { return /start|aanvang|opdracht|akkoord|aanbetaling|ondertekening/i.test(x.omschrijving); })
      .reduce(function (s, x) { return s + (x.procent || 0); }, 0);
    if (vooraf >= 50) v.push("Je betaalt " + vooraf + "% voordat het werk klaar is. Vraag of een kleiner deel vooraf kan.");
    if (res.concept) v.push("De offerte noemt geschatte hoeveelheden of is een concept. Vraag na de opname om een vaste prijs.");
    if (res.controle && res.controle.klopt === false) v.push("De losse posten tellen niet op tot het totaal. Vraag de schilder waar het verschil zit.");
    if ((res.btwTarieven || []).indexOf(21) >= 0 && (res.posten || []).some(function (p) { return p.btw == null && p.type !== "materiaal"; }) && (res.btwTarieven || []).indexOf(9) < 0)
      v.push("Er wordt 21% btw gerekend. Voor schilderwerk aan een woning ouder dan twee jaar geldt 9%: vraag waarom het hier 21% is.");
    return v;
  }

  /* ------------------------------------------------------------ pdf.js-tekst naar regels */
  // items: textContent.items van één pagina. Groepeert op hoogte met tolerantie en
  // zet een dubbele spatie tussen kolommen.
  function regelsUitItems(items) {
    var lijst = items.filter(function (it) { return it.str && it.str.trim(); }).map(function (it) {
      var h = Math.abs(it.height || it.transform[3] || 10);
      return { s: it.str, x: it.transform[4], y: it.transform[5], w: it.width || 0, h: h };
    }).sort(function (a, b) { return b.y - a.y || a.x - b.x; });
    var regels = [];
    lijst.forEach(function (it) {
      var r = regels.length && regels[regels.length - 1];
      if (r && Math.abs(r.y - it.y) <= Math.max(2, Math.min(r.h, it.h) * 0.45)) r.items.push(it);
      else regels.push({ y: it.y, h: it.h, items: [it] });
    });
    return regels.map(function (r) {
      r.items.sort(function (a, b) { return a.x - b.x; });
      var s = "", eind = null;
      r.items.forEach(function (it) {
        if (eind != null) {
          var gat = it.x - eind;
          s += gat > it.h * 1.5 ? "   " : (gat > it.h * 0.15 && !/\s$/.test(s) && !/^\s/.test(it.s) ? " " : "");
        }
        s += it.s;
        eind = it.x + it.w;
      });
      return s.replace(/\s+$/, "");
    }).join("\n");
  }

  return {
    TYPES: TYPES, EENHEDEN: EENHEDEN, getal: getal, euro: euro, leesOfferte: leesOfferte,
    beoordeelPost: beoordeelPost, algemeneVragen: algemeneVragen, regelsUitItems: regelsUitItems,
    bepaalType: bepaalType, controle: controle
  };
});

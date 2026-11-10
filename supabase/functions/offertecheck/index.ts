// Topschilder offertecheck — Supabase Edge Function (Deno).
//
// Ontvangt een schildersofferte (pdf, foto of geplakte tekst), laat Claude de
// posten eruit halen en stuurt die gestructureerd terug. De vergelijking met
// de richtprijzen gebeurt in de browser (assets.py, OFFERTECHECK-blok).
//
// Er wordt niets opgeslagen: de offerte gaat alleen naar de Claude API en het
// antwoord gaat direct terug naar de bezoeker.
//
// Instellen: zie supabase/functions/offertecheck/LEESMIJ.md

import Anthropic from "npm:@anthropic-ai/sdk";
import { z } from "npm:zod";
import { zodOutputFormat } from "npm:@anthropic-ai/sdk/helpers/zod";

const MODEL = Deno.env.get("OFFERTECHECK_MODEL") ?? "claude-opus-5-5";
const MAX_BYTES = 6 * 1024 * 1024; // 6 MB per bestand
const MAX_TEKST = 20_000; // tekens bij geplakte tekst
const TOEGESTAAN = ["https://topschilder.nl", "https://www.topschilder.nl"];
const EXTRA_ORIGIN = Deno.env.get("OFFERTECHECK_EXTRA_ORIGIN"); // bv. http://localhost:8000 om te testen
const TYPES: Record<string, "pdf" | "image"> = {
  "application/pdf": "pdf",
  "image/jpeg": "image",
  "image/png": "image",
  "image/webp": "image",
};

// Moet gelijk blijven aan PRIJSBANDEN in kosten_data.py.
const CATEGORIEEN = [
  "muren_plafonds_m2",
  "buitenkozijn",
  "binnenkozijn",
  "deur",
  "keukenfront",
  "trap",
  "houtrot_plek",
  "behang_m2",
  "uurloon",
  "steiger",
  "anders",
] as const;

const Offerte = z.object({
  leesbaar: z.boolean().describe("false als dit geen schildersofferte is of als je hem niet kunt lezen"),
  posten: z.array(z.object({
    categorie: z.enum(CATEGORIEEN),
    omschrijving: z.string().describe("korte omschrijving van de post, zonder namen of adressen"),
    hoeveelheid: z.number().nullable().describe("aantal in de eenheid van de categorie, null als onbekend"),
    bedrag_excl_btw: z.number().nullable(),
    bedrag_incl_btw: z.number().nullable(),
  })),
  totaal_excl_btw: z.number().nullable(),
  totaal_incl_btw: z.number().nullable(),
  btw_percentage: z.number().nullable().describe("het btw-percentage op het schilderwerk, bv. 9 of 21"),
  ontbrekend: z.array(z.string()).describe("wat er niet in de offerte staat maar er wel in hoort"),
  aandachtspunten: z.array(z.string()).describe("vage formuleringen, opvallende posten, btw die niet klopt"),
  samenvatting: z.string().describe("twee of drie zinnen in gewone taal"),
});

const SYSTEEM = `Je leest Nederlandse offertes van schilders voor een vergelijkingssite.
Haal de posten eruit en deel elke post in bij één categorie. Gebruik voor de hoeveelheid de eenheid van die categorie:
- muren_plafonds_m2: binnenmuren en plafonds, in m²
- buitenkozijn: buitenkozijnen inclusief ramen en dorpels, per stuk
- binnenkozijn: binnenkozijnen en deurkozijnen binnen, per stuk
- deur: losse deuren schilderen of spuiten, per stuk
- keukenfront: keukendeurtjes en lades, per front
- trap: een complete trap, per trap
- houtrot_plek: houtrotreparatie, per reparatieplek
- behang_m2: behangen inclusief behang, in m²
- uurloon: werk op regie, in uren
- steiger: steiger of hoogwerker, hoeveelheid 1
- anders: al het andere, of als een post meerdere categorieën samenvoegt
Neem bedragen alleen over als ze er echt staan. Reken niets bij en verzin geen hoeveelheden: onbekend is null.
Als één bedrag voor meerdere soorten werk geldt, gebruik dan "anders".
Bij ontbrekend kijk je naar: aantal lagen, verfmerk en type, voorbereiding, steiger, afrekening van houtrot, btw-splitsing, garantie, planning, betaalvoorwaarden.
Schilderwerk aan een woning ouder dan twee jaar valt onder 9% btw; houten inzetstukken, onderdorpels en de levering van behang onder 21%.
Neem nooit namen, adressen, telefoonnummers, e-mailadressen of bedrijfsnamen over in je antwoord.
Schrijf in eenvoudig Nederlands, kort en zonder jargon.`;

const client = new Anthropic(); // leest ANTHROPIC_API_KEY uit de secrets

function cors(origin: string | null): Record<string, string> {
  const toegestaan = origin && (TOEGESTAAN.includes(origin) || origin === EXTRA_ORIGIN);
  return {
    "Access-Control-Allow-Origin": toegestaan ? origin! : TOEGESTAAN[0],
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "authorization, apikey, content-type, x-client-info",
    "Vary": "Origin",
  };
}

function antwoord(body: unknown, status: number, headers: Record<string, string>): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...headers, "Content-Type": "application/json" },
  });
}

Deno.serve(async (req) => {
  const origin = req.headers.get("origin");
  const headers = cors(origin);
  if (req.method === "OPTIONS") return new Response(null, { headers });
  if (req.method !== "POST") return antwoord({ fout: "Alleen POST" }, 405, headers);
  if (!origin || !(TOEGESTAAN.includes(origin) || origin === EXTRA_ORIGIN)) {
    return antwoord({ fout: "Niet toegestaan" }, 403, headers);
  }

  let invoer: { bestand?: { type: string; data: string }; tekst?: string };
  try {
    invoer = await req.json();
  } catch {
    return antwoord({ fout: "Ongeldige aanvraag" }, 400, headers);
  }

  const inhoud: Anthropic.ContentBlockParam[] = [];
  if (invoer.bestand) {
    const soort = TYPES[invoer.bestand.type];
    if (!soort) return antwoord({ fout: "Upload een pdf, jpg, png of webp." }, 415, headers);
    if (invoer.bestand.data.length * 0.75 > MAX_BYTES) {
      return antwoord({ fout: "Het bestand is te groot. Maximaal 6 MB." }, 413, headers);
    }
    inhoud.push(soort === "pdf"
      ? { type: "document", source: { type: "base64", media_type: "application/pdf", data: invoer.bestand.data } }
      : {
        type: "image",
        source: {
          type: "base64",
          media_type: invoer.bestand.type as "image/jpeg" | "image/png" | "image/webp",
          data: invoer.bestand.data,
        },
      });
  } else if (invoer.tekst && invoer.tekst.trim().length > 20) {
    inhoud.push({ type: "text", text: "Offertetekst:\n" + invoer.tekst.slice(0, MAX_TEKST) });
  } else {
    return antwoord({ fout: "Upload een offerte of plak de tekst." }, 400, headers);
  }
  inhoud.push({ type: "text", text: "Lees deze schildersofferte uit volgens de instructies." });

  try {
    const res = await client.messages.parse({
      model: MODEL,
      max_tokens: 8000,
      system: SYSTEEM,
      output_config: { effort: "low", format: zodOutputFormat(Offerte) },
      messages: [{ role: "user", content: inhoud }],
    });
    if (res.stop_reason === "refusal") {
      return antwoord({ fout: "Deze offerte konden we niet automatisch lezen." }, 422, headers);
    }
    if (!res.parsed_output) {
      return antwoord({ fout: "Het uitlezen is niet gelukt. Probeer het opnieuw of plak de tekst." }, 502, headers);
    }
    return antwoord({ ok: true, offerte: res.parsed_output }, 200, headers);
  } catch (e) {
    console.error("offertecheck", e instanceof Error ? e.message : e);
    return antwoord({ fout: "Er ging iets mis. Probeer het later opnieuw." }, 502, headers);
  }
});

# Topschilder.nl

Statische leadgeneratie-site voor schilderwerk. 263 pagina's, gegenereerd uit
`data.py` — geen CMS, geen database bij het laden.

## Hoe het werkt

```
data.py        →  alle content: diensten, plaatsen, prijzen, bedrijfsgegevens
components.py  →  herbruikbare HTML-blokken (header, formulier, FAQ, footer)
assets.py      →  CSS, JavaScript, favicon en de Supabase-koppeling
build.py       →  genereert de complete site in site/
verify.py      →  controleert links, dubbele titles, JSON-LD en sitemap
```

Lokaal draaien:

```bash
python3 build.py     # bouwt site/
python3 verify.py    # moet eindigen met "ALLES OK"
```

Push naar `main` en GitHub Actions bouwt en publiceert automatisch. Als
`verify.py` een fout vindt, wordt er niets gepubliceerd.

## Iets aanpassen

| Wat | Waar |
|---|---|
| Nieuwe plaats | `PLAATSEN` in `data.py` (levert automatisch 7 pagina's op) |
| Nieuwe dienst | `DIENSTEN` in `data.py` |
| Prijzen | `prijs_van` / `prijs_tot` in `data.py`, regio via `PRIJSINDEX` |
| Bedrijfsgegevens, KvK, btw | `SITE` bovenaan `data.py` |
| Supabase-koppeling | `CONFIG_JS` in `assets.py` |
| Vormgeving | `STYLE_CSS` in `assets.py` |

## Leads

Formulieren schrijven naar Supabase. Het schema staat in `supabase_schema.sql`
— Row Level Security met alleen insert-rechten, dus de anon key in `config.js`
is veilig om publiek te hebben.

Zie `STARTGIDS.md` voor de volledige uitleg, marktdata en het verdienmodel.

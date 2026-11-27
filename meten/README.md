# Meten (SEO-ronde 5)

Hulpscripts om de site te meten. Ze horen niet bij de build en veranderen niets.

```bash
python3 build.py
python3 meten/seo_audit.py site            # titels, descriptions, links, klikdiepte, schema, gewicht
LINKS=1 python3 meten/seo_audit.py site    # plus pagina's met de minste inkomende links

python3 meten/serve_gzip.py site 8847 &    # lokale server met gzip, zoals GitHub Pages
node meten/perf.mjs http://127.0.0.1:8847 / /kosten/ /schilder/zwolle/
W=1350 node meten/perf_desktop.mjs http://127.0.0.1:8847 / /kosten/
```

`perf.mjs` start headless Chrome (uit /Applications) en meet per pagina FCP, LCP, CLS, TBT
(long tasks), bytes en het LCP-element. Mobiel: 412 px breed, 150 ms latentie, 1,6 Mbit/s en
een 4x tragere CPU. De eerste URL is altijd trager (koude start): zet er een wegwerp-URL voor.
Met `EXPR="..."` geef je een JavaScript-expressie mee waarvan de uitkomst in kolom `x` komt.

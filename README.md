# Nut in my bar — fase 0/1
Eigen Shopify Online Store 2.0-thema voor een veilige merkverkenning. Neon-groene verpakkingen, zwart/warmwit, grote typografie en droge copy. Alle smaken en beelden zijn **concepten**; prijzen en voedingsinformatie zijn nog niet vastgesteld.

## Structuur
- `theme/`: uploadbare theme-root met assets, config, layout, locales, sections, snippets en templates.
- `content/concepts.json`: interne conceptnotities; geen Shopify-productimport.
- `preview/index.html`: zelfstandige desktop/mobile visualisatie van dezelfde sectiemarkup en CSS.
- `scripts/`: controles en reproduceerbare preview zonder npm-dependencies.
- `docs/`: testgrenzen en Shopify-overdracht.

## Direct starten
```sh
python3 scripts/check.py
python3 scripts/preview.py
python3 -m http.server 8000 --directory preview
```
Open http://localhost:8000. Controleer 390px mobiel en 1440px desktop, toetsenbordnavigatie en de ankerlinks. De preview is geen Shopify-runtime.

## Shopify (pas met development store)
Installeer de officiële Shopify CLI volgens https://shopify.dev/docs/api/shopify-cli en voer uit:
```sh
shopify theme check --path theme
shopify theme dev --path theme --store YOUR-DEVELOPMENT-STORE.myshopify.com
```
Theme Check en echte Shopify-rendering zijn nog niet uitgevoerd. Gebruik uitsluitend een development store of ongepubliceerd thema; geen `theme publish`, productimport of live-theme-push. Stel winkelwachtwoord en betalingen in Shopify Admin apart veilig in. Dit thema is geen beveiligingsgrens voor bestaande Shopify-producten of checkout.

Zie docs/VALIDATION.md en docs/SHOPIFY_HANDOFF.md voor ontbrekende informatie en acceptatie.

# Validatie — fase 0/1
## Uitvoerbaar zonder Shopify
`python3 scripts/check.py`: JSON en sectieschema’s parsen, template- en snippetverwijzingen controleren, layout-hooks en broncode-prelaunchguard controleren.
`python3 scripts/preview.py`: dezelfde markup en CSS naar zelfstandige HTML renderen; controleert achtergebleven Liquid-placeholders. Dit is een beperkte project-specifieke vervanging, geen Liquid-engine.

## Handmatige desktop/mobile acceptatie
Open preview/index.html op 1440px en 390px (ook 320px): geen horizontale scroll, hero leesbaar, drie kaarten op mobiel onder elkaar, Starter Mix zichtbaar. Tab vanaf skip-link door navigatie en CTA’s; Enter/Space opent FAQ. Controleer kleurcontrast, 200% zoom en verminderde beweging. De geautomatiseerde browsercheck is geprobeerd, maar kon niet starten doordat Chromium niet geïnstalleerd is. Er zijn geen screenshots of geslaagde browserresultaten. Herhaal met Playwright en Chromium: `node scripts/browser-check.cjs`.

## Nog niet getest
Shopify Theme Check, Liquid-rendering, theme-editor save/reorder, content_for_header-injecties, echte asset-URLs, wachtwoord-route en andere Shopify-routes. Hiervoor zijn Shopify CLI en development-storeconfiguratie nodig. Geen Lighthouse- of WCAG-conformiteitsclaim.

## Resultaat lokale controles
JSON/schema/referentie- en prelaunchbroncontroles: geslaagd. Previewgeneratie: geslaagd. Er zijn geen actieve product-, betaal-, cart- of publicatie-integraties.

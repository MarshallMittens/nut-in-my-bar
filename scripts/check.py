from pathlib import Path
import json,re
r=Path(__file__).resolve().parents[1]; t=r/'theme'
for p in t.rglob('*.json'): json.loads(p.read_text())
for p in (t/'sections').glob('*.liquid'):
 s=p.read_text(); assert s.count('{% schema %}')==1,p
 json.loads(s.split('{% schema %}')[1].split('{% endschema %}')[0])
for p in (t/'templates').glob('*.json'):
 d=json.loads(p.read_text()); assert set(d['order'])==set(d['sections']),p
 for s in d['sections'].values(): assert (t/'sections'/f"{s['type']}.liquid").exists(),p
for p in t.rglob('*.liquid'):
 s=p.read_text()
 for name in re.findall(r"{% render '([^']+)' %}",s): assert (t/'snippets'/f'{name}.liquid').exists(),p
 assert not re.search(r'cart/add|/checkout|https?://|form[ \t]+[\'"]product',s),p
layout=(t/'layout/theme.liquid').read_text()
assert '{{ content_for_header }}' in layout and '{{ content_for_layout }}' in layout
print('PASS: JSON, schemas, template/snippet references, layout hooks and prelaunch source guard.')
print('Not tested: Shopify Liquid runtime, Theme Check, editor, browser layout or live store settings.')

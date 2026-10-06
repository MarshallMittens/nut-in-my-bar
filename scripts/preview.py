"""Static illustration, not a Liquid runtime. Reuses section HTML and theme CSS."""
from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parents[1]
T=ROOT/'theme'
def render(name,values=None):
 raw=(T/'sections'/f'{name}.liquid').read_text()
 markup,schema=raw.split('{% schema %}')
 schema=json.loads(schema.split('{% endschema %}')[0])
 settings={s['id']:s.get('default','') for s in schema.get('settings',[])}
 settings.update((values or {}).get('settings',{}))
 markup=markup.replace("{% render 'pack' %}",(T/'snippets/pack.liquid').read_text()).replace('{{ routes.root_url }}','./index.html')
 def replace(m):return html.escape(str(settings[m[1]]))
 markup=re.sub(r'{{ section.settings.(\w+) \| escape }}',replace,markup)
 loop=re.search(r'{% for block in section.blocks %}(.*?){% endfor %}',markup,re.S)
 if loop:
  pieces=[]
  for key in values['block_order']:
   b=values['blocks'][key]['settings']; s=loop[1].replace('{{ block.shopify_attributes }}','')
   s=re.sub(r'{{ block.settings.(\w+) \| escape }}',lambda m:html.escape(b[m[1]]),s);pieces.append(s)
  markup=markup[:loop.start()]+''.join(pieces)+markup[loop.end():]
 return markup
index=json.loads((T/'templates/index.json').read_text())
body=render('header')+'<main id="MainContent" tabindex="-1">'+''.join(render(index['sections'][k]['type'],index['sections'][k]) for k in index['order'])+'</main>'+render('footer')
css=(T/'assets/theme.css').read_text()
out=ROOT/'preview/index.html';out.parent.mkdir(exist_ok=True)
out.write_text('<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Nut in my bar — conceptpreview</title><style>'+css+'</style></head><body><a class="skip-link" href="#MainContent">Ga naar inhoud</a>'+body+'</body></html>')
assert '{{' not in body and '{%' not in body
print('Preview generated:',out)

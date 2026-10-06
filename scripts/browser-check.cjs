// Optional: requires Playwright and an installed Chromium. No runtime dependency for theme.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
 const browser = await chromium.launch({headless:true});
 fs.mkdirSync(path.join(__dirname,'../preview'),{recursive:true});
 for (const [name,width,height] of [['desktop',1440,1000],['mobile',390,844],['small-mobile',320,780]]) {
  const page = await browser.newPage({viewport:{width,height}});
  const errors=[]; page.on('pageerror',e=>errors.push(e.message));
  await page.goto('file://'+path.resolve(__dirname,'../preview/index.html'));
  if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)) throw Error(name+': horizontal overflow');
  await page.keyboard.press('Tab');
  if(await page.locator('.skip-link').evaluate(el=>el!==document.activeElement)) throw Error('skip-link focus');
  await page.keyboard.press('Enter');
  await page.locator('summary').first().click();
  if(!await page.locator('details').first().evaluate(el=>el.open)) throw Error('FAQ');
  await page.locator('details').first().evaluate(el=>el.open=false);
  if(errors.length) throw Error(errors.join('\n'));
  await page.screenshot({path:path.join(__dirname,'../preview',name+'.png'),fullPage:true});
  console.log('PASS',name,width+'px: no overflow, skip-link focus, FAQ toggle, no page errors');
  await page.close();
 }
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});

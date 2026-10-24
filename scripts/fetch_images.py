import os, re, urllib.parse, urllib.request, io
from PIL import Image
# name, host, path, signature, crop centre (0-1), crop width (0-1)
SRC=[
  ('agb-ivory','p16','tos-alisg-p-0037/oEFQAFhADLKNNRFIQqIGfReGQfubAHFjGQAfXG~tplv-tiktokx-origin.image','pxCSzhCKpVE0LA0+ubu2n2yzaYg=',0.55,0.92),
  ('agb-gold','p16','tos-alisg-p-0037/okCrEfsuDBGqF3HEgbE19HI5mBUIAeRguORPdA~tplv-tiktokx-origin.image','OMLemZBOe2BW0TxlhVGFhwe7uLI=',0.5,1.0),
  ('agb-sage','p16','tos-alisg-p-0037/oUlRudEBHslHL1cgEIV7hHgIDfADFBEpfB2qYI~tplv-tiktokx-origin.image','jZ4gnkVlsImngd6lXe6ah87fgpw=',0.52,1.0),
  ('kft-wine','p16','tos-alisg-p-0037/oUDU5UHxIBB1eIEXXfRiEG5BSkjVIga2DSAqFq~tplv-tiktokx-origin.image','CdTjYJX9p+0nPwccKigwi0G1uFM=',0.56,0.86),
  ('kft-wine-2','p19','tos-alisg-p-0037/oYiMEE69oBIAdA28coVNPJIDiBsiaI63XY3Tt~tplv-tiktokx-origin.image','O5oM63CS/YgtI8+pzhxiH+9LPaQ=',0.6,0.9),
  ('kft-cocoa','p16','tos-alisg-p-0037/owP1z92jxAY1DIhJwIiiJmqB3fE7Y9ciACAJLI~tplv-tiktokx-origin.image','McQHGIMz7yrCGzVlxBjf96Qd764=',0.52,0.92),
  ('kft-cream','p16','tos-alisg-p-0037/o8herLmeAtQjCGLeQCuDzhjmaAIIlUz4AHCWQ0~tplv-tiktokx-origin.image','Dj30/JgIc7p5vJe24X05q6IMXN8=',0.52,0.92),
  ('kft-white','p16','tos-alisg-p-0037/oMvVaaaqyRA4EYVFtUJXOUGBCiJAlBpiIIuup~tplv-tiktokx-origin.image','FR1U3wTNXYs0R55hfFP/CxHgyk0=',0.5,1.0),
  ('kft-midnight','p16','tos-alisg-p-0037/ok1QQQLxAAtBGBTBGLeslqGF4bzWeIRxea8fLn~tplv-tiktokx-origin.image','gu98EO74Xr62Mog8GU5EQtGAg5s=',0.52,1.0),
  ('sen-sky','p16','tos-alisg-p-0037/ogSfdFWhAcSR0DqXIf1BMDNhnoEE0qdcgEBRIC~tplv-tiktokx-origin.image','D0Z95ozqx6i5yW0tf9XI8ZpqkSE=',0.58,0.86),
  ('sen-slate','p16','tos-alisg-p-0037/o4DNY7f1HijAqFWEZyiBABc8EjQBGQ3gRa8sMe~tplv-tiktokx-origin.image','NRVEM2g0/zD753Kg6imfEL8nH98=',0.5,0.92),
  ('sen-safari','p16','tos-alisg-p-0037/o8A0HM4aNgfeEfYYglfASpY7tf4IBXfaVgTHQN~tplv-tiktokx-origin.image','IrlAx0hMVz9W2vud5xwtBMnEyCQ=',0.52,0.92),
  ('cap-emb','p16','tos-alisg-p-0037/oQ7MeqEIIBgqIPrfmHFctc2mEx7pxEAHDBRREj~tplv-tiktokx-origin.image','EaqDo0xLWVaSS9KqyIjYYdQGs5E=',0.42,1.0),
  ('look-gold','p16','tos-alisg-p-0037/osoj5YiaRAMh31BAiVXqNdaNKBKEaIpPjIEvZ~tplv-tiktokx-origin.image','apQx+GahkG0M4PMy2oiiaGX5/uM=',0.55,1.0),
  ('look-royal','p16','tos-alisg-p-0037/owrHR4i9qIUrEiBfjBRFS5pEIlDElMAJCgflHd~tplv-tiktokx-origin.image','5Q2s/vQeSCYcVnCuqqWSV4J6CKM=',0.55,1.0),
  ('look-teal','p16','tos-alisg-p-0037/o4HeeAGGQyYDDLjSVB0VNRgIAgS0CmegN1GmIm~tplv-tiktokx-origin.image','L4JBm+IpadlPZg/PEgGt0vsMFUg=',0.55,1.0),
  ('look-mustard','p19','tos-alisg-p-0037/oMLkaFBvN5PVVIkBHUEvA3G7iAY71kEzcuijI~tplv-tiktokx-origin.image','kJB+9QE+GBLC+/iiRENgrK87P4o=',0.55,1.0),
]
os.makedirs('img2',exist_ok=True)
for n,h,p,sig,cy,z in SRC:
    out=f'img2/{n}.webp'
    if os.path.exists(out): continue
    q={'dr':'14575','x-expires':'1793005200','x-signature':sig,'t':'4d5b0474','ps':'13740610','shp':'81f88b70','shcp':'43f4a2f9','idc':'my2'}
    url=f'https://{h}-common-sign.tiktokcdn.com/{p}?'+urllib.parse.urlencode(q)
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0','Referer':'https://www.tiktok.com/'})
    im=Image.open(io.BytesIO(urllib.request.urlopen(req,timeout=60).read())).convert('RGB')
    W,H=im.size; cw=int(W*z); ch=int(cw*4/3); top=int(min(max(cy*H-ch/2,0),H-ch)); left=(W-cw)//2
    im.crop((left,top,left+cw,top+ch)).resize((750,1000),Image.LANCZOS).save(out,quality=78,method=6)
    print('saved',out)
html=open('index.html',encoding='utf-8').read()
m=re.search(r'<symbol id="bmark" viewBox="([^"]+)"><path fill-rule="evenodd" d="([^"]+)"',html)
if m and not os.path.exists('favicon.svg'):
    open('favicon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{m.group(1)}"><path fill="#17130F" fill-rule="evenodd" d="{m.group(2)}"/></svg>')

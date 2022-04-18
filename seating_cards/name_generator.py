from PIL import Image, ImageDraw, ImageFont
from pil_drawer import PilDrawer
from background_drawer import BackgroundDrawer
import math
import constants as c

def init_image():
    #the image size should be set as a default, since all cards shall be the same size
    return Image.new('RGB', (c.image_w, c.image_h), color = (0,31,115))

img = init_image()
d = ImageDraw.Draw(img)

bgd = BackgroundDrawer(d)
pd = PilDrawer(d)

bgd.img_w(c.image_w).img_h(c.image_h).head_d(c.head_d).padding(c.padding)

bgd.print_background()


#set size for the whole image text as a variable, calculated from the text
size = 100 
fnt = ImageFont.truetype('assets/Minnie.TTF', size)

text = 'Bendegúz. De amit az Isti rair nekem. Irodalom fuzetre egyszer azt irta hogy Bendicica'

text_area_w = c.image_w - c.head_d * 2 - c.padding * 2
text_area_h = c.image_h - c.padding * 2
text_area_start_w = c.padding + c.head_d
text_area_start_h = c.padding

words = text.split()
current = ''
newText = ''
texts = []
for w in words:
    if(len(current) > 0):
        newText = ' '.join([current, w])
    else:
        newText = w
    if(d.textlength(newText, font=fnt) > text_area_w):
        texts.append(current)
        newText = ''
        current = w
    else:
        current = newText

texts.append(current)

row = 0
text_cnt = len(texts)
h_offset = (text_area_h - text_cnt * size) / 2 - size


pd.rectangle(text_area_start_w, text_area_start_h, text_area_w, text_area_h, 'red')
pd.rectangle(text_area_start_w, text_area_start_h, text_area_w/2, text_area_h/2, 'green')

for t in texts:
    row += 1
    w_offset = (text_area_w - d.textlength(t, font=fnt)) / 2
    x = text_area_start_w + w_offset
    y = h_offset + text_area_start_h + row * size
    for c in t:
        pd.print_char(c, (x,y), fnt)
        last_char_length = d.textlength(c, font=fnt)
        x += last_char_length

img.save('out/test.png')




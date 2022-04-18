from PIL import Image, ImageDraw, ImageFont
from pil_drawer import PilDrawer
from background_drawer import BackgroundDrawer
import constants as c
import utils as u

def init_image():
    #the image size should be set as a default, since all cards shall be the same size
    return Image.new('RGB', (c.image_w, c.image_h), color = (0,31,115))

text_area_w = c.image_w - c.head_d * 2 - c.padding * 2
text_area_h = c.image_h - c.padding * 2
text_area_start_w = c.padding + c.head_d
text_area_start_h = c.padding

img = init_image()
d = ImageDraw.Draw(img)

bgd = BackgroundDrawer(d)
pd = PilDrawer(d)

bgd.img_w(c.image_w).img_h(c.image_h).head_d(c.head_d).padding(c.padding)

bgd.print_background()

text = 'Árvíztűrőtükörfúrógép'

words = text.split()

pd.rectangle(text_area_start_w, text_area_start_h, text_area_w, text_area_h, 'red')

#calculate text size and font, also creating rows for the text
size = text_area_h 
fnt = ImageFont.truetype('assets/Minnie.TTF', size)
fits = False
while( not fits ):
    too_long_word = False
    current = ''
    newText = ''
    rows = []
    for w in words:
        unaccented_word = u.unaccent_word(w)
        print ('unaccented_word: {}, text_area: {}, text: {}'.format(unaccented_word, text_area_w, d.textlength(unaccented_word, font = fnt)))
        if(d.textlength(unaccented_word, font=fnt) > text_area_w):
            too_long_word = True
            # print('too long word')
            break
        if(len(current) > 0):
            newText = ' '.join([current, w])
        else:
            newText = w
        
        if(d.textlength(newText, font=fnt) > text_area_w):
            if(len(current) > 0):
                rows.append(current)
            newText = ''
            current = w
        else:
            current = newText
    rows.append(current)
    text_height = len(rows) * size * c.row_offset
    # print('size: {0}, text_area: {1}, text_size: {2}'.format(size,text_area_h, text_height))

    if(not too_long_word and text_height <= text_area_h):
        fits = True
    else :
        size = size - 2
        fnt = ImageFont.truetype('assets/Minnie.TTF', size)


#print rows into the text area
row = 0
text_cnt = len(rows)
h_offset = (text_area_h - text_cnt * size * c.row_offset) / 2

for t in rows:
    w_offset = (text_area_w - d.textlength(u.unaccent_word(t), font=fnt)) / 2
    x = text_area_start_w + w_offset
    y = h_offset + text_area_start_h + row * size * c.row_offset
    for char in t:
        pd.print_char(char, (x,y), fnt, size)
        last_char_length = d.textlength(c.character_counterparts.get(char,char), font=fnt)
        x += last_char_length
    row += 1

img.save('out/test.png')




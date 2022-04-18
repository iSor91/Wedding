from PIL import Image, ImageDraw, ImageFont
from pil_drawer import PilDrawer
from background_drawer import BackgroundDrawer
import math
import constants as c

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

text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
words = text.split()
#set size for the whole image text as a variable, calculated from the text
size = 110
fnt = ImageFont.truetype('assets/Minnie.TTF', size)
fits = False
while( not fits ):
    

    current = ''
    newText = ''
    texts = []
    for w in words:
        if(len(current) > 0):
            newText = ' '.join([current, w])
        else:
            newText = w
        if(d.textlength(newText + ' ', font=fnt) > text_area_w):
            texts.append(current)
            newText = ''
            current = w
        else:
            current = newText

    texts.append(current)

    text_height = len(texts) * size * c.row_offset
    print('size: {0}, text_area: {1}, text_size: {2}'.format(size,text_area_h, text_height))

    if(text_height <= text_area_h):
        fits = True
    else :
        size = size - 10
        fnt = ImageFont.truetype('assets/Minnie.TTF', size)

row = 0
text_cnt = len(texts)
h_offset = (text_area_h - text_cnt * size * c.row_offset) / 2 - size

for t in texts:
    row += 1
    w_offset = (text_area_w - d.textlength(t + ' ', font=fnt)) / 2
    x = text_area_start_w + w_offset
    y = h_offset + text_area_start_h + row * size * c.row_offset
    for char in t:
        pd.print_char(char, (x,y), fnt, size)
        last_char_length = d.textlength(c.character_counterparts.get(char,char), font=fnt)
        x += last_char_length

img.save('out/test.png')




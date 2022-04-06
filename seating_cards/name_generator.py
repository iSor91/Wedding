from PIL import Image, ImageDraw, ImageFont
from pil_drawer import PilDrawer
from background_drawer import BackgroundDrawer
import math

image_w = 1920 #full image width
image_h = 1080 #full image height
head_d  = 450  #head circle diameter
padding = 50   #padding on the image


def init_image():
    #the image size should be set as a default, since all cards shall be the same size
    return Image.new('RGB', (image_w, image_h), color = (0,31,115))

img = init_image()
d = ImageDraw.Draw(img)

bgd = BackgroundDrawer(d)
pd = PilDrawer(d)

bgd.img_w(image_w).img_h(image_h).head_d(head_d).padding(padding)

bgd.print_background()


#set size for the whole image text as a variable, calculated from the text
size = 100 
x=size
y=size
fnt = ImageFont.truetype('assets/Minnie.TTF', size)

text = 'Pukifeju julofej egy nagy trampli'

for c in text:
    pd.print_char(c, (x,y), fnt)
    last_char_length = d.textlength(c, font=fnt)
    x += last_char_length




img.save('out/test.png')




from PIL import Image, ImageDraw, ImageFont
import math

def print_char(char, start, fnt, d):

    d.text((start[0]+2,start[1]+2), char, font = fnt, fill = (0,0,0))

    d.text(start, char, font = fnt, fill = (255,255,255))

#    if(ord(char) >= 97 and ord(char) <= 122):
#        print_long_umlaut(char, start, fnt, d)
    

    #calculations required for umlaut drawing
    #    umlautlength = d.textlength('..', font=fnt)
    #    olength = d.textlength('o', font = fnt)
    #    startdiff = (olength - umlautlength) /2
    #    start = d.textlength('Hell', font=fnt) + startdiff
    #    d.text((size + start,5),'..', fill=(255,0,255), font=fnt)

def print_tittle(char, start, fnt, d):
    print_accent(char,start,fnt,d,'.', 0, size / 4)

def print_umlaut(char, start, fnt, d):
    print_accent(char,start,fnt,d,'..', 0, size / 4)

def print_long_tittle(char,start,fnt,d):
    print_accent(char,start,fnt,d,',', size/10, size / 8)

def print_long_umlaut(char,start,fnt,d):
    print_accent(char,start,fnt,d,',,', size/10, size / 8)

def print_accent(char, start, fnt, d, accent, x_diff, y_diff):
    tittle_length = d.textlength(accent, font = fnt)
    char_length = d.textlength(char, font = fnt)
    start_diff = math.ceil((char_length - tittle_length) / 2 )
    x = start[0] + start_diff + x_diff
    y = start[1] - size + y_diff 
    d.text((x+2,y+2), accent, font = fnt, fill = (0,0,0))
    d.text((x, y), accent, font = fnt, fill = (255,255,255))

def init_image():
    #the image size should be set as a default, since all cards shall be the same size
    return Image.new('RGB', (1920, 1080), color = (0,31,115))

def print_background(d):
    #the font shall be the same
    d.ellipse([(100,100), (1870,1000)], fill=(37,67,147))
    d.ellipse([(280,270), (1780,950)], fill=(62,94,180))
    d.ellipse([(400,350), (1500,890)], fill=(85,119,211))
    d.ellipse([(20,550), (520, 1050)], fill=(0,0,0))
    d.ellipse([(1400, 200), (1900, 700)], fill=(0,0,0))

img = init_image()
d = ImageDraw.Draw(img)

print_background(d)

#set size for the whole image text as a variable, calculated from the text
size = 100 
x=size
y=size
fnt = ImageFont.truetype('assets/Minnie.TTF', size)

text = 'Pukifeju julofej egy nagy trampli'

for c in text:
    print_char(c, (x,y), fnt, d)
    last_char_length = d.textlength(c, font=fnt)
    x += last_char_length




img.save('out/test.png')




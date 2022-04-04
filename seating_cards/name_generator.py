from PIL import Image, ImageDraw, ImageFont

def print_text(text, start, fnt, d):

    d.multiline_text((start[0]+2,start[1]+2), text, font = fnt, fill = (0,0,0))

    d.multiline_text(start, text, font = fnt, fill = (255,255,255))

    #calculations required for umlaut drawing
    #    umlautlength = d.textlength('..', font=fnt)
    #    olength = d.textlength('o', font = fnt)
    #    startdiff = (olength - umlautlength) /2
    #    start = d.textlength('Hell', font=fnt) + startdiff
    #    d.text((size + start,5),'..', fill=(255,0,255), font=fnt)





text = 'This is\na test'

#set size for the whole image text as a variable, calculated from the text
size = 20
#the image size should be set as a default, since all cards shall be the same size
img = Image.new('RGB', (size*10,size*3), color = (73,109,137))

#the font shall be the same
fnt = ImageFont.truetype('assets/Minnie.TTF', size)
d = ImageDraw.Draw(img)

print_text(text, (size,size), fnt, d)

img.save('out/test.png')




from email.mime import image
from PIL import Image, ImageDraw
from pil_drawer import *
import random as rand


class BackgroundDrawer:

    def __init__(self,d, img):
        c.d = d
        self.pd = PilDrawer(d)
        c.img = img

    def print_background(self):
        #background ellipses
        bg_padding_w = c.padding + 300
        bg_padding_h = c.padding + 50
        self.pd.ellipse( 
                bg_padding_w,
                bg_padding_h,       
                c.image_w - 2*bg_padding_w,  
                c.image_h - 2*bg_padding_h, 
                (37,67,147))

        one_w = 100
        one_h = 100
        one_p = 50 
        self.pd.ellipse( 
                bg_padding_w + one_w, 
                bg_padding_h + one_h, 
                c.image_w - 2*bg_padding_w - one_w - one_p, 
                c.image_h - 2*bg_padding_h - one_h - one_p,
                (62,94,180))

        two_w = 230
        two_h = 250
        two_p = 0
        self.pd.ellipse( 
                bg_padding_w + two_w, 
                bg_padding_h + two_h,  
                c.image_w - 2*bg_padding_w - two_w - two_p - one_w,  
                c.image_h - 2*bg_padding_h - two_h - two_p - one_h, 
                (85,119,211))

        #head circles
        self.pd.ellipse( c.padding, c.image_h - c.padding - c.head_d,  c.head_d, c.head_d, fill=(0,0,0))
        self.pd.ellipse( c.image_w - c.padding - c.head_d, c.padding,  c.head_d, c.head_d, fill=(0,0,0))

        i = rand.randint(0,len(c.heads)-1)
        images = c.heads[i]
        #add heads
        dog = Image.open('assets/' + images['dog'] + '.png')
        dog = dog.resize((c.head_d, c.head_d))
        mask = Image.new("L", dog.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((10,10, c.head_d-10, c.head_d-10), fill=255)
        c.img.paste(dog, (c.padding, c.image_h - c.padding - c.head_d), mask)

        up = Image.open('assets/' + images['up'] + '.png')
        up = up.resize((c.head_d,c.head_d))
        c.img.paste(up, (c.image_w - c.padding - c.head_d, c.padding), mask)
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
        if(c.outline > 0):
                self.pd.ellipse( 
                        c.bg_padding_w - c.outline,
                        c.bg_padding_h - c.outline,       
                        c.image_w - 2*c.bg_padding_w + 2 * c.outline,  
                        c.image_h - 2*c.bg_padding_h + 2 * c.outline, 
                        (0,0,0))

        self.pd.ellipse( 
                c.bg_padding_w,
                c.bg_padding_h,       
                c.image_w - 2*c.bg_padding_w,  
                c.image_h - 2*c.bg_padding_h, 
                (37,67,147))
        

        if(c.outline > 0):
                self.pd.ellipse( 
                        c.bg_padding_w + c.one_padding + c.one_offset - c.outline,
                        c.bg_padding_h + c.one_padding + c.one_offset - c.outline,       
                        c.image_w - 2*c.bg_padding_w - 2*c.one_padding+ 2 * c.outline,  
                        c.image_h - 2*c.bg_padding_h - 2*c.one_padding+ 2 * c.outline, 
                        (0,0,0))
        self.pd.ellipse( 
                c.bg_padding_w + c.one_padding + c.one_offset, 
                c.bg_padding_h + c.one_padding + c.one_offset, 
                c.image_w - 2*c.bg_padding_w - 2*c.one_padding, 
                c.image_h - 2*c.bg_padding_h - 2*c.one_padding,
                (62,94,180))

        if(c.outline > 0):
                self.pd.ellipse( 
                        c.bg_padding_w + c.two_padding + c.two_offset - c.outline,
                        c.bg_padding_h + c.two_padding + c.two_offset - c.outline,       
                        c.image_w - 2*c.bg_padding_w - 2*c.two_padding + 2 * c.outline,  
                        c.image_h - 2*c.bg_padding_h - 2*c.two_padding + 2 * c.outline, 
                        (0,0,0))
        self.pd.ellipse( 
                c.bg_padding_w + c.two_padding + c.two_offset, 
                c.bg_padding_h + c.two_padding + c.two_offset,  
                c.image_w - 2*c.bg_padding_w - 2*c.two_padding,  
                c.image_h - 2*c.bg_padding_h - 2*c.two_padding, 
                (85,119,211))

        #head circles
        self.pd.ellipse( c.padding, c.image_h - c.padding - c.head_d,  c.head_d, c.head_d, fill=(0,0,0))
        self.pd.ellipse( c.image_w - c.padding - c.head_d, c.padding,  c.head_d, c.head_d, fill=(0,0,0))


        if(c.head_d > 0):
                i = rand.randint(0,len(c.heads)-1)
                images = c.heads[i]
                #add heads
                dog = Image.open('assets/' + images['dog'] + '.png')
                dog = dog.resize((c.head_d, c.head_d))

                up = Image.open('assets/' + images['up'] + '.png')
                up = up.resize((c.head_d,c.head_d))

                #mask for creating border effect on the heads, otherwise the images are not round
                mask = Image.new("L", dog.size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((c.head_d * c.head_border_percent / 2,
                        c.head_d * c.head_border_percent / 2,
                        c.head_d * (1-c.head_border_percent / 2),
                        c.head_d * (1-c.head_border_percent / 2)),
                        fill=255)

                c.img.paste(dog, (c.padding, c.image_h - c.padding - c.head_d), mask)
                c.img.paste(up, (c.image_w - c.padding - c.head_d, c.padding), mask)
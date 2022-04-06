from PIL import Image
from pil_drawer import *


class BackgroundDrawer:

    def __init__(self,d):
        self.d = d
        self.pd = PilDrawer(d)

    def img_w(self, w):
        self.image_w = w
        return self

    def img_h(self, h):
        self.image_h = h
        return self

    def head_d(self, d):
        self.head_d = d
        return self

    def padding(self, p):
        self.padding = p
        return self


    def print_background(self):
        #background ellipses
        bg_padding_w = self.padding + 300
        bg_padding_h = self.padding + 50
        self.pd.ellipse( 
                bg_padding_w,
                bg_padding_h,       
                self.image_w - 2*bg_padding_w,  
                self.image_h - 2*bg_padding_h, 
                (37,67,147))

        one_w = 100
        one_h = 100
        one_p = 50 
        self.pd.ellipse( 
                bg_padding_w + one_w, 
                bg_padding_h + one_h, 
                self.image_w - 2*bg_padding_w - one_w - one_p, 
                self.image_h - 2*bg_padding_h - one_h - one_p,
                (62,94,180))

        two_w = 230
        two_h = 250
        two_p = 0
        self.pd.ellipse( 
                bg_padding_w + two_w, 
                bg_padding_h + two_h,  
                self.image_w - 2*bg_padding_w - two_w - two_p - one_w,  
                self.image_h - 2*bg_padding_h - two_h - two_p - one_h, 
                (85,119,211))

        #head circles
        self.pd.ellipse( self.padding, self.image_h - self.padding - self.head_d,  self.head_d, self.head_d, fill=(0,0,0))
        self.pd.ellipse( self.image_w - self.padding - self.head_d, self.padding,  self.head_d, self.head_d, fill=(0,0,0))

        #test rectangle for text
    #    print_rectangle(520, 120, 800,800, d, fill = 'green')

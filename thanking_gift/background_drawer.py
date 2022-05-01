from constants import *

class BackgroundDrawer:

    def __init__(self, dwg):
        self.dwg = dwg

    def draw_bg(self):
        self.dwg.add(
            self.dwg.rect(
                (img_padding,img_padding),
                (img_size,img_size), 
                stroke=img_border,
                fill=background_color_0
            )
        )

        self.dwg.add(
            self.dwg.ellipse(
                center=((img_padding+img_size)/2,(img_padding+img_size)/2),
                r=(img_size/2-img_size*0.05, img_size/2-img_size*0.1),
                stroke=img_border,
                fill=background_color_1
            )
        )

        self.dwg.add(
            self.dwg.ellipse(
                center=((img_padding+img_size)/2 + img_padding * 0.8,(img_padding+img_size)/2 + img_padding * 0.6),
                r=(img_size/2-img_size*0.125, img_size/2-img_size*0.15),
                stroke=img_border,
                fill=background_color_2
            )
        )

        self.dwg.add(
            self.dwg.ellipse(
                center=((img_padding+img_size)/2 + img_padding * 1.2,(img_padding+img_size)/2 + img_padding * 1),
                r=(img_size/2-img_size*0.18, img_size/2-img_size*0.2),
                stroke=img_border,
                fill=background_color_3
            )
        )
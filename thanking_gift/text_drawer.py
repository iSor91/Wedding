from constants import *

class TextDrawer:

    def __init__(self, dwg):
        self.dwg = dwg

    def draw_text(self):
        text_size=str(img_size*0.22) + 'px'

        self.dwg.add(self.dwg.text('Julo',
            insert=(img_size * 0.25, img_size * 0.4),
            stroke='#000',
            fill='#FFFFFF',
            stroke_width=2,
            font_size=text_size,
            font_weight="bold",
            font_family="Minnie Regular")
        )

        self.dwg.add(self.dwg.text('&',
            insert=(img_size * 0.4, img_size * 0.6),
            stroke='#000',
            fill='#FFFFFF',
            stroke_width=2,
            font_size=text_size,
            font_weight="bold",
            font_family="Minnie Regular")
        )

        self.dwg.add(self.dwg.text('isor',
            insert=(img_size*0.25,img_size*0.8),
            stroke='#000',
            fill='#FFFFFF',
            stroke_width=2,
            font_size=text_size,
            font_weight="bold",
            font_family="Minnie Regular")
        )

        self.dwg.add(self.dwg.text('..',
            insert=(img_size*0.52,img_size*0.65),
            stroke='#000',
            fill='#FFFFFF',
            stroke_width=2,
            font_size=text_size,
            font_weight="bold",
            font_family="Minnie Regular")
        )
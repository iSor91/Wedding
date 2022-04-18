from PIL import Image, ImageDraw
from pil_drawer import PilDrawer
from background_drawer import BackgroundDrawer
import constants as c
from text_calculator import TextCalculator
import utils as u

class CardGenerator:

    def init_image(self):
        #the image size should be set as a default, since all cards shall be the same size
        return Image.new('RGB', (c.image_w, c.image_h), color = (0,31,115))

    def generate_image(self,text):
        img = self.init_image()
        d = ImageDraw.Draw(img)

        bgd = BackgroundDrawer(d)
        pd = PilDrawer(d)

        bgd.img_w(c.image_w).img_h(c.image_h).head_d(c.head_d).padding(c.padding)

        bgd.print_background()

        txc = TextCalculator()
        txc.calculate_text(text, d)

        #print rows into the text area
        row = 0
        text_cnt = len(txc.rows)
        h_offset = (c.text_area_h - text_cnt * txc.size * ((c.row_offset - 1) / 2 + 1)) / 2

        for t in txc.rows:
            w_offset = (c.text_area_w - d.textlength(u.unaccent_word(t), font=txc.fnt)) / 2
            x = c.text_area_start_w + w_offset
            y = h_offset + c.text_area_start_h + row * txc.size * c.row_offset
            for char in t:
                pd.print_char(char, (x,y), txc.fnt, txc.size)
                last_char_length = d.textlength(c.character_counterparts.get(char,char), font=txc.fnt)
                x += last_char_length
            row += 1

        return img




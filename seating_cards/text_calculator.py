from PIL import ImageFont
import constants as c
import utils as u

class TextCalculator:

    def __init__(self) -> None:
        self.base_size = c.text_area_h
        pass

    def calculate_text(self, text, d):
        words = text.split(' ')

        #calculate text size and font, also creating rows for the text
        self.size = self.base_size
        self.fnt = ImageFont.truetype('assets/Minnie.TTF', self.size)
        fits = False
        while( not fits ):
            too_long_word = False
            current = ''
            newText = ''
            self.rows = []
            create_newline = False
            print(words)
            for w in words:
                unaccented_word = u.unaccent_word(w)
                if(d.textlength(unaccented_word, font=self.fnt) > c.text_area_w):
                    too_long_word = True
                    # print('too long word')
                    break
                
                if(w == 'nl'):
                    create_newline = True   

                if(len(current) > 0 and not create_newline):
                    newText = ' '.join([current, w])
                elif(not create_newline):
                    newText = w
                
                if(d.textlength(newText, font=self.fnt) > c.text_area_w or create_newline):
                    if(len(current) > 0):
                        self.rows.append(current)
                    newText = ''
                    current = w
                    if(create_newline):
                        print(w)
                        current = ''
                        create_newline = False
                else:
                    current = newText
            self.rows.append(current)
            text_height = len(self.rows) * self.size * c.row_offset

            if(not too_long_word and text_height <= c.text_area_h):
                fits = True
            else :
                self.size = self.size - 2
                self.fnt = ImageFont.truetype('assets/Minnie.TTF', self.size)
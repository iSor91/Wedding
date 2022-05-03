from email.policy import default
import constants as c
import math

class PilDrawer:

    def __init__(self,d):
        self.d = d

    #shapes
    def ellipse(self,x,y,w,h, fill):
        self.d.ellipse([(x,y),(x+w,y+h)], fill)

    def rectangle(self,x,y,w,h, fill):
        self.d.rectangle([(x,y),(x+w,y+h)], fill)

    #text
    def print_char(self,char, start, fnt, size):
        char_to_print = c.character_counterparts.get(char, char)
        self.d.text((start[0]+c.shadow_offset,start[1]+c.shadow_offset), char_to_print, font = fnt, fill = (0,0,0))
        self.d.text(start, char_to_print, font = fnt, fill = (255,255,255))

        if(char in c.long_tittle_chars):
            self.print_long_tittle(char_to_print, start, fnt, size)
        if(char in c.tittle_chars):
            self.print_tittle(char_to_print, start, fnt, size)
        if(char in c.umlaut_chars):
            self.print_umlaut(char_to_print, start, fnt, size)
        if(char in c.long_umlaut_chars):
            self.print_long_umlaut(char_to_print, start, fnt, size)

    def print_tittle(self, char, start, fnt, size):
        self.print_accent(char,start,fnt,'.', 0, size / 4, size)

    def print_umlaut(self, char, start, fnt, size):
        self.print_accent(char,start,fnt,'..', 0, size / 4, size)

    def print_long_tittle(self, char,start,fnt, size):
        self.print_accent(char,start,fnt,'\'', size/10, size / 1.5, size)

    def print_long_umlaut(self, char,start,fnt, size):
        self.print_accent(char,start,fnt,'\"', size/10, size / 1.5, size)

    def print_accent(self,char, start, fnt, accent, x_diff, y_diff, size):
        tittle_length = self.d.textlength(accent, font = fnt)
        char_length = self.d.textlength(char, font = fnt)
        start_diff = math.ceil((char_length - tittle_length) / 2 )
        x = start[0] + start_diff + x_diff
        y = start[1] - size + y_diff 
        self.d.text((x+c.shadow_offset,y+c.shadow_offset), accent, font = fnt, fill = (0,0,0))
        self.d.text((x, y), accent, font = fnt, fill = (255,255,255))

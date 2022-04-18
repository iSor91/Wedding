from PIL import ImageDraw


class PilDrawer:

    def __init__(self,d):
        self.d = d

    #shapes
    def ellipse(self,x,y,w,h, fill):
        self.d.ellipse([(x,y),(x+w,y+h)], fill)

    def rectangle(self,x,y,w,h, fill):
        self.d.rectangle([(x,y),(x+w,y+h)], fill)

    #text
    def print_char(self,char, start, fnt):
        self.d.text((start[0]+2,start[1]+2), char, font = fnt, fill = (0,0,0))
        self.d.text(start, char, font = fnt, fill = (255,255,255))

    def print_tittle(self,char, start, fnt):
        print_accent(char,start,fnt,'.', 0, size / 4)

    def print_umlaut(self,char, start, fnt):
        print_accent(char,start,fnt,'..', 0, size / 4)

    def print_long_tittle(self,char,start,fnt):
        print_accent(char,start,fnt,',', size/10, size / 8)

    def print_long_umlaut(self,char,start,fnt):
        print_accent(char,start,fnt,',,', size/10, size / 8)

    def print_accent(self,char, start, fnt, accent, x_diff, y_diff):
        tittle_length = self.d.textlength(accent, font = fnt)
        char_length = self.d.textlength(char, font = fnt)
        start_diff = math.ceil((char_length - tittle_length) / 2 )
        x = start[0] + start_diff + x_diff
        y = start[1] - size + y_diff 
        self.d.text((x+2,y+2), accent, font = fnt, fill = (0,0,0))
        self.d.text((x, y), accent, font = fnt, fill = (255,255,255))

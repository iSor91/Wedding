from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont

class JpegConverter:
    def convert_to_jpeg(self, filename):
        registerFont(TTFont('Minnie Regular', 'assets/fonts/Minnie.TTF'))
        svg_content = svg2rlg(filename+'.svg')
        renderPM.drawToFile(svg_content, filename+'.png', fmt='PNG')
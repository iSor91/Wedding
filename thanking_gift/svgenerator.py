import svgwrite
from constants import *
from background_drawer import BackgroundDrawer
from text_drawer import TextDrawer
from jpeg_converter import JpegConverter

file_name='gift_logo'
dwg = svgwrite.Drawing(file_name+'.svg', profile = 'tiny', size=(img_size + img_padding*2,img_size + img_padding*2))

bgd = BackgroundDrawer(dwg)
txtd = TextDrawer(dwg)

bgd.draw_bg()
txtd.draw_text()

dwg.save()

# JpegConverter().convert_to_jpeg(file_name)
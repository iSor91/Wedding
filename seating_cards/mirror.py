import imp
import os
from PIL import Image


def mirror_and_merge_image(dir, image):
    im = Image.open(dir + image)
    dst = Image.new('RGB', (im.width, im.height * 2))
    dst.paste(im.rotate(180), (0,0))
    dst.paste(im, (0,im.height))
    return dst    
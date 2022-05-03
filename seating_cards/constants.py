#main image constants
image_w = 4000 #full image width
image_h = 4000 #full image height
head_d  = 0  #head circle diameter
padding = 400   #padding on the image
outline = 8 #outline for the ellipses

head_border_percent = 0.02


#background circle constants
bg_padding_w = padding + head_d / 2 
bg_padding_h = padding + head_d / 10
one_offset = (image_w - 2 * bg_padding_w) / 35 
one_padding = (image_w - 2*bg_padding_w) / 18
two_offset = (image_w - 2*bg_padding_w) / 20
two_padding = (image_w - 2*bg_padding_w) / 10

#text row size multiplier
row_offset = 1
shadow_offset = 20 #offset for the text shadow

heads = [{'dog': 'isor_dog', 'up': 'julo_up'}, {'dog': 'julo_dog', 'up': 'isor_up'}]

text_area_w = image_w - head_d * 2 - padding * 2
text_area_h = image_h - padding * 2
text_area_start_w = padding + head_d
text_area_start_h = padding

umlaut_chars = ['ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü']
long_umlaut_chars = ['ő', 'ű', 'Ő', 'Ű']

tittle_chars = ['i']
long_tittle_chars = ['á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú']

character_counterparts = {
    'ä': 'a',
    'á': 'a',
    'é': 'e',
    'i': 'i',
    'í': 'i',
    'ó': 'o',
    'ö': 'o',
    'ő': 'o',
    'ú': 'u',
    'ü': 'u',
    'ű': 'u',

    'Ä': 'A',
    'Á': 'A',
    'É': 'E',
    'I': 'I',
    'Í': 'I',
    'Ó': 'O',
    'Ö': 'O',
    'Ő': 'O',
    'Ú': 'U',
    'Ü': 'U',
    'Ű': 'U'

}

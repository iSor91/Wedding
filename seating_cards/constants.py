
image_w = 1920 #full image width
image_h = 1080 #full image height
head_d  = 450  #head circle diameter
padding = 50   #padding on the image

row_offset = 1.25

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

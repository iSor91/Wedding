import os
import shutil
from card_generator import CardGenerator
from google_sheet_service import GoogleSheetService
from datetime import datetime

dir_path = 'out_thanking_gift/'

try:
    shutil.rmtree(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))

os.mkdir(dir_path)


def generate(text, name):
    cg = CardGenerator()

    start_time = datetime.now()
    print('Started seating card generation at {}'.format(start_time) )
    img = cg.generate_image(text)
    img.save(dir_path + name)
    end_time = datetime.now()
    print('Image generation ended at {} after {}'.format(end_time, end_time-start_time))

generate('Julo & nl isör', 'thanking_gift.png')

canthelp="Wise men say nl Only fools rush in nl But I can't help falling in love with you nl nl Shall I stay? nl Would it be a sin nl If I can't help falling in love with you? nl nl Like a river flows nl Surely to the sea nl Darling, so it goes nl Some things are meant to be nl nl Take my hand nl Take my whole life too nl For I can't help falling in love with you nl nl Like a river flows nl Surely to the sea nl Darling, so it goes nl Some things are meant to be nl nl Take my hand nl Take my whole life too nl For I can't help falling in love with you nl nl For I can't help falling nl in love nl with you"
generate(canthelp, 'thanking_gift_back.png')
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

cg = CardGenerator()

start_time = datetime.now()
print('Started seating card generation at {}'.format(start_time) )
img = cg.generate_image('Julo & nl isör')
img.save(dir_path + 'thanking_gift.png')
end_time = datetime.now()
print('Image generation ended at {} after {}'.format(end_time, end_time-start_time))
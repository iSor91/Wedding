import os
import shutil
from card_generator import CardGenerator
from google_sheet_service import GoogleSheetService
from datetime import datetime


dir_path = 'out'

try:
    shutil.rmtree(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))

os.mkdir(dir_path)

cg = CardGenerator()

gs = GoogleSheetService()

start_time = datetime.now()
print('Started seating card generation at {}'.format(start_time) )
all = 1
cnt = 0
for r in gs.all_response_names:
    subcnt = 0
    for name in r:
        print('{} - generating seating card for {}'.format(all, name))
        img = cg.generate_image(name)
        img.save('out/' + str(cnt) + '_' + str(subcnt) + '.png')
        subcnt = subcnt + 1
        all = all + 1
    cnt = cnt + 1

end_time = datetime.now()
print('Image generation ended at {} after {}'.format(end_time, end_time-start_time))
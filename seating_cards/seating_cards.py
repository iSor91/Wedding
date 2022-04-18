import os
import shutil
from card_generator import CardGenerator
from google_sheet_service import GoogleSheetService

dir_path = 'out'

try:
    shutil.rmtree(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))

os.mkdir(dir_path)

cg = CardGenerator()

gs = GoogleSheetService()

cnt = 0
for r in gs.all_response_names:
    subcnt = 0
    for name in r:
        print('generating seating card for {}'.format(name))
        img = cg.generate_image(name)
        img.save('out/' + str(cnt) + '_' + str(subcnt) + '.png')
        subcnt = subcnt + 1
    cnt = cnt + 1

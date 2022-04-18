import requests
import json
import os


class GoogleSheetService:

    api_key = os.getenv('GSHEET_API_KEY')
    base_url = 'https://sheets.googleapis.com/v4/spreadsheets/'
    spreadsheet_id = os.getenv('GSHEET_SPREADSHEET_ID')

    def __init__(self):
        
        self.all_response_names = []

        couples=self.get_response('Couple')

        for r in couples.json()['values']:
            response_names = []
            response_names.append(r[2])
            response_names.append(r[4])
            if(len(r[7]) > 0):
                response_names.extend([s.strip() for s in r[7].split(',')])
            self.all_response_names.append(response_names)

        singles=self.get_response('Single')
        for r in singles.json()['values']:
            response_names = []
            response_names.append(r[2])
            self.all_response_names.append(response_names)
    
    def get_response(self, spreadsheet):
        return requests.get(self.base_url + self.spreadsheet_id + '/values/' + spreadsheet + '!A2:Z1000?key=' + self.api_key)

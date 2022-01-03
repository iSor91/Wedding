import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GsheetService {

  baseUrl: string = 'https://sheets.googleapis.com/v4/spreadsheets/'
  spreadsheetId: string = '1SbwPIDL9h5qoEFMZmMS5SSw5RDB1v8fH3HlW9Dl_yfg'
  //TODO move to server side API
  key: string = 'AIzaSyBM30ioEyekkcQdr5AveXBLcgjE1Cyi97s'

  constructor(private http: HttpClient) { }

  getProgram() {
    return this.readSheet('Program')
  }

  getInvites() {
    return this.readSheet('Invite');
  }

  readSheet(sheet: string) {
    return this.http.get<any>(`${this.baseUrl}${this.spreadsheetId}/values/${sheet}!A2:Z1000?key=${this.key}`)
  }

}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';
import { Invitee } from '../model/invitee';
import { Program } from '../model/program';
import { InviteContent } from '../model/invite-content';
import { Previously } from '../model/previously';

@Injectable({
  providedIn: 'root'
})
export class GsheetService {

  baseUrl: string = 'https://sheets.googleapis.com/v4/spreadsheets/'
  spreadsheetId: string = '1SbwPIDL9h5qoEFMZmMS5SSw5RDB1v8fH3HlW9Dl_yfg'
  //TODO move to server side API
  key: string = 'AIzaSyBM30ioEyekkcQdr5AveXBLcgjE1Cyi97s'

  invitees: BehaviorSubject<Invitee[]> = new BehaviorSubject<Invitee[]>([]);
  program: BehaviorSubject<Program[]> = new BehaviorSubject<Program[]>([]);
  inviteContent: BehaviorSubject<InviteContent[]> = new BehaviorSubject<InviteContent[]>([]);
  respondedHashes: BehaviorSubject<string[]> = new BehaviorSubject<string[]>([]);
  previouslyContent: BehaviorSubject<Previously[]> = new BehaviorSubject<Previously[]>([]);

  constructor(private http: HttpClient) { 
    var programJson = this.readSheet('Program');
    var programs: Program[] = []
    programJson.subscribe(data => {
      data.values.forEach((element: any) => {
        programs.push(new Program(element[0], element[1], element[2], element[3] == '1'))
      });
      this.program.next(programs);
    });

    var inviteeJson = this.readSheet('Invitee');
    inviteeJson.subscribe(data => {
      var invitees: Invitee[] = [];
      data.values.forEach((element: any) => {
        var invitee = new Invitee();
        invitee.hash = element[0];
        invitee.validity = element[1];
        invitee.name = element[2];
        invitee.type = element[3];
        invitees.push(invitee);
      });
      this.invitees.next(invitees);
    });

    var inviteContentJson = this.readSheet('InviteContent');
    inviteContentJson.subscribe(data => {
      var inviteContents: InviteContent[] = [];
      data.values.forEach((element: any) => {
        var inv = new InviteContent();
        inv.type = element[0];
        inv.contentType = element[1];
        inv.greeting = element[2];
        for (let i = 3; i < element.length; i++) {
          inv.content.push(element[i]);
        }
        inviteContents.push(inv);
      });
      this.inviteContent.next(inviteContents);
    });

    var respondedHashesJson = this.readSheet('Responded');
    respondedHashesJson.subscribe(data => {
      var responses: string[] = [];
      if(data.values !== undefined) {
        data.values.forEach((element: any) => {
          for (let i = 0; i < element.length; i++) {
            responses.push(element[i]);
          }
        });
        this.respondedHashes.next(responses);
      }
      
      
    });

    var previouslyJson = this.readSheet('Previously');
    var i = 0;
    previouslyJson.subscribe(data => {
      var previouslyContents: Previously[] =[];
      data.values.forEach((element:any) =>{
        var p = new Previously();
        p.imgUrl = element[0];
        for (let i = 1; i < element.length; i++) {
          p.paragraphs.push(element[i]);
        }
        p.index = ++i;
        previouslyContents.push(p);
      });
      this.previouslyContent.next(previouslyContents);
    });
  }

  getProgram() {
    return this.program.asObservable();
  }

  getInviteContents() {
    return this.inviteContent.asObservable();
  }

  getInvitees() {
    return this.invitees.asObservable();
  }

  getResponses() {
    return this.respondedHashes.asObservable();
  }

  getPreviously() {
    return this.previouslyContent.asObservable();
  }

  readSheet(sheet: string) {
    return this.http.get<any>(`${this.baseUrl}${this.spreadsheetId}/values/${sheet}!A2:Z1000?key=${this.key}`)
  }

}

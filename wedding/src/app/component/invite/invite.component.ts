import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { InviteContent } from 'src/app/model/invite-content';
import { Invitee } from 'src/app/model/invitee';
import { GsheetService } from 'src/app/service/gsheet.service';

@Component({
  selector: 'app-invite',
  templateUrl: './invite.component.html',
  styleUrls: ['./invite.component.scss']
})
export class InviteComponent implements OnInit {

  hash: string = "";

  inviteesObs: Observable<Invitee[]> = this.gsheetService.getInvitees();
  inviteContentsObs: Observable<InviteContent[]> = this.gsheetService.getInviteContents();
  responsesObs: Observable<string[]> = this.gsheetService.getResponses();

  invitees: Invitee[] = [];
  inviteContents: InviteContent[] = [];
  responses: string[] = [];

  invitee: Invitee | undefined;
  inviteContent: InviteContent | undefined;
  respondedContent: InviteContent | undefined;
  calendarContent: InviteContent | undefined;
  
  constructor(private activeRoute: ActivatedRoute, private gsheetService: GsheetService) { 
    this.hash = activeRoute.snapshot.paramMap.get("hash")!!;
  }

  ngOnInit(): void {
    this.inviteesObs.subscribe(data => {
      this.invitees = data;
      this.getContent();
    });
    this.inviteContentsObs.subscribe(data => {
      this.inviteContents = data;
      this.getContent();
    });
    this.responsesObs.subscribe(data => {
      this.responses = data
      this.getContent();
    });
  }

  alreadyResponded(): boolean {
    var hash = this.invitee?.hash
    if(hash == undefined) {
      return true;
    }
    return this.responses.indexOf(hash) != -1;
  }

  private getContent() {

    if(this.invitees.length == 0) {
      return;
    }
    var invitee = this.invitees.find(invitee => invitee.hash == this.hash);
    
    if(invitee instanceof Invitee) {
      this.invitee = invitee!!;
    } else {
      this.invitee = this.invitees.find(invitee => invitee.hash == 'error');
    }

    if(this.inviteContents.length == 0) {
      return;
    }

    this.inviteContent = this.getInviteContentOfType('invite');
    this.respondedContent = this.getInviteContentOfType('responded');
    this.calendarContent = this.getInviteContentOfType('calendar');
  }

  private getInviteContentOfType(type: string): InviteContent | undefined {
    return this.inviteContents.find(invite => invite.type == this.invitee?.type && invite.contentType == type)!!;
  }

  validType(): boolean {
    return this.invitee?.validity == '1';
  }
}

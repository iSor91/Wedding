import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { InviteContent } from 'src/app/model/invite-content';
import { Invitee } from 'src/app/model/invitee';
import { GsheetService } from 'src/app/service/gsheet.service';


@Component({
  selector: 'app-invite',
  templateUrl: './invite.component.html',
  styleUrls: ['./invite.component.scss']
})
export class InviteComponent implements OnInit {

  type: string = "";

  private invitees: Invitee[] = [];
  private inviteContents: InviteContent[] = [];
  private responses: string[] = [];

  invitee: Invitee | undefined;
  inviteContent: InviteContent | undefined;
  respondedContent: InviteContent | undefined;
  calendarContent: InviteContent | undefined;
  
  constructor(private activeRoute: ActivatedRoute, private gsheetService: GsheetService) { 
    this.type = activeRoute.snapshot.paramMap.get("hash")!!;
  }

  ngOnInit(): void {
    this.inviteContents = [];
    this.gsheetService.getInviteContents().subscribe(data => {
      this.processInviteContent(data);
    });
    this.gsheetService.getInvitees().subscribe(data => {
      this.processInvitees(data);
    });
    this.gsheetService.getResponses().subscribe(data => {
      this.processResponses(data);
    })
  }

  alreadyResponded(): boolean {
    var hash = this.invitee?.hash
    if(hash == undefined) {
      return true;
    }
    return this.responses.indexOf(hash) != -1;
  }

  processResponses(data: any) {
    data.values.forEach((element: any) => {
      for (let i = 0; i < element.length; i++) {
        this.responses.push(element[i]);
        
      }
    });
  }

  processInvitees(data: any) {
    data.values.forEach((element: any) => {
      var invitee = new Invitee();
      invitee.hash = element[0];
      invitee.validity = element[1];
      invitee.name = element[2];
      invitee.type = element[3];
      this.invitees.push(invitee);
    });
    this.getContent();
  }

  private processInviteContent(data: any) {
    data.values.forEach((element: any) => {
      var inv = new InviteContent();
      inv.type = element[0];
      inv.contentType = element[1];
      inv.greeting = element[2];
      for (let i = 3; i < element.length; i++) {
        inv.content.push(element[i]);
      }
      this.inviteContents.push(inv);
    });
    this.getContent();
  }

  getContent() {

    if(this.invitees.length == 0) {
      return;
    }
    var invitee = this.invitees.find(invitee => invitee.hash == this.type);
    
    if(invitee instanceof Invitee) {
      this.invitee = invitee!!;
    } else {
      this.invitee = this.invitees.find(invitee => invitee.hash == 'error');
    }

    if(this.inviteContents.length == 0) {
      return;
    }

    this.inviteContent = this.inviteContents.find(invite => invite.type == this.invitee?.type && invite.contentType == 'invite')!!;

    this.respondedContent = this.inviteContents.find(invite => invite.type == this.invitee?.type && invite.contentType == 'responded');

    this.calendarContent = this.inviteContents.find(invite => invite.type == this.invitee?.type && invite.contentType == 'calendar');

  }

  validType(): boolean {
    return this.invitee?.validity == '1';
  }
}

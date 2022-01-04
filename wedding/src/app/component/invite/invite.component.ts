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

  invitee: Invitee | undefined;
  inviteContent: InviteContent | undefined;
  
  constructor(private activeRoute: ActivatedRoute, private gsheetService: GsheetService) { 
    this.type = activeRoute.snapshot.paramMap.get("hash")!!;
  }

  ngOnInit(): void {
    this.inviteContents = [];
    this.gsheetService.getInviteContents().subscribe(data => {
      this.processInviteTypes(data);
    });
    this.gsheetService.getInvitees().subscribe(data => {
      this.processInvitees(data);
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

  private processInviteTypes(data: any) {
    data.values.forEach((element: any) => {
      var inv = new InviteContent();
      inv.type = element[0];
      inv.greeting = element[1];
      for (let i = 2; i < element.length; i++) {
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

    this.inviteContent = this.inviteContents.find(invite => invite.type == this.invitee?.type)!!;

  }

  validType(): boolean {
    return this.invitee?.validity == '1';
  }
}

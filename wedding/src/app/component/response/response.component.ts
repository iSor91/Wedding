import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Invitee } from 'src/app/model/invitee';
import { GsheetService } from 'src/app/service/gsheet.service';

@Component({
  selector: 'app-response',
  templateUrl: './response.component.html',
  styleUrls: ['./response.component.scss']
})
export class ResponseComponent implements OnInit {

  private hash: string = "";

  private invitees: Invitee[] = [];
  invitee: Invitee | undefined;
  
  constructor(private activeRoute: ActivatedRoute, private gsheetService: GsheetService) { 
    this.hash = activeRoute.snapshot.paramMap.get("hash")!!;
  }

  ngOnInit(): void {
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

  getContent() {
    var invitee = this.invitees.find(invitee => invitee.hash == this.hash);
    if(invitee instanceof Invitee) {
      this.invitee = invitee!!;
    } else {
      this.invitee = this.invitees.find(invitee => invitee.hash == 'error');
    }
  }
}

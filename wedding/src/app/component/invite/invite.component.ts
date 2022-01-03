import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Invite } from 'src/app/model/invite';
import { GsheetService } from 'src/app/service/gsheet.service';


@Component({
  selector: 'app-invite',
  templateUrl: './invite.component.html',
  styleUrls: ['./invite.component.scss']
})
export class InviteComponent implements OnInit {

  type: string = "";

  //update to behaviorsubject
  invite: Invite = new Invite();

  private validInvites: Invite[] = []
  
  constructor(private activeRoute: ActivatedRoute, private gsheetService: GsheetService) { 
    this.type = activeRoute.snapshot.paramMap.get("type")!!;
  }

  ngOnInit(): void {
    this.validInvites = [];
    this.gsheetService.getInvites().subscribe(data => {
      data.values.forEach((element: any) => {
        var inv = new Invite();
        inv.type = element[0];
        inv.valid = element[1];
        inv.greeting = element[2];
        for (let i = 3; i < element.length; i++) {
          inv.content.push(element[i]);
        }
        this.validInvites.push(inv);
        console.log(inv);
      });
      this.invite = this.getContent();
    })
  }

  getContent(): Invite {
    
    var invite = this.validInvites.find(invite => invite.type == this.type);
    
    if(invite instanceof Invite && invite?.type !== "") {
      return invite!!;
    }
    return this.validInvites.find(invite => invite.type == 'error')!!;
  }

  validType(): boolean {
    return this.invite!!.valid == '1';
  }
}

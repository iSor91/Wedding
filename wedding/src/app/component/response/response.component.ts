import { Component, OnInit } from '@angular/core';
import { DomSanitizer, SafeResourceUrl, SafeUrl } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';
import { Invitee } from 'src/app/model/invitee';
import { GsheetService } from 'src/app/service/gsheet.service';

@Component({
  selector: 'app-response',
  templateUrl: './response.component.html',
  styleUrls: ['./response.component.scss']
})
export class ResponseComponent implements OnInit {

  hash: string = "";
  
  private invitees: Invitee[] = [];
  invitee: Invitee | undefined;
  
  constructor(private sanitizer: DomSanitizer, private activeRoute: ActivatedRoute, private gsheetService: GsheetService) { 
    this.hash = activeRoute.snapshot.paramMap.get("hash")!!;
  }

  ngOnInit(): void {
    this.gsheetService.getInvitees().subscribe(data => {
      this.processInvitees(data);
    });
  }

  formUrl(): string {
    return this.invitee?.type == 'single' ? 
    //single response
    `https://docs.google.com/forms/d/e/1FAIpQLSfeS3E2qKuRm6H9XMmUBYKGS9nsDVXmClfY38HwHYZNkHBR1w/viewform?usp=pp_url&entry.557630679=${this.hash}` :
    //couple response
    `https://docs.google.com/forms/d/e/1FAIpQLSeHWe6ODD0zbvEf3-T_JmYutigdtTvMbHGKXS9S6F_RQAy0yw/viewform?embedded=true&entry.1895075738=${this.hash}`;
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

import { Component, OnInit } from '@angular/core';
import { DomSanitizer, SafeResourceUrl, SafeUrl } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { InviteContent } from 'src/app/model/invite-content';
import { Invitee } from 'src/app/model/invitee';
import { GsheetService } from 'src/app/service/gsheet.service';
import { InviteComponent } from '../invite/invite.component';

@Component({
  selector: 'app-response',
  templateUrl: './response.component.html',
  styleUrls: ['./response.component.scss']
})
export class ResponseComponent extends InviteComponent implements OnInit {

  formUrl(): string {
    return this.invitee?.type == 'single' ? 
    //single response
    `https://docs.google.com/forms/d/e/1FAIpQLSfeS3E2qKuRm6H9XMmUBYKGS9nsDVXmClfY38HwHYZNkHBR1w/viewform?embedded=true&entry.557630679=${this.hash}` :
    //couple response
    `https://docs.google.com/forms/d/e/1FAIpQLSeHWe6ODD0zbvEf3-T_JmYutigdtTvMbHGKXS9S6F_RQAy0yw/viewform?embedded=true&entry.1895075738=${this.hash}`;
  }

  getHeight(): string {
    return this.invitee?.type == 'single' ? '1000' : '1250';
  }
}

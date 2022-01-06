import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Previously } from 'src/app/model/previously';
import { GsheetService } from 'src/app/service/gsheet.service';

@Component({
  selector: 'app-previously',
  templateUrl: './previously.component.html',
  styleUrls: ['./previously.component.scss']
})
export class PreviouslyComponent implements OnInit {

  constructor(private gsheetService: GsheetService) { }

  previouslyContentObs: Observable<Previously[]> = this.gsheetService.getPreviously();
  previouslyContent: Previously[] = [];

  ngOnInit(): void {
    this.previouslyContentObs.subscribe(data => this.previouslyContent = data);
  }

  imgOrder(p: Previously): string {
    return p.index % 2 == 1 ? '3' : '1';
  }
  
  pOrder(p: Previously): string {
    return p.index % 2 == 0 ? '3' : '1';
  }

}

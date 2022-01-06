import { Component, OnInit } from '@angular/core';
import { Previously } from 'src/app/model/previously';
import { GsheetService } from 'src/app/service/gsheet.service';

@Component({
  selector: 'app-previously',
  templateUrl: './previously.component.html',
  styleUrls: ['./previously.component.scss']
})
export class PreviouslyComponent implements OnInit {

  constructor(private gsheetService: GsheetService) { }

  previouslyContent: Previously[] = [];

  ngOnInit(): void {
    var i = 0;
    this.gsheetService.getPreviously().subscribe(data => {
      data.values.forEach((element:any) =>{
        var p = new Previously();
        p.imgUrl = element[0];
        for (let i = 1; i < element.length; i++) {
          p.paragraphs.push(element[i]);
        }
        p.index = ++i;
        this.previouslyContent.push(p);
      })
    });
  }

  imgOrder(p: Previously): string {
    return p.index % 2 == 1 ? '3' : '1';
  }
  
  pOrder(p: Previously): string {
    return p.index % 2 == 0 ? '3' : '1';
  }

}

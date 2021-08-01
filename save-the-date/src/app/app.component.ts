import { Component, NgZone, OnInit } from '@angular/core';
import { CdkScrollable, ScrollDispatcher, ScrollingModule } from "@angular/cdk/scrolling";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  
  scrollState = 0;

  constructor(
    private scrollDispatcher: ScrollDispatcher,
    private zone: NgZone)
  {}
  
  ngOnInit(): void {
    this.scrollDispatcher.scrolled().subscribe(
      (event: CdkScrollable) => {
        const scrollState = event.measureScrollOffset("top")
        this.zone.run(()=> this.scrollState = scrollState);
      }
    )
  }

  calculateOpacity(index: number): number {
    const fullheight = window.innerHeight;
    const windowcenter = fullheight/2;
    const inwindowvalue = fullheight * index - this.scrollState;
    if(inwindowvalue < -windowcenter || inwindowvalue > windowcenter) {
      return 0;
    }
    if(inwindowvalue > 0) {
      return 1 - inwindowvalue / windowcenter;
    } else {
      return (inwindowvalue + windowcenter) / windowcenter ;
    }
  }


}

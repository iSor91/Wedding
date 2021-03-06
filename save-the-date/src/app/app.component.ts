import { Component, NgZone, OnInit } from '@angular/core';
import { CdkScrollable, ScrollDispatcher, ScrollingModule } from "@angular/cdk/scrolling";
import { DeviceDetectorService } from 'ngx-device-detector';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  
  scrollState = 0;
  backgroundImgUrl : string;
  description = "Összeházasodunk ebben az időpontban, mentsd el, hivatalos meghívó később érkezik. :)";
  not_working_button = "Ha a gomb nem működik a kapitalizmust hibáztasd";

  constructor(
    private scrollDispatcher: ScrollDispatcher,
    private zone: NgZone,
    private deviceService: DeviceDetectorService)
  {
    const backgroundIndex = Math.floor( Math.random() * 4 ) + 1;
    this.backgroundImgUrl = `assets/images/oh_you_${backgroundIndex}.png`;
  }
  
  ngOnInit(): void {
    this.scrollDispatcher.scrolled().subscribe(
      (event: CdkScrollable) => {
        const scrollState = event.measureScrollOffset("top")
        this.zone.run(()=> this.scrollState = scrollState);
      }
    )
  }

  isDesktop(): boolean {
    return this.deviceService.isDesktop();
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

import { Component, OnInit } from '@angular/core';
import { DeviceDetectorService } from 'ngx-device-detector';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  deviceService: DeviceDetectorService;

  constructor(private ds: DeviceDetectorService) {
    this.deviceService = ds;
  }

}

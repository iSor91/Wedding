import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, NavigationEnd, Router } from '@angular/router';
import { DeviceDetectorService } from 'ngx-device-detector';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent implements OnInit {

  active: string = "";
  activename: string = "";

  buttons = [
    ["program","Program"],
    ["previously","Bemutatkozás"],
    ["images", "Képek"],
    ["contactus","Kapcsolat"]
  ]

  buttonsMap = new Map([
    ["invitation","Meghívó"],
    ["response","Visszajelzés"],
    ["program","Program"],
    ["previously","Bemutatkozás"],
    ["images","Képek"],
    ["contactus","Kapcsolat"]
  ])

  constructor(private route: Router, public ds: DeviceDetectorService) {
    route.events.subscribe(data => {
      if(data instanceof NavigationEnd) {
        this.active = data.url.substring(1);
        if(this.active == "") {
          this.active = "program";
        } else if(this.active.startsWith("invitation")) {
          this.active = "invitation";
        } else if(this.active.startsWith("response")) {
          this.active = "response";
        }
        var activename = this.buttonsMap.get(this.active);
        this.activename = activename == undefined ? "" : activename;
      }
    });
  }

  ngOnInit(): void {
  }

  setActive(active: string, name: string) {
    this.active = active;
    this.activename = name;
  }

  isActive(active: string): boolean {
    return this.active == active;
  }
}

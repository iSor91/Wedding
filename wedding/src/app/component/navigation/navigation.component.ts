import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent implements OnInit {

  active: string = "";

  constructor() { }

  ngOnInit(): void {
  }

  setActive(active: string) {
    this.active = active;
  }

  isActive(active: string): boolean {
    return this.active == active;
  }
}

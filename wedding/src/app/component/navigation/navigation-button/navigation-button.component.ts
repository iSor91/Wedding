import { Component, Input, OnInit } from '@angular/core';
import { NavigationComponent } from '../navigation.component';

@Component({
  selector: 'app-navigation-button',
  templateUrl: './navigation-button.component.html',
  styleUrls: ['./navigation-button.component.scss']
})
export class NavigationButtonComponent implements OnInit {

  @Input() name: string = "";
  @Input() routerLink: string = "";

  constructor(private nav: NavigationComponent) { }

  ngOnInit(): void {
  }

  setActive() {
    this.nav.setActive(this.routerLink);    
  }

  isActive() {
    return this.nav.isActive(this.routerLink);
  }

}

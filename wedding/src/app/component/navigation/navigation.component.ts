import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent implements OnInit {

  active: string = "";

  constructor(private router: Router) { 
  }

  ngOnInit(): void {
  }

  setActive(active: string) {
    this.active = active;
  }

  isActive(active: string): boolean {
    return this.active == active;
  }
}

import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor() { }

  index = 1;
  
  ngOnInit(): void {
    this.index = Math.ceil(Math.random() * 2);
  }

  getIndex(): number {
    return this.index;
  }

}

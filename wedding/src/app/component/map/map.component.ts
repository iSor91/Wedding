import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {

  api_key = 'AIzaSyBiPj0d-3Gf31MD-13AXS3yYKEZRJtYkoI';
  constructor() { }

  ngOnInit(): void {
  }

}

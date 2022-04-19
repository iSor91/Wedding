import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { TravelInfo } from 'src/app/model/travel-info';
import { GsheetService } from 'src/app/service/gsheet.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {


  map_base_url = 'https://www.google.com/maps/embed/v1/place?key='
  map_search_url = '&q=Nádas Tó Park Hotel,Hungary&language=hu'
  sectionsObs : Observable<TravelInfo[]> = this.gsheetService.getTravelInformation();
  sections : TravelInfo[] = [];
  constructor(private gsheetService: GsheetService) { }

  ngOnInit(): void {
    this.getSections();
  }

  getSections(){
    this.sectionsObs.subscribe(data => {
      this.sections = data;
    })
  }

  getMapUrl() :string{
    return `${this.map_base_url}${environment.key}${this.map_search_url}`
  }

}

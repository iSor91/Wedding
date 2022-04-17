import { Component, Input, OnInit } from '@angular/core';
import { Program } from 'src/app/model/program';

@Component({
  selector: 'app-progrow',
  templateUrl: './progrow.component.html',
  styleUrls: ['./progrow.component.scss']
})
export class ProgrowComponent implements OnInit {

  @Input() program: Program | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}

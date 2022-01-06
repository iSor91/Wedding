import { Component, OnInit } from '@angular/core';
import { GsheetService } from 'src/app/service/gsheet.service';
import { tap } from 'rxjs/operators';
import { Program } from 'src/app/model/program';
import { BehaviorSubject, Observable } from 'rxjs';

@Component({
  selector: 'app-program',
  templateUrl: './program.component.html',
  styleUrls: ['./program.component.scss']
})
export class ProgramComponent implements OnInit {

  constructor(private db: GsheetService) { }

  programsObs: Observable<Program[]> = this.db.getProgram();
  programs: Program[] = [];

  ngOnInit(): void {
    this.getPrograms();
  }

  getPrograms() {
    this.programsObs.subscribe(data => this.programs = data.filter(p=>!p.hidden))
  }

}

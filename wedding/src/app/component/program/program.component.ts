import { Component, OnInit } from '@angular/core';
import { GsheetService } from 'src/app/service/gsheet.service';
import { tap } from 'rxjs/operators';
import { Program } from 'src/app/model/program';

@Component({
  selector: 'app-program',
  templateUrl: './program.component.html',
  styleUrls: ['./program.component.scss']
})
export class ProgramComponent implements OnInit {

  constructor(private db: GsheetService) { }

  programs: Program[] = []

  ngOnInit(): void {
    this.getPrograms();
  }

  getPrograms() {
    this.programs = []
    this.db.getProgram().subscribe(data => 
      data.values.forEach((element: any) => {
        this.programs.push(new Program(element[0], element[1], element[2], element[3] == '1'))
      })
    );
    this.programs.filter(p=>!p.hidden)
  }

}

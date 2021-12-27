import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProgramComponent } from './component/program/program.component';

const routes: Routes = [
  {path: 'program', component: ProgramComponent},
  {path: '', redirectTo:'program', pathMatch:'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

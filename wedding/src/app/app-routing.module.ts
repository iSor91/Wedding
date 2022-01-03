import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InviteComponent } from './component/invite/invite.component';
import { ProgramComponent } from './component/program/program.component';
import { ResponseComponent } from './component/response/response.component';

const routes: Routes = [
  {path: 'response/:type', component: ResponseComponent},
  {path: 'invite/:type', component: InviteComponent},
  {path: 'program', component: ProgramComponent},
  {path: '', redirectTo:'program', pathMatch:'full'},
  {path: '**', redirectTo: 'program'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

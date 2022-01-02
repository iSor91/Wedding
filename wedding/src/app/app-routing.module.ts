import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InviteComponent } from './component/invite/invite.component';
import { ProgramComponent } from './component/program/program.component';
import { ResponseComponent } from './component/response/response.component';

const routes: Routes = [
  {path: 'response', component: ResponseComponent},
  {path: 'invite', component: InviteComponent},
  {path: 'program', component: ProgramComponent},
  {path: '', redirectTo:'invite', pathMatch:'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

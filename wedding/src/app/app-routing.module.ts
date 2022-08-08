import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContactUsComponent } from './component/contact-us/contact-us.component';
import { InviteComponent } from './component/invite/invite.component';
import { PreviouslyComponent } from './component/previously/previously.component';
import { ProgramComponent } from './component/program/program.component';
import { ResponseComponent } from './component/response/response.component';
import { ImagesComponent } from './images/images.component';

const routes: Routes = [
  {path: 'contactus', component: ContactUsComponent},
  {path: 'previously', component: PreviouslyComponent},
  {path: 'response/:hash', component: ResponseComponent},
  {path: 'invitation/:hash', component: InviteComponent},
  {path: 'program', component: ProgramComponent},
  {path: 'images', component: ImagesComponent},
  {path: '', redirectTo:'program', pathMatch:'full'},
  {path: '**', redirectTo: 'previously'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

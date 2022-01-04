import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProgramComponent } from './component/program/program.component';
import { ResponseComponent } from './component/response/response.component';
import { InviteComponent } from './component/invite/invite.component';
import { HttpClientModule } from '@angular/common/http';
import { HeaderComponent } from './component/header/header.component';
import { NavigationComponent } from './component/navigation/navigation.component';
import { FloatingStarsComponent } from './component/floating-stars/floating-stars.component';
import { NavigationButtonComponent } from './component/navigation/navigation-button/navigation-button.component';
import { PreviouslyComponent } from './component/previously/previously.component';
import { SafePipe } from './service/safe.pipe';

@NgModule({
  declarations: [
    AppComponent,
    ProgramComponent,
    ResponseComponent,
    InviteComponent,
    HeaderComponent,
    NavigationComponent,
    FloatingStarsComponent,
    NavigationButtonComponent,
    PreviouslyComponent,
    SafePipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

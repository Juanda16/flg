import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddDonorComponent } from './components/add-donor/add-donor.component';
import { DonorDetailsComponent } from './components/donor-details/donor-details.component';
import { DonorListComponent } from './components/donor-list/donor-list.component';
import { CookieModule, CookieService } from 'ngx-cookie';
//import {csrfTokenService} from "./csrf.service";
import {HttpClientXsrfModule} from '@angular/common/http';
import { LoginComponent } from './components/login/login.component';
import { LoginService } from './services/login.service';
import { AddDonationComponent } from './components/add-donation/add-donation.component';

@NgModule({
  declarations: [
    AppComponent,
    AddDonorComponent,
    DonorDetailsComponent,
    DonorListComponent,
    LoginComponent,
    AddDonationComponent,
   //RegisterComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    CookieModule.forRoot(),
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken',
      headerName: 'X-CSRFToken',
    }),
  ],
  providers: [CookieService,LoginService],
  bootstrap: [AppComponent]
})


export class AppModule { }




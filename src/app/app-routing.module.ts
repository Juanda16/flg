import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DonorDetailsComponent } from './components/donor-details/donor-details.component';
import { AddDonorComponent } from './components/add-donor/add-donor.component';
import { DonorListComponent } from './components/donor-list/donor-list.component';
import { LoginComponent } from './components/login/login.component';

const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'donor', component: DonorListComponent },
  { path: 'donor/:id', component: DonorDetailsComponent },
  { path: 'add', component: AddDonorComponent },
  { path: 'login', component : LoginComponent},
  //{ path: 'register',component: RegisterComponent}
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

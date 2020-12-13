import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DonorDetailsComponent } from './components/donor-details/donor-details.component';
import { AddDonorComponent } from './components/add-donor/add-donor.component';
import { DonorListComponent } from './components/donor-list/donor-list.component';

const routes: Routes = [
  { path: '', redirectTo: 'donor', pathMatch: 'full' },
  { path: 'donor', component: DonorListComponent },
  { path: 'donor/:id', component: DonorDetailsComponent },
  { path: 'add', component: AddDonorComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AddDonorComponent } from './components/add-donor/add-donor.component';


const routes: Routes = [
 // { path: '', redirectTo: 'tutorials', pathMatch: 'full' },
 // { path: 'tutorials', component: TutorialsListComponent },
 // { path: 'tutorials/:id', component: TutorialDetailsComponent },
  { path: 'add', component: AddDonorComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

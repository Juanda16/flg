import { Component, OnInit } from '@angular/core';
import { DonorService } from 'src/app/services/donor.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Donor,User } from 'src/app/models/donor.model';

@Component({
  selector: 'app-donor-details',
  templateUrl: './donor-details.component.html',
  styleUrls: ['./donor-details.component.css']
})
export class DonorDetailsComponent implements OnInit {
  currentDonor: User = {
    username: '',
    first_name: '',
    last_name : '',
    email:'',
    is_active: false,
  };
  message = '';

  constructor(
    private donorService: DonorService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.message = '';
    this.getDonor(this.route.snapshot.params.id);
  }

  getDonor(id: string): void {
    this.donorService.get(id)
      .subscribe(
        data => {
          this.currentDonor = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  updatePublished(status: boolean): void {
    const data = {
      username: this.currentDonor.username,
      password:this.currentDonor.password,
      first_name: this.currentDonor.first_name,
      last_name : this.currentDonor.last_name,
      email:this.currentDonor.email ,
      is_active:status
      
    };

    this.donorService.update(this.currentDonor.id, data)
      .subscribe(
        response => {
          this.currentDonor.is_active= status;
          console.log(response);
          this.message = response.message;
          //this.message = "Donor was updated";
        },
        error => {
          console.log(error);
        });
  }

  updateDonor(): void {
    this.donorService.update(this.currentDonor.id, this.currentDonor)
      .subscribe(
        response => {
          console.log(response);
          this.message = response.message;
          //this.message = "Donor was updated";
        },
        error => {
          console.log(error);
        });
  }

  deleteDonor(): void {
    this.donorService.delete(this.currentDonor.id)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/donor']);
        },
        error => {
          console.log(error);
        });
  }
}



import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/models/donor.model';
import { DonorService } from 'src/app/services/donor.service';

@Component({
  selector: 'app-donor-list',
  templateUrl: './donor-list.component.html',
  styleUrls: ['./donor-list.component.css']
})
export class DonorListComponent implements OnInit {
  donor?: User[];
  currentDonor?: User;
  currentIndex = -1;
  first_name = '';

  constructor(private donorService: DonorService) { }

  ngOnInit(): void {
    this.retrieveDonor();
  }

  retrieveDonor(): void {
    this.donorService.getAll()
      .subscribe(
        data => {
          this.donor = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveDonor();
    this.currentDonor = undefined;
    this.currentIndex = -1;
  }

  setActiveDonor(donor: User, index: number): void {
    this.currentDonor = donor;
    this.currentIndex = index;
  }

  removeAllDonor(): void {
    this.donorService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.refreshList();
        },
        error => {
          console.log(error);
        });
  }

  searchFirst_name(): void {
    this.donorService.findByFirst_name(this.first_name)
      .subscribe(
        data => {
          this.donor = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

}

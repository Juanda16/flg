import { Component, OnInit } from '@angular/core';
import { Donor } from 'src/app/models/donor.model';
import { DonorService } from 'src/app/services/donor.service';

@Component({
  selector: 'app-donor-list',
  templateUrl: './donor-list.component.html',
  styleUrls: ['./donor-list.component.css']
})
export class DonorListComponent implements OnInit {
  donor?: Donor[];
  currentDonor?: Donor;
  currentIndex = -1;
  documentId = '';

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

  setActiveDonor(donor: Donor, index: number): void {
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

   searchDocumentId(): void {
    this.donorService.findByDocumentId(this.documentId)
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

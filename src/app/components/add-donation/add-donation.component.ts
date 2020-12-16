import { Component, OnInit } from '@angular/core';
import { Donation } from 'src/app/models/donation.model';
import { DonationService } from 'src/app/services/donation.service';

@Component({
  selector: 'app-add-donation',
  templateUrl: './add-donation.component.html',
  styleUrls: ['./add-donation.component.css']
  })

export class AddDonationComponent implements OnInit {
  donation: Donation = {
  valueDonation: 0,
  transactionState: false
  };
  submitted = false;

  constructor(private donationService: DonationService) { }

  ngOnInit(): void {
    console.log("add donation component init")
  }

  saveDonation(): void {
    console.log("save donation")
    const data = {
      valueDonation: this.donation.valueDonation
    };

    this.donationService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
        },
        error => {
          console.log(error);
        });
  }

  newDonation(): void {
    this.submitted = false;
    this.donation = {
      valueDonation: 0,
      transactionState: false,
    };
  }
}

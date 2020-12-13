import { Component, OnInit } from '@angular/core';
import { Donor } from 'src/app/models/donor.model';
import { DonorService } from 'src/app/services/donor.service';

@Component({
  selector: 'app-add-donor',
  templateUrl: './add-donor.component.html',
  styleUrls: ['./add-donor.component.css']
})
export class AddDonorComponent implements OnInit {
  donor: Donor = {
    documentId: '',
    documentType: '',
    legalNature: false
  };

  submitted = false;

  constructor(private donorService: DonorService) { }
  
  ngOnInit(): void {
    console.log("add donor component init")
  }

  saveDonor(): void {
    console.log("save donor")
    const data = {
      documentId: this.donor.documentId,
      documentType: this.donor.documentType    
    };

    this.donorService.create(data)
      .subscribe(
        response => {
          console.log("donor service creted")
          console.log(response);
          this.submitted = true;
        },
        error => {
          console.log(error);
        });
  }

  newDonor(): void {
    this.submitted = false;
    this.donor = {
      documentId: '',
      documentType: '',
      legalNature: false
    };
  }
}

import { Component, OnInit } from '@angular/core';
import { Donor,User } from 'src/app/models/donor.model';
import { DonorService } from 'src/app/services/donor.service';

@Component({
  selector: 'app-add-donor',
  templateUrl: './add-donor.component.html',
  styleUrls: ['./add-donor.component.css']
})
export class AddDonorComponent implements OnInit {
  user: User = {
    username: '',
    password: '',
    first_name: '',
    last_name : '',
    email:'',
    is_active: false    
  };
  submitted = false;

  constructor(private donorService: DonorService) { }
  
  ngOnInit(): void {
    console.log("add donor component init")
  }

  saveDonor(): void {
    console.log("save donor")
    const data = {
      username: this.user.username,
      password:this.user.password,
      first_name: this.user.first_name,
      last_name : this.user.last_name,
      email:this.user.email  
    };

    this.donorService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
        },
        error => {
          console.log(error);
        });
  }

  newDonor(): void {
    this.submitted = false;
    this.user = {
    username: '',
    first_name: '',
    last_name : '',
    email:'',
    is_active: false,
    };
  }
}

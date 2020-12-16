import { Component, OnInit} from '@angular/core';
//import { CookieService } from 'angular2-cookie/core';
import { CookieService } from 'ngx-cookie';
import { LoginService } from 'src/app/services/login.service';
import { User } from 'src/app/models/donor.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(public auth: LoginService, public cookieService: CookieService) { 
    //this.cookieService.set( 'Test', 'Hello World' );
    //this.cookieValue = this.cookieService.get('csrftoken');
  }
  public user: any = new User();

  ngOnInit(): void {
  }
  LoginUser(){
  	console.log("login user");
    this.auth.login(this.user)
    /* .then((data)=>{
      console.log(data);
      if(data.status==200){
        if(data.json()['status']=='success'){
          this.cookieService.put('token', data.json()['token']);
        }else{
          console.log('Invalid Credentials');
        }
      }
      else{
        console.log("Some error occured")
      }
    }) */
  	
  }
    get diagnostic() { return JSON.stringify(this.user); }

}

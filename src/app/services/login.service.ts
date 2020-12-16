import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Donor } from '../models/donor.model';
import { HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie';
//import 'rxjs/add/operator/toPromise'

const baseUrl = '//127.0.0.1:8000/api/v1/donor';
/* const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    'X-CSRFToken': cookieService.get('csrftoken')
  })
}; */

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  public headers: Headers = new Headers({
        'content-type': 'application/json',
        'X-CSRFToken': this.cookieService.get('csrftoken')
      }) 
          
  constructor(private http: HttpClient, private cookieService: CookieService ){}

 

  login(user): Observable <any> {
		console.log(document.cookie['csrftoken']);
		return this.http.post(`${baseUrl}/login`, user)
  }
  
 
	register(user): Observable <any>{
		
		return this.http.post(`${baseUrl}/register`, user)
	}
}

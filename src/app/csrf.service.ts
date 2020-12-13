import {Injectable} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie';

@Injectable()
export class csrfTokenService {

    // http options used for making any writing API calls
    private httpOptions: any;

    constructor(private http:HttpClient, private _cookieService:CookieService) {
        // CSRF token is needed to make API calls work when logged in
        let csrf = this._cookieService.get("csrftoken");
        // the Angular HttpHeaders class throws an exception if any of the values are undefined
        if (typeof(csrf) === 'undefined') {
          csrf = '';
        }
        this.httpOptions = {
          headers: new HttpHeaders({ 'Content-Type': 'application/json', 'X-CSRFToken': csrf })
        };
    
    
    }   
 } 
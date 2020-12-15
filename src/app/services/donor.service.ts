import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { from, Observable } from 'rxjs';
import { Donor } from '../models/donor.model';
import { HttpHeaders } from '@angular/common/http';
import {CookieService} from 'ngx-cookie';

const baseUrl = '//127.0.0.1:8000/api/v1/donor';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    'X-CSRFToken': 'csrftoken'
  })
};

@Injectable({
  providedIn: 'root'
})
export class DonorService {
  constructor(private http: HttpClient, public cookieService: CookieService) { }

  get(id): Observable<any> {
    return this.http.get(`${baseUrl}/${id}`);
  }

  create(data): Observable<any> {
    return this.http.post(`${baseUrl}/`, data ,httpOptions);
  }

  update(id, data): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }

  delete(id): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }

  getAll():Observable<any> {
    return this.http.get(`${baseUrl}/`);
  }

  findByDocumentId(documentId: any): Observable<Donor[]> {
    return this.http.get<Donor[]>(`${baseUrl}?documentId=${documentId}`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }
 
}
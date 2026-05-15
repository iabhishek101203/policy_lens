import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class PolicyService {
  private apiBase = 'http://localhost:8000/api/policies';

  constructor(private http: HttpClient) {}

  search(query: any): Observable<any> {
    return this.http.post(`${this.apiBase}/search`, query);
  }

  getPolicy(id: string): Observable<any> {
    return this.http.get(`${this.apiBase}/${id}`);
  }

  suggest(profile: any): Observable<any> {
    return this.http.post(`${this.apiBase}/suggestions`, profile);
  }
}

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { UserBets } from '../shared/Interfaces/InterfaceUserBets';
import { Auth } from './auth';
import { BetResponse } from '../shared/Interfaces/InterfaceExtract';

@Injectable({
  providedIn: 'root',
})
export class Bet {

  private http = inject(HttpClient);
  private auth = inject(Auth);

  private BaseURL = 'http://localhost:8000/api/bet';

  UserBetsGet(): Observable<UserBets[]> {

    const token = this.auth.gettoken();

    return this.http.get<UserBets[]>(
      `${this.BaseURL}/bets/`,
      {
        withCredentials: true
      }
    );
  }

  UserBetPost(body: Object) {

    const token = this.auth.gettoken();

    console.log("TOKEN:", token);

    return this.http.post(
      `${this.BaseURL}/main/`,
      body,
      {
      
        withCredentials: true
      }
    );
  }

UserBetsExtract(): Observable<BetResponse> {

    const token = this.auth.gettoken();

    return this.http.get<BetResponse>(
      `${this.BaseURL}/extract/`,
      {
        headers: {
          Authorization: `Bearer ${token}`
        },
        withCredentials: true
      }
    );
  }
}
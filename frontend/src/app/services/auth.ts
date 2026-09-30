import { HttpClient } from '@angular/common/http';
import { inject, Injectable, signal } from '@angular/core';
import { LoginResponse } from '../shared/Interfaces/InterfaceAccessToken';

@Injectable({ providedIn: 'root' })
export class Auth {
  private http = inject(HttpClient);
  private baseURL = 'http://localhost:8000/api/auth';
  private accesstoken: string | null = null;

  login(username: string, password: string) {
    localStorage.setItem('user', JSON.stringify(username));
    return this.http.post<LoginResponse>(`${this.baseURL}/login/`, { username, password }, { withCredentials: true });
  }

  register(username: string, first_name: string, email: string, password: string) {
    return this.http.post(`${this.baseURL}/register/`, { username, first_name, email, password }, { withCredentials: true });
  }

  gettoken() {
    return this.accesstoken;
  }

  settoken(token: string) {
    this.accesstoken = token;
  }

  refresh() {
    return this.http.post<any>(`${this.baseURL}/refresh/`, {}, { withCredentials: true }); // ✅ URL correta
  }

  logout() {
    this.accesstoken = null;
    this.http.post(`${this.baseURL}/logout/`, {}, { withCredentials: true }).subscribe();  // ✅ URL correta
  }

  isAuthenticated() {
    return !!this.accesstoken;
  }
}

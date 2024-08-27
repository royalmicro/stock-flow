import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { EnvironmentService } from '../environment/environment.service';
import { AppModule } from '../../app.module';

@Injectable({
  providedIn: AppModule,
})
export class AuthService {
  constructor(
    private http: HttpClient,
    private envService: EnvironmentService,
  ) {}

  login(
    username?: string | null,
    password?: string | null,
  ): Observable<{ token: string; user: any }> {
    return this.http.post<{ token: string; user: any }>(
      `${this.envService.apiUrl}/auth/login`,
      { username, password },
    );
  }

  logout(): void {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  }

  setToken(token: string): void {
    localStorage.setItem('token', token);
  }

  getToken(): string | null {
    return localStorage.getItem('token');
  }
}

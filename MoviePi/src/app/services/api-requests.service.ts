import { ApiResponse } from './../interfaces/api-response';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../interfaces/user';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiRequestsService {
  private API_SERVER_ADDRESS = 'http://10.15.194.88:4242/api/v1/';

  constructor(private httpClient: HttpClient) {}

  register(user: User, genres): Observable<ApiResponse> {
    return this.httpClient.post<ApiResponse>(`${this.API_SERVER_ADDRESS}user`, {
      userInfos: user,
      genres
    });
  }

  login(user: User): Observable<ApiResponse> {
    return this.httpClient.post<ApiResponse>(
      `${this.API_SERVER_ADDRESS}users`,
      user
    );
  }

  reauth(): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(`${this.API_SERVER_ADDRESS}user`);
  }

  getGenres(): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(`${this.API_SERVER_ADDRESS}genres`);
  }

  checkUsername(username: string): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(
      `${this.API_SERVER_ADDRESS}checkUsername/${username}`
    );
  }
}

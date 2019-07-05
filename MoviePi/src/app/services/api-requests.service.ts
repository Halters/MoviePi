import { ApiResponse } from './../interfaces/api-response';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../interfaces/user';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiRequestsService {
  private API_SERVER_ADDRESS = 'http://51.75.141.254/api/v1/';

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
    return this.httpClient.get<ApiResponse>(`${this.API_SERVER_ADDRESS}users`);
  }

  getGenres(): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(`${this.API_SERVER_ADDRESS}genres`);
  }

  getFilmsFromPage(page: number): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(
      `${this.API_SERVER_ADDRESS}films/page/${page}`
    );
  }

  getFilmsSeen(): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(
      `${this.API_SERVER_ADDRESS}user/filmsSeen`
    );
  }

  checkUsername(username: string): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(
      `${this.API_SERVER_ADDRESS}checkUsername/${username}`
    );
  }

  getSuggestions(): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(
      `${this.API_SERVER_ADDRESS}suggestions`
    );
  }

  updatePreferences({
    uuid,
    username,
    age,
    password
  }: {
    uuid: string;
    username: string;
    age: number;
    password?: string;
  }): Observable<ApiResponse> {
    const packet = { uuid, username, age, password };
    return this.httpClient.patch<ApiResponse>(
      `${this.API_SERVER_ADDRESS}user/settings`,
      packet
    );
  }
}

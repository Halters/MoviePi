import { AuthResponse } from './../interfaces/auth-response';
import { ApiResponse } from './../interfaces/api-response';
import { ApiRequestsService } from './api-requests.service';
import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';
import { BehaviorSubject } from 'rxjs';
import { User } from '../interfaces/user';
import { Platform } from '@ionic/angular';
import { JwtHelperService } from '@auth0/angular-jwt';

const TOKEN_KEY = 'ACCESS_TOKEN';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  authenticationState = new BehaviorSubject(false);
  user: User;

  constructor(
    private storage: Storage,
    private apiRequests: ApiRequestsService,
    private plt: Platform
  ) {
    this.plt.ready().then(() => {
      this.checkToken();
    });
  }

  checkToken() {
    this.storage.get(TOKEN_KEY).then(token => {
      if (token) {
        this.reauth();
      }
    });
  }

  register(user: User, genres) {
    this.apiRequests
      .register(user, genres)
      .subscribe(async (res: ApiResponse) => {
        if (res.data) {
          const data = res.data as AuthResponse;
          await this.storage.set(TOKEN_KEY, data.JWT);
          this.user = data.userInfos;
          this.authenticationState.next(true);
        }
      });
  }

  login(user: User) {
    this.apiRequests.login(user).subscribe(async (res: ApiResponse) => {
      if (res.data) {
        const data = res.data as AuthResponse;
        await this.storage.set(TOKEN_KEY, data.JWT);
        console.log(data);
        this.user = data.userInfos;
        this.authenticationState.next(true);
      }
    });
  }

  reauth() {
    this.apiRequests.reauth().subscribe(async (res: ApiResponse) => {
      if (res.data) {
        const data = res.data as AuthResponse;
        await this.storage.set(TOKEN_KEY, data.JWT);
        this.user = data.userInfos;
        this.authenticationState.next(true);
      }
    });
  }

  async logout() {
    await this.storage.remove(TOKEN_KEY);
    this.user = null;
    this.authenticationState.next(false);
  }

  isAuthenticated() {
    return this.authenticationState.value;
  }
}

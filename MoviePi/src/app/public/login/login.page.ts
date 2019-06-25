import { AuthenticationService } from './../../services/authentication.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss']
})
export class LoginPage {
  constructor(private authService: AuthenticationService) {}

  login() {
    this.authService.login();
  }
}

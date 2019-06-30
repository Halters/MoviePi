import { User } from './../../interfaces/user';
import { AuthenticationService } from './../../services/authentication.service';
import { Component } from '@angular/core';
import { Validators, FormGroup, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss']
})
export class LoginPage {
  loginForm: FormGroup;
  invalidLogin = false;

  constructor(
    private authService: AuthenticationService,
    private formBuilder: FormBuilder
  ) {
    this.loginForm = this.formBuilder.group({
      username: ['', [Validators.required]],
      password: ['', [Validators.required]]
    });
  }

  login() {
    if (this.loginForm.valid) {
      this.invalidLogin = false;
      const user: User = {
        username: this.loginForm.get('username').value,
        password: this.loginForm.get('password').value,
        age: undefined,
        uuid: undefined
      };
      this.authService.login(user);
    } else {
      this.invalidLogin = true;
    }
  }
}

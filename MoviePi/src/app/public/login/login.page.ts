import { AuthenticationService } from './../../services/authentication.service';
import { Component } from '@angular/core';
import { Validators, FormGroup, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss']
})
export class LoginPage {
  public loginForm: FormGroup;

  constructor(
    private authService: AuthenticationService,
    public formBuilder: FormBuilder
  ) {
    this.loginForm = formBuilder.group({
      username: ['', [Validators.required]],
      password: ['', [Validators.required]]
    });
  }

  login() {
    if (this.loginForm.valid) {
      console.log('success');
    }
    this.authService.login();
  }
}

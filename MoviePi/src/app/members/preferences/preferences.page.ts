import { AuthResponse } from './../../interfaces/auth-response';
import { ApiResponse } from './../../interfaces/api-response';
import { User } from './../../interfaces/user';
import { AuthenticationService } from './../../services/authentication.service';
import { Component } from '@angular/core';
import { Storage } from '@ionic/storage';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ApiRequestsService } from 'src/app/services/api-requests.service';
import { PasswordValidator } from 'src/app/validators/password';
import { AgeValidator } from 'src/app/validators/age';
import { Router } from '@angular/router';

@Component({
  selector: 'app-preferences',
  templateUrl: './preferences.page.html',
  styleUrls: ['./preferences.page.scss']
})
export class PreferencesPage {
  passwordForm: FormGroup;
  ageForm: FormGroup;
  userInfos: User;

  constructor(
    public formBuilder: FormBuilder,
    private authService: AuthenticationService,
    private apiRequests: ApiRequestsService,
    private storage: Storage,
    private router: Router
  ) {
    this.userInfos = this.authService.user;
    this.passwordForm = formBuilder.group(
      {
        password: ['password', [Validators.required]],
        passwordConfirmation: ['password', [Validators.required]]
      },
      { validator: PasswordValidator.checkPasswords }
    );

    this.ageForm = formBuilder.group({
      age: [this.userInfos.age, AgeValidator.isValid]
    });
  }

  save() {
    if (this.passwordForm.valid && this.ageForm.valid) {
      this.userInfos.password = this.passwordForm.get('password').value;
      this.userInfos.age = this.ageForm.get('age').value;
      this.apiRequests
        .updatePreferences(this.userInfos)
        .subscribe(async (res: ApiResponse) => {
          if (res.data) {
            const data = res.data as AuthResponse;
            this.storage.set('ACCESS_TOKEN', data.JWT);
            this.authService.user = data.userInfos;
          }
        });
    } else if (this.ageForm.valid) {
      this.userInfos.password = undefined;
      this.userInfos.age = this.ageForm.get('age').value;
      this.apiRequests
        .updatePreferences(this.userInfos)
        .subscribe(async (res: ApiResponse) => {
          if (res.data) {
            const data = res.data as AuthResponse;
            this.storage.set('ACCESS_TOKEN', data.JWT);
            this.authService.user = data.userInfos;
          }
        });
    }
    this.router.navigate(['members', 'home']);
  }
}

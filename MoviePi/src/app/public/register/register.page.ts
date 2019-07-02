import {
  UsernameValidatorDirective,
  usernameValidator
} from './../../validators/username-validator.directive';
import { ApiResponse } from './../../interfaces/api-response';
import { ApiRequestsService } from './../../services/api-requests.service';
import { User } from './../../interfaces/user';
import { AuthenticationService } from './../../services/authentication.service';
import { PasswordValidator } from './../../validators/password';
import { AgeValidator } from './../../validators/age';
import { Component, ViewChild, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { IonInfiniteScroll, IonSlides } from '@ionic/angular';

@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss']
})
export class RegisterPage implements OnInit {
  @ViewChild(IonInfiniteScroll) infiniteScroll: IonInfiniteScroll;
  @ViewChild('signupSlider') signupSlider: IonSlides;
  accountInfos: FormGroup;
  passwordForm: FormGroup;
  ageForm: FormGroup;
  attemptRegister = false;
  genres: any = undefined;
  prevButtonVisibility = 'hidden';
  nextButtonVisibility = 'visible';

  constructor(
    public formBuilder: FormBuilder,
    private authService: AuthenticationService,
    private apiRequests: ApiRequestsService
  ) {
    this.accountInfos = formBuilder.group({
      username: [
        '',
        Validators.compose([
          Validators.required,
          Validators.pattern('[a-zA-Z]*')
        ]),
        usernameValidator(this.apiRequests)
      ]
    });

    this.passwordForm = formBuilder.group(
      {
        password: ['', [Validators.required]],
        passwordConfirmation: ['', [Validators.required]]
      },
      { validator: PasswordValidator.checkPasswords }
    );

    this.ageForm = formBuilder.group({
      age: ['', AgeValidator.isValid]
    });

    this.initializeGenres();
  }

  ngOnInit() {
    this.signupSlider.ionSlideDidChange.subscribe(e => {
      this.signupSlider.isBeginning().then((v: boolean) => {
        if (v) {
          this.prevButtonVisibility = 'hidden';
        } else {
          this.prevButtonVisibility = 'visible';
        }
      });
      this.signupSlider.isEnd().then((v: boolean) => {
        if (!v) {
          this.nextButtonVisibility = 'visible';
        } else {
          this.nextButtonVisibility = 'hidden';
        }
      });
    });
  }

  initializeGenres() {
    this.apiRequests.getGenres().subscribe(async (res: ApiResponse) => {
      this.genres = res.data;
      for (const item of this.genres) {
        item.isChecked = false;
      }
    });
  }

  next() {
    this.signupSlider.slideNext();
  }

  prev() {
    this.signupSlider.slidePrev();
  }

  isFirst() {
    return this.signupSlider.isBeginning();
  }

  save() {
    console.log(this.accountInfos.controls.username.errors);
    this.attemptRegister = true;
    const genres = this.genres.filter(i => i.isChecked);
    if (
      !this.accountInfos.valid ||
      !this.passwordForm.valid ||
      !this.ageForm.valid
    ) {
      this.signupSlider.slideTo(0);
    } else if (genres.length < 5) {
      this.signupSlider.slideTo(1);
    } else {
      this.attemptRegister = false;
      const user: User = {
        uuid: undefined,
        username: this.accountInfos.get('username').value,
        password: this.passwordForm.get('password').value,
        age: this.ageForm.get('age').value,
        genres: null
      };
      this.authService.register(user, genres);
    }
  }
}

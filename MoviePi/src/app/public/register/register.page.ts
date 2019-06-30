import { User } from './../../interfaces/user';
import { AuthenticationService } from './../../services/authentication.service';
import { PasswordValidator } from './../../validators/password';
import { AgeValidator } from './../../validators/age';
import { UsernameValidator } from './../../validators/username';
import { Component, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { IonInfiniteScroll, IonSlides } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss']
})
export class RegisterPage {
  @ViewChild(IonInfiniteScroll) infiniteScroll: IonInfiniteScroll;
  @ViewChild('signupSlider') signupSlider: IonSlides;
  accountInfos: FormGroup;
  passwordForm: FormGroup;
  ageForm: FormGroup;
  attemptRegister = false;
  items = [];

  constructor(
    public formBuilder: FormBuilder,
    private http: HttpClient,
    private authService: AuthenticationService
  ) {
    this.http
      .get('http://10.15.193.10:5002/filmsearch/title=star')
      .subscribe(response => {
        console.log(response);
      });

    this.accountInfos = formBuilder.group({
      username: [
        '',
        Validators.compose([
          Validators.required,
          Validators.pattern('[a-zA-Z]*')
        ]),
        UsernameValidator.checkUsername
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

    this.initializeItems();
  }

  initializeItems() {
    this.items = [];
    for (let i = 0; i < 10; i++) {
      this.items.push({ val: i.toString(), isChecked: false });
    }
  }

  getItems(ev) {
    // this.initializeItems();
    // const val = ev.target.value;
    // if (val && val.trim() !== '') {
    //   this.items = this.items.filter(item => {
    //     return item.val.toLowerCase().indexOf(val.toLowerCase()) > -1;
    //   });
    // }
  }

  loadData(event) {
    setTimeout(() => {
      console.log('Done');
      for (let i = 0; i < 10; i++) {
        this.items.push({ val: i.toString(), isChecked: false });
      }
      event.target.complete();

      if (this.items.length === 50) {
        event.target.disabled = true;
      }
    }, 500);
  }

  next() {
    this.signupSlider.slideNext();
  }

  prev() {
    this.signupSlider.slidePrev();
  }

  save() {
    this.attemptRegister = true;
    if (!this.accountInfos.valid || !this.passwordForm.valid) {
      this.signupSlider.slideTo(0);
    } else if (!this.ageForm.valid) {
      this.signupSlider.slideTo(1);
    } else {
      this.attemptRegister = false;
      const user: User = {
        uuid: undefined,
        username: this.accountInfos.get('username').value,
        password: this.passwordForm.get('password').value,
        age: this.ageForm.get('age').value
      };
      const genres = null;
      this.authService.register(user, genres);
    }
  }
}

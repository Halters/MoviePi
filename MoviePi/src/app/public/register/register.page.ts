import { PasswordValidator } from './../../validators/password';
import { AgeValidator } from './../../validators/age';
import { UsernameValidator } from './../../validators/username';
import { Component, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { IonInfiniteScroll } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss']
})
export class RegisterPage {
  @ViewChild(IonInfiniteScroll) infiniteScroll: IonInfiniteScroll;
  @ViewChild('signupSlider') signupSlider;
  public slideOneForm: FormGroup;
  public passwordForm: FormGroup;
  public slideTwoForm: FormGroup;
  // public films: Observable<any>;
  public items = [];

  constructor(public formBuilder: FormBuilder, private http: HttpClient) {
    this.http
      .get('http://10.15.193.10:5002/filmsearch/title=star')
      .subscribe(response => {
        console.log(response);
      });

    this.slideOneForm = formBuilder.group({
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

    this.slideTwoForm = formBuilder.group({
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
    if (!this.slideOneForm.valid || !this.passwordForm.valid) {
      this.signupSlider.slideTo(0);
    } else if (!this.slideTwoForm.valid) {
      this.signupSlider.slideTo(1);
    } else {
      console.log('success!');
      console.log(this.slideOneForm.value);
      console.log(this.passwordForm.value);
      console.log(this.slideTwoForm.value);
    }
  }
}

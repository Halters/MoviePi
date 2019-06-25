import { PasswordValidator } from './../../validators/password';
import { AgeValidator } from './../../validators/age';
import { UsernameValidator } from './../../validators/username';
import { Component, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss']
})
export class RegisterPage {
  @ViewChild('signupSlider') signupSlider;
  public slideOneForm: FormGroup;
  public passwordForm: FormGroup;
  public slideTwoForm: FormGroup;

  constructor(public formBuilder: FormBuilder) {
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
  }

  next() {
    this.signupSlider.slideNext();
  }

  prev() {
    this.signupSlider.slidePrev();
  }

  save() {
    console.log(this.slideTwoForm.controls.age);
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

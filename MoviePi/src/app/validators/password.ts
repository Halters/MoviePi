import { FormGroup } from '@angular/forms';

export class PasswordValidator {
  static checkPasswords(group: FormGroup) {
    const pass = group.controls.password.value;
    const confirmPass = group.controls.passwordConfirmation.value;

    return pass === confirmPass ? null : { notSame: true };
  }
}

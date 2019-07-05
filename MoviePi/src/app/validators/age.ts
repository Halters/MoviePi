import { FormControl } from '@angular/forms';

export class AgeValidator {
  static isValid(control: FormControl): any {
    if (isNaN(control.value)) {
      return {
        error: 'Ce n\'est pas un nombre'
      };
    }
    if (control.value % 1 !== 0) {
      return {
        error: 'Ce n\'est pas un nombre entier'
      };
    }
    if (control.value > 120) {
      return {
        error: 'Vous n\'êtes pas si vieux?!'
      };
    }
    if (control.value <= 0) {
      return {
        error: 'Trop jeune ?!'
      };
    }
    return null;
  }
}

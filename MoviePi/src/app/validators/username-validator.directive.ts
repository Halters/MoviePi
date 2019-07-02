import { Directive } from '@angular/core';
import {
  NG_ASYNC_VALIDATORS,
  AsyncValidator,
  AbstractControl,
  ValidationErrors,
  AsyncValidatorFn
} from '@angular/forms';
import { ApiRequestsService } from '../services/api-requests.service';
import { map, catchError } from 'rxjs/operators';
import { ApiResponse } from '../interfaces/api-response';
import { of } from 'rxjs';

export function usernameValidator(
  apiRequests: ApiRequestsService
): AsyncValidatorFn {
  return (
    control: AbstractControl
  ):
    | Promise<ValidationErrors>
    | import('rxjs').Observable<ValidationErrors> => {
    return apiRequests.checkUsername(control.value).pipe(
      map((infos: ApiResponse) => {
        return infos.data ? null : { error: infos.message };
      }),
      catchError(() => of(null))
    );
  };
}

@Directive({
  selector: '[appUsernameValidator]',
  providers: [
    {
      provide: NG_ASYNC_VALIDATORS,
      useExisting: UsernameValidatorDirective,
      multi: true
    }
  ]
})
export class UsernameValidatorDirective implements AsyncValidator {
  constructor(private apiRequests: ApiRequestsService) {}

  validate(
    control: AbstractControl
  ): Promise<ValidationErrors> | import('rxjs').Observable<ValidationErrors> {
    return this.apiRequests.checkUsername(control.value).pipe(
      map(infos => {
        return infos.data ? null : { error: infos.message };
      }),
      catchError(() => of(null))
    );
  }
}

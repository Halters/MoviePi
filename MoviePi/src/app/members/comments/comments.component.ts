import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { AuthenticationService } from './../../services/authentication.service';
import { User } from './../../interfaces/user';
import { Comment } from './../../interfaces/comment';
import { ApiRequestsService } from 'src/app/services/api-requests.service';
import { ApiResponse } from '../../interfaces/api-response';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.scss']
})
export class CommentsComponent {
  @Input() filmId: number;
  comments: Array<Comment>;
  user: User;
  submitCommentForm: FormGroup;

  constructor(
    private apiRequests: ApiRequestsService,
    private authService: AuthenticationService,
    private formBuilder: FormBuilder
  ) {
    this.apiRequests
      .getComments(this.filmId)
      .subscribe(async (res: ApiResponse) => {
        if (res && res.data) {
          this.comments = res.data as Comment[];
        }
      });
    this.submitCommentForm = this.formBuilder.group({
      comment: ['', [Validators.required]]
    });
    this.user = this.authService.user;
  }

  delete(commentId: number) {
    this.apiRequests
      .deleteComment(commentId)
      .subscribe(async (res: ApiResponse) => {
        if (res && res.data) {
          this.comments = res.data as Comment[];
        }
      });
  }

  edit() {}

  save() {
    if (this.submitCommentForm.valid) {
      this.apiRequests
        .postComment(this.filmId, this.submitCommentForm.get('comment').value)
        .subscribe(async (res: ApiResponse) => {
          if (res && res.data) {
            this.comments = res.data as Comment[];
            this.submitCommentForm.get('comment').setValue('');
          }
        });
    }
  }
}

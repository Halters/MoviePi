import { Comments } from './../../interfaces/comments';
import { User } from './../../interfaces/user';
import { FilmDetails } from 'src/app/interfaces/film';
import { ColorsStars } from './../../enums/colors-stars.enum';
import { Component, AfterContentInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiRequestsService } from './../../services/api-requests.service';
import { ApiResponse } from './../../interfaces/api-response';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-filmdetails',
  templateUrl: './filmdetails.page.html',
  styleUrls: ['./filmdetails.page.scss']
})
export class FilmdetailsPage implements AfterContentInit {
  filmDetails: FilmDetails = undefined;
  id = null;
  comments: Comments[];
  isChecked = false;
  disabled = false;
  filmsSeen;
  userRate = 0;
  TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500';
  NO_IMAGE = 'assets/image-not-found.jpg';
  user: User;
  submitCommentForm: FormGroup;

  constructor(
    private activatedRoute: ActivatedRoute,
    private apiRequests: ApiRequestsService,
    private authService: AuthenticationService,
    private formBuilder: FormBuilder
  ) {
    this.submitCommentForm = this.formBuilder.group({
      comment: ['', [Validators.required]]
    });
    this.user = this.authService.user;
    this.apiRequests
      .getRateUser(this.id)
      .subscribe(async (res: ApiResponse) => {
        if (res && res.data) {
          this.userRate = res.data.rating;
        }
      });
  }

  ngAfterContentInit() {
    this.id = this.activatedRoute.snapshot.paramMap.get('id');
    this.apiRequests
      .getFilmDetails(this.id)
      .subscribe(async (res: ApiResponse) => {
        if (res && res.data) {
          this.filmDetails = res.data[0];
          this.filmDetails.rating = Math.round(this.filmDetails.rating / 2);
          this.getComments();
          this.initializeFilmsSeen();
        }
      });
  }

  initializeFilmsSeen() {
    this.apiRequests.getFilmsSeen().subscribe(async (res: ApiResponse) => {
      this.filmsSeen = res.data;
      for (const film of this.filmsSeen) {
        if (film.title === this.filmDetails.title) {
          this.isChecked = true;
          this.disabled = true;
        }
      }
    });
  }

  rate(index: number) {
    this.userRate = index;
    this.apiRequests
      .updateRate(this.id, index)
      .subscribe(async (res: ApiResponse) => {});
  }

  getColor(index: number) {
    if (this.isAboveRating(index)) {
      return ColorsStars.GREY;
    }
    switch (this.userRate) {
      case 1:
      case 2:
        return ColorsStars.RED;
      case 3:
        return ColorsStars.YELLOW;
      case 4:
      case 5:
        return ColorsStars.GREEN;
      default:
        return ColorsStars.GREY;
    }
  }

  getColorGlobal(index: number) {
    if (this.isAboveRatingGlobal(index)) {
      return ColorsStars.GREY;
    }
    switch (this.filmDetails.rating) {
      case 1:
      case 2:
        return ColorsStars.RED;
      case 3:
        return ColorsStars.YELLOW;
      case 4:
      case 5:
        return ColorsStars.GREEN;
      default:
        return ColorsStars.GREY;
    }
  }
  isAboveRatingGlobal(index: number): boolean {
    return index > this.filmDetails.rating;
  }

  isAboveRating(index: number): boolean {
    return index > this.userRate;
  }

  checkboxClicked(event) {
    if (!this.disabled) {
      this.apiRequests
        .updateFilmsSeen(this.id)
        .subscribe(async (res: ApiResponse) => {});
      this.disabled = true;
    }
  }

  getComments() {
    this.apiRequests
      .getComments(this.filmDetails.id)
      .subscribe(async (res: ApiResponse) => {
        console.log(res);
        if (res && res.data) {
          this.comments = res.data as Comments[];
        } else if (res && !res.data) {
          this.comments = null;
        }
      });
    this.user = this.authService.user;
  }

  delete(commentId: number) {
    this.apiRequests
      .deleteComment(commentId)
      .subscribe(async (res: ApiResponse) => {
        this.getComments();
      });
  }

  edit() {}

  save() {
    if (this.submitCommentForm.valid) {
      this.apiRequests
        .postComment(
          this.filmDetails.id,
          this.submitCommentForm.get('comment').value
        )
        .subscribe(async (res: ApiResponse) => {
          if (res && res.data) {
            this.comments = res.data as Comments[];
            this.submitCommentForm.get('comment').setValue('');
          }
        });
    }
  }
}

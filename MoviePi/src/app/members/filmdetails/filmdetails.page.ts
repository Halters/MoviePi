import { FilmDetails } from 'src/app/interfaces/film';
import { ColorsStars } from './../../enums/colors-stars.enum';
import { Component, OnInit, EventEmitter } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiRequestsService } from './../../services/api-requests.service';
import { ApiResponse } from './../../interfaces/api-response';

@Component({
  selector: 'app-filmdetails',
  templateUrl: './filmdetails.page.html',
  styleUrls: ['./filmdetails.page.scss']
})
export class FilmdetailsPage implements OnInit {
  filmDetails: FilmDetails;
  id = null;
  isChecked = false;
  disabled = false;
  filmsSeen;
  userRate = 0;
  TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500';
  NO_IMAGE = 'assets/image-not-found.jpg';

  constructor(
    private activatedRoute: ActivatedRoute,
    private apiRequests: ApiRequestsService
  ) {
    this.id = this.activatedRoute.snapshot.paramMap.get('id');
    this.apiRequests
      .getFilmDetails(this.id)
      .subscribe(async (res: ApiResponse) => {
        if (res && res.data) {
          this.filmDetails = res.data[0];
          this.filmDetails.rating = Math.round(this.filmDetails.rating / 2);
          this.initializeFilmsSeen();
        }
      });
  }

  ngOnInit() {}

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
}

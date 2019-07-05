import { Film } from 'src/app/interfaces/film';
import { ApiResponse } from './../../interfaces/api-response';
import { ApiRequestsService } from 'src/app/services/api-requests.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss']
})
export class HomePage {
  films: Array<Film>;
  TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500';
  NO_IMAGE = 'assets/image-not-found.jpg';
  maxPage: number;

  constructor(private apiRequests: ApiRequestsService) {
    this.apiRequests.getActivityThread().subscribe(async (res: ApiResponse) => {
      if (res && res.data) {
        this.maxPage = res.data;
        this.getFilms();
      }
    });
  }

  getFilms() {
    this.apiRequests
      .getFilmsFromPage(Math.floor(Math.random() * this.maxPage))
      .subscribe(async (res: ApiResponse) => {
        if (res && res.data) {
          this.films = res.data as Film[];
        }
      });
  }
}

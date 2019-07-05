import { Film } from 'src/app/interfaces/film';
import { Component, OnInit } from '@angular/core';
import { ApiRequestsService } from './../../services/api-requests.service';
import { ApiResponse } from './../../interfaces/api-response';

@Component({
  selector: 'app-filmsseen',
  templateUrl: './filmsseen.page.html',
  styleUrls: ['./filmsseen.page.scss']
})
export class FilmsseenPage implements OnInit {
  films: Array<Film>;
  TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500';
  NO_IMAGE = 'assets/image-not-found.jpg';

  constructor(private apiRequests: ApiRequestsService) {
    this.initializeFilmsSeen();
  }

  ngOnInit() {}

  initializeFilmsSeen() {
    this.apiRequests.getFilmsSeen().subscribe(async (res: ApiResponse) => {
      if (res && res.data) {
        this.films = res.data;
      }
    });
  }
}

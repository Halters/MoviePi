import { ApiResponse } from './../../interfaces/api-response';
import { Film } from 'src/app/interfaces/film';
import { ApiRequestsService } from 'src/app/services/api-requests.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-suggestions',
  templateUrl: './suggestions.page.html',
  styleUrls: ['./suggestions.page.scss']
})
export class SuggestionsPage implements OnInit {
  films: Array<Film>;
  TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500';
  NO_IMAGE = 'assets/image-not-found.jpg';

  constructor(private apiRequests: ApiRequestsService) {}

  initializeSuggestions() {
    this.apiRequests.getSuggestions().subscribe(async (res: ApiResponse) => {
      if (res && res.data) {
        this.films = res.data;
      }
    });
  }

  ngOnInit() {
    this.initializeSuggestions();
  }
}

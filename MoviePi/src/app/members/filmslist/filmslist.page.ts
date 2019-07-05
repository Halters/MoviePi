import { Component, OnInit, ViewChild } from '@angular/core';
import { ApiResponse } from './../../interfaces/api-response';
import { ApiRequestsService } from './../../services/api-requests.service';
import { IonInfiniteScroll } from '@ionic/angular';
import { Film } from 'src/app/interfaces/film';

@Component({
  selector: 'app-filmslist',
  templateUrl: './filmslist.page.html',
  styleUrls: ['./filmslist.page.scss']
})
export class FilmslistPage implements OnInit {
  @ViewChild(IonInfiniteScroll) infiniteScroll: IonInfiniteScroll;
  searchOpen = false;
  dropDown = false;
  films: Array<Film>;
  searchMode = false;
  actualPage = 0;
  TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500';
  NO_IMAGE = 'assets/image-not-found.jpg';

  constructor(private apiRequests: ApiRequestsService) {
    this.initializeFilmsSeen();
  }

  ngOnInit() {}

  initializeFilmsSeen() {
    this.apiRequests
      .getFilmsFromPage(this.actualPage)
      .subscribe(async (res: ApiResponse) => {
        if (res && res.data) {
          this.films = res.data;
          console.log(this.films);
        }
      });
  }

  loadData(event) {
    this.actualPage += 1;
    this.apiRequests.getFilmsFromPage(this.actualPage).subscribe(rep => {
      if (rep) {
        if (!rep.data) {
          this.infiniteScroll.disabled = true;
        } else {
          this.films.push(rep.data);
          console.log(this.films);
        }
        this.infiniteScroll.complete();
      }
    });
  }
}

import { Component, OnInit, ViewChild } from '@angular/core';
import { ApiResponse } from './../../interfaces/api-response';
import { ApiRequestsService } from './../../services/api-requests.service';
import { IonInfiniteScroll } from '@ionic/angular';
import { Film } from 'src/app/interfaces/film';
import { FormControl } from '@angular/forms';
import { debounceTime } from 'rxjs/operators';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/switchMap';

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
  displayFilms: Array<Film>;
  genres: any = undefined;
  searchTerm = '';
  searchControl: FormControl;
  searching: any = false;
  searchMode = false;
  actualPage = 0;
  searchData = [];
  TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500';
  NO_IMAGE = 'assets/image-not-found.jpg';

  constructor(private apiRequests: ApiRequestsService) {
    this.initializeFilms();
    this.initializeGenres();
    this.searchControl = new FormControl();
  }

  ngOnInit() {
    this.setFilteredItems();
    this.searchControl.valueChanges
      .pipe(debounceTime(700))
      .subscribe(search => {
        this.setFilteredItems();
      });
  }

  initializeFilms() {
    this.apiRequests
      .getFilmsFromPage(this.actualPage)
      .subscribe(async (res: ApiResponse) => {
        if (res && res.data) {
          this.films = res.data;
          this.displayFilms = this.films.slice(0);
          console.log(this.films);
        }
      });
  }

  initializeGenres() {
    this.apiRequests.getGenres().subscribe(async (res: ApiResponse) => {
      this.genres = res.data;
    });
  }

  loadData(event) {
    this.actualPage += 1;
    this.apiRequests.getFilmsFromPage(this.actualPage).subscribe(rep => {
      if (rep) {
        if (!rep.data) {
          this.infiniteScroll.disabled = true;
        } else {
          this.films = this.films + rep.data;
          this.displayFilms = this.films.slice(0);
        }
        this.infiniteScroll.complete();
      }
    });
  }

  onChangeGenre(value: number) {
    this.actualPage = 0;
    if (value === 0) {
      this.initializeFilms();
    } else {
      this.apiRequests.getFilmsFromPage(value).subscribe(rep => {
        if (rep && rep.data) {
          this.films = rep.data as Film[];
          this.displayFilms = this.films.slice(0);
        }
      });
    }
  }

  cancelSearch() {
    this.displayFilms = this.films.slice(0);
    this.searchOpen = false;
  }

  onSearchInput() {
    this.searchTerm = this.searchControl.value;
    this.setFilteredItems();
    this.searchControl.valueChanges.debounceTime(700).subscribe(search => {
      this.setFilteredItems();
    });
  }

  setFilteredItems() {
    if (this.films) {
      this.searchData = this.films.slice(0);
      this.searchData = this.filterItems(this.searchTerm).slice(0);
      this.displayFilms = this.searchData.slice(0);
    }
  }

  filterItems(searchTerm) {
    const data = this.films.slice(0);
    this.infiniteScroll.disabled = true;
    if (!searchTerm) {
      this.infiniteScroll.disabled = false;
      this.displayFilms = this.films.slice(0);
      return this.displayFilms;
    }
    return data.filter(film => {
      return film.title.toLowerCase().indexOf(searchTerm.toLowerCase()) > -1;
    });
  }
}

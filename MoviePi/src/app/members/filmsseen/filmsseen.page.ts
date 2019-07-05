import { Component, ViewChild, OnInit } from '@angular/core';
import { IonInfiniteScroll } from '@ionic/angular';
import { ApiRequestsService } from './../../services/api-requests.service';
import { ApiResponse } from './../../interfaces/api-response';

@Component({
  selector: 'app-filmsseen',
  templateUrl: './filmsseen.page.html',
  styleUrls: ['./filmsseen.page.scss']
})
export class FilmsseenPage implements OnInit {
  @ViewChild(IonInfiniteScroll) infiniteScroll: IonInfiniteScroll;
  public filmsSeen: any = undefined;
  constructor(private apiRequests: ApiRequestsService) {
    this.initializeFilmsSeen();
  }

  ngOnInit() {}

  initializeFilmsSeen() {
    this.apiRequests.getFilmsSeen().subscribe(async (res: ApiResponse) => {
      this.filmsSeen = res.data;
      console.log(this.filmsSeen);
    });
  }
}

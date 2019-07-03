import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-filmslist',
  templateUrl: './filmslist.page.html',
  styleUrls: ['./filmslist.page.scss']
})
export class FilmslistPage implements OnInit {
  public searchOpen = false;
  public dropDown = false;
  public items: any[] = [
    {
      src:
        'https://gravatar.com/avatar/dba6bae8c566f9d4041fb9cd9ada7741?d=identicon&f=y',
      text:
        'This is content, without any paragraph or header tags, within an ion-card-content element.'
    },
    {
      src:
        'https://gravatar.com/avatar/dba6bae8c566f9d4041fb9cd9ada7741?d=identicon&f=y',
      text:
        'This is content, without any paragraph or header tags, within an ion-card-content element.'
    },
    {
      src:
        'https://gravatar.com/avatar/dba6bae8c566f9d4041fb9cd9ada7741?d=identicon&f=y',
      text:
        'This is content, without any paragraph or header tags, within an ion-card-content element.'
    }
  ];

  public searchMode = false;
  constructor() {}

  ngOnInit() {}
}

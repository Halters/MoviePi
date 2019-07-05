import { ColorsStars } from './../../enums/colors-stars.enum';
import { Component, OnInit, EventEmitter } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-filmdetails',
  templateUrl: './filmdetails.page.html',
  styleUrls: ['./filmdetails.page.scss']
})
export class FilmdetailsPage implements OnInit {
  id = null;
  isChecked = false;
  rating = 5;
  ratingChange: EventEmitter<number>;
  title = 'Ariel';
  image = 'https://image.tmdb.org/t/p/w500/w0NzAc4Lv6euPtPAmsdEf0ZCF8C.jpg';
  releaseDate = '1988-10-21';
  overview =
    'Salla, petite ville minière de la Laponie. Taisto Kasurinen, mineur, hérite d\'une \'belle américaine\' après le suicide de son propriétaire. Il retire toute ses économies de la banque et part à Helsinki. La capitale l\'accueille froidement : il se fait voler son argent et se retrouve en prison. Cependant il a eu le temps de rencontrer Irmeli, jeune femme débordée, et son petit garçon. Ils réussiront a faire évader Taisto. Poursuivis par la police, ils sont bien décidés a tout faire pour s\'en sortir.';

  constructor(private activatedRoute: ActivatedRoute) {}

  ngOnInit() {
    this.id = this.activatedRoute.snapshot.paramMap.get('id');
    console.log(this.id);
  }
  rate(index: number) {
    console.log(index);
  }

  getColor(index: number) {
    if (this.isAboveRating(index)) {
      return ColorsStars.GREY;
    }
    switch (this.rating) {
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

  isAboveRating(index: number): boolean {
    return index > this.rating;
  }
}

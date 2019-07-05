import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  {
    path: 'home',
    loadChildren: './home/home.module#HomePageModule'
  },
  {
    path: 'suggestions',
    loadChildren: './suggestions/suggestions.module#SuggestionsPageModule'
  },
  {
    path: 'preferences',
    loadChildren: './preferences/preferences.module#PreferencesPageModule'
  },
  {
    path: 'filmslist',
    loadChildren: './filmslist/filmslist.module#FilmslistPageModule'
  },
  {
    path: 'filmsseen',
    loadChildren: './filmsseen/filmsseen.module#FilmsseenPageModule'
  },
  {
    path: 'filmdetails/:id',
    loadChildren: './filmdetails/filmdetails.module#FilmdetailsPageModule'
  },
  {
    path: 'filmdetails',
    loadChildren: './filmdetails/filmdetails.module#FilmdetailsPageModule'
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MemberRoutingModule {}

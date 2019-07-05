import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { FilmdetailsPage } from './filmdetails.page';

const routes: Routes = [
  {
    path: '',
    component: FilmdetailsPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [FilmdetailsPage]
})
export class FilmdetailsPageModule {}

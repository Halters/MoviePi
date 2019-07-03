import { Component } from '@angular/core';

import { Platform, MenuController } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { AuthenticationService } from './services/authentication.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html'
})
export class AppComponent {
  appPages = [
    {
      title: 'Fil d\'actualité',
      url: '/members/home',
      icon: 'home'
    },
    {
      title: 'Films vus',
      url: '/members/filmsseen',
      icon: 'eye'
    },
    {
      title: 'Liste des films',
      url: '/members/filmslist',
      icon: 'film'
    },
    {
      title: 'Suggestions',
      url: '/members/suggestions',
      icon: 'bulb'
    }
  ];

  footerLink = {
    title: 'Préférences',
    url: '/members/preferences',
    icon: 'build'
  };

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private authenticationService: AuthenticationService,
    private router: Router,
    private menu: MenuController
  ) {
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();

      this.authenticationService.authenticationState.subscribe(state => {
        if (state) {
          this.router.navigate(['members', 'home']);
        } else {
          this.router.navigate(['login']);
        }
      });
    });
  }

  logout() {
    this.authenticationService.logout();
    this.menu.close('sidebar');
  }

  isLogged() {
    return true;
    return this.authenticationService.isAuthenticated();
  }
}

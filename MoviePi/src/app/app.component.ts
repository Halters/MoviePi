import { Component } from '@angular/core';

import { Platform, MenuController } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { AuthenticationService } from './services/authentication.service';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html'
})
export class AppComponent {
  public appPages = [
    {
      title: 'Home',
      url: '/members/home',
      icon: 'home'
    },
    {
      title: 'Films vus',
      url: 'members/home',
      icon: 'eye'
    },
    {
      title: 'Liste des films',
      url: 'members/home',
      icon: 'film'
    },
    {
      title: 'Suggestions',
      url: '/members/suggestions',
      icon: 'bulb'
    }
  ];

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private authenticationService: AuthenticationService,
    private menu: MenuController
  ) {
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }

  logout() {
    this.authenticationService.logout();
    this.menu.close('sidebar');
  }

  isLogged() {
    return this.authenticationService.isAuthenticated();
  }
}

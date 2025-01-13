import { Component } from '@angular/core';
import { HomePageComponent } from './home-page/home-page.component';
import { HeaderComponent } from "./header/header.component";

@Component({
  selector: 'app-root',
  imports: [HomePageComponent, HeaderComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  title = 'ytSummarizer';
}

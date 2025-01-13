import { Component } from "@angular/core";
import { HttpClient, HttpErrorResponse, HttpResponse } from "@angular/common/http";
import { FormsModule } from "@angular/forms";

@Component({
  selector: "app-home-page",
  imports: [FormsModule],
  templateUrl: "./home-page.component.html",
  styleUrl: "./home-page.component.css",
})
export class HomePageComponent {
  baseUrl = "http://127.0.0.1:5000";
  videoUrl: string = "";
  isValidUrl : boolean = false;
  summary: string | null = null;
  errorMessage: string | null = null;

  constructor(private http: HttpClient) {}

  submitForm(): void {
    // Send GET request with the input text as a query parameter
    this.http
      .post(`${this.baseUrl}`, {videoUrl : this.videoUrl} ,{responseType : 'text' })
      .subscribe({
        next: (data: any) => {
          this.isValidUrl = true
          this.summary = data ;
        },
        error: (err : HttpErrorResponse) => {
          this.isValidUrl = false
          this.errorMessage = err.error
          console.error("Error:", err);
        },
      });
  }
}

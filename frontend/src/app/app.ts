import { DatePipe } from '@angular/common';
import { Component, signal } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { RouterOutlet } from '@angular/router';


@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})


export class App {
  protected readonly title = signal('core-frontend');
}

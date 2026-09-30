import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { MatToolbarModule } from '@angular/material/toolbar';


@Component({
  selector: 'app-auth',
  imports: [RouterOutlet,MatToolbarModule],
  templateUrl: './auth.html',
  styleUrl: './auth.css',
})
export class Auth {

}

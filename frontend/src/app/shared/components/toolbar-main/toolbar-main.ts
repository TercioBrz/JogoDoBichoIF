import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { Auth } from '../../../services/auth';
import { Router } from '@angular/router';


@Component({
  selector: 'app-toolbar-main',
  imports: [  
    MatToolbarModule,
    MatButtonModule,
    MatIconModule],
  templateUrl: './toolbar-main.html',
  styleUrl: './toolbar-main.css',
})
export class ToolbarMain {
  auth = inject(Auth)
  router = inject(Router);

  Username = JSON.parse(localStorage.getItem('user')!);

  logout(){
    this.auth.logout()
    console.log("Ok")
    this.router.navigate(['auth/login']);
  }

  extract(){
    this.router.navigate(['extracts']);
  }

  
}

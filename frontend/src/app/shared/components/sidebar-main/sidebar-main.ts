import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { BetDialogbox } from '../bet-dialogbox/bet-dialogbox';
import { MatDialog } from '@angular/material/dialog';


@Component({
  selector: 'app-sidebar-main',
  imports: [
    MatSidenavModule,
    MatToolbarModule,
    MatButtonModule,

  ],
  templateUrl: './sidebar-main.html',
  styleUrl: './sidebar-main.css',
})
export class SidebarMain {

  private dialog = inject(MatDialog);

  abrirOpcoes() {

      const dialogRef = this.dialog.open(BetDialogbox,{
        width: '550px',
        height: '450x',
        disableClose: true
      });

    }
  }



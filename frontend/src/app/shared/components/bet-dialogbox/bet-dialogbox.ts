import { Component, inject } from '@angular/core';

import { MatButtonModule } from '@angular/material/button';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';

import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { BetDezena } from '../bet-dezena/bet-dezena';
import { BetGrupo } from '../bet-grupo/bet-grupo';


@Component({
  selector: 'app-bet-dialogbox',

  imports: [
    MatDialogModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule
  ],

  templateUrl: './bet-dialogbox.html',
  styleUrl: './bet-dialogbox.css',
})
export class BetDialogbox {

  private dialog = inject(MatDialog);
  

  abrirGrupo() {
    this.dialog.open(BetGrupo,{
      disableClose: true
    });
  }

  abrirDezena() {
    this.dialog.open(BetDezena,{
      disableClose: true
    });
  }

  // abrirCentena() {
  //   this.dialog.open(CentenaDialog);
  // }

  // abrirMilhar() {
  //   this.dialog.open(MilharDialog);
  // }
}
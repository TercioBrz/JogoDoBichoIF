import { Component, inject } from '@angular/core';
import { MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { Bet } from '../../../services/bet';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-bet-grupo',
  imports: [
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule
  ],
  templateUrl: './bet-grupo.html',
  styleUrl: './bet-grupo.css',
})
export class BetGrupo {

  private dialogRef = inject(MatDialogRef<BetGrupo>);
  private bet = inject(Bet);
  private snackBar = inject(MatSnackBar);
  
  apostar(grupo: string| null, valor: string, head: string) {

    const aposta = {
      modalidade: 'grupo',
      grupo: Number(valor),
      valor: Number(valor),
      head: head ? 1 : 0
    };

    console.log("OKKK",aposta)

    this.bet.UserBetPost(aposta).subscribe({
      next: resposta => {

          this.snackBar.open('Aposta Feita! Aguarde...', 'Fechar', {
          duration: 3000
        });

          console.log(resposta);
          this.dialogRef.close(aposta);
      },
      error: erro => {
          console.error(erro);
      }
    });

  }

  cancelar() {
    this.dialogRef.close();
  }

}

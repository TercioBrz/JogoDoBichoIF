import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { Bet } from '../../../services/bet';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-bet-dezena',
  imports: [
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule],

  templateUrl: './bet-dezena.html',
  styleUrl: './bet-dezena.css',
})
export class BetDezena {

  private dialogRef = inject(MatDialogRef<BetDezena>);
  private bet = inject(Bet);
  private snackBar = inject(MatSnackBar);
  
  apostar(dezena: string| null, valor: string, head: string) {

    const aposta = {
      modalidade: 'dezena',
      dezena: Number(valor),
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

}

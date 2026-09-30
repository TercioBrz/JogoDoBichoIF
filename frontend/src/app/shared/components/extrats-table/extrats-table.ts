import { ChangeDetectorRef, Component, inject } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { Bet } from '../../Interfaces/InterfaceExtract';
import { Bet as BetService } from '../../../services/bet';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-extrats-table',
  imports: [MatTableModule,
    MatTableModule,
    DatePipe,
  ],
  templateUrl: './extrats-table.html',
  styleUrl: './extrats-table.css',
})
export class ExtratsTable {

  private bet = inject(BetService);
  private cdr = inject(ChangeDetectorRef);

  displayedColumns = [

    'bet',
    'win',
    'loss',
    'created_at'
  ];

  bets: Bet[] = [];

  ngOnInit() {
    this.bet.UserBetsExtract().subscribe({
      next: resposta => {
        this.bets = resposta.data;

        this.cdr.detectChanges();
      },
      error: erro => {
        console.error(erro);
      }
    });
  }
}
import { Component, input } from '@angular/core';
import { MatCardModule } from '@angular/material/card';



@Component({
  selector: 'app-bet-card',
  imports: [MatCardModule],
  templateUrl: './bet-card.html',
  styleUrl: './bet-card.css',
})
export class BetCard {

  image = input<string>();
  title = input<string>();
  number = input<number>();
  dezenas = input.required<string[]>();

}

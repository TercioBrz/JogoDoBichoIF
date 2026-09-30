import { Component, EventEmitter, Input, Output } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-buttongreen',
  imports: [MatButtonModule],
  templateUrl: './buttongreen.html',
  styleUrl: './buttongreen.css',
})
export class Buttongreen {

  @Input() type: 'button' | 'submit' = 'button';
  @Input() disabled = false;
  @Input() color: 'primary' | 'accent' | 'warn' = 'primary';

  @Output() clicked = new EventEmitter<void>();

  onClick() {
    if (!this.disabled) {
      this.clicked.emit();
    }
  }

}

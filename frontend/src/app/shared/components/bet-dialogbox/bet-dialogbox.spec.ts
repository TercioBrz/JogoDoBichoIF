import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BetDialogbox } from './bet-dialogbox';

describe('BetDialogbox', () => {
  let component: BetDialogbox;
  let fixture: ComponentFixture<BetDialogbox>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BetDialogbox]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BetDialogbox);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

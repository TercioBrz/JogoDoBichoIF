import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BetCard } from './bet-card';

describe('BetCard', () => {
  let component: BetCard;
  let fixture: ComponentFixture<BetCard>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BetCard]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BetCard);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

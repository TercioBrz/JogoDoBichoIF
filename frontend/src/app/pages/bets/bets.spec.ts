import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Bets } from './bets';

describe('Bets', () => {
  let component: Bets;
  let fixture: ComponentFixture<Bets>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Bets]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Bets);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

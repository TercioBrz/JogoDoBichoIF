import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BetDezena } from './bet-dezena';

describe('BetDezena', () => {
  let component: BetDezena;
  let fixture: ComponentFixture<BetDezena>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BetDezena]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BetDezena);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

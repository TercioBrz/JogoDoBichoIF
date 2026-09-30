import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BetGrupo } from './bet-grupo';

describe('BetGrupo', () => {
  let component: BetGrupo;
  let fixture: ComponentFixture<BetGrupo>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BetGrupo]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BetGrupo);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

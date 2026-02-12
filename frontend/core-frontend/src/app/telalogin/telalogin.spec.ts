import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Telalogin } from './telalogin';

describe('Telalogin', () => {
  let component: Telalogin;
  let fixture: ComponentFixture<Telalogin>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Telalogin]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Telalogin);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

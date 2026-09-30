import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Buttongreen } from './buttongreen';

describe('Buttongreen', () => {
  let component: Buttongreen;
  let fixture: ComponentFixture<Buttongreen>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Buttongreen]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Buttongreen);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

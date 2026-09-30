import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Extracts } from './extracts';

describe('Extracts', () => {
  let component: Extracts;
  let fixture: ComponentFixture<Extracts>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Extracts]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Extracts);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

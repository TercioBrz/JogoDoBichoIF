import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExtratsTable } from './extrats-table';

describe('ExtratsTable', () => {
  let component: ExtratsTable;
  let fixture: ComponentFixture<ExtratsTable>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ExtratsTable]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ExtratsTable);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

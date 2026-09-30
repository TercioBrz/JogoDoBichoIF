import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToolbarMain } from './toolbar-main';

describe('ToolbarMain', () => {
  let component: ToolbarMain;
  let fixture: ComponentFixture<ToolbarMain>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ToolbarMain]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ToolbarMain);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

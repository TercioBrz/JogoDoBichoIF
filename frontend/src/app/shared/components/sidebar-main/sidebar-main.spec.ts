import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SidebarMain } from './sidebar-main';

describe('SidebarMain', () => {
  let component: SidebarMain;
  let fixture: ComponentFixture<SidebarMain>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SidebarMain]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SidebarMain);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

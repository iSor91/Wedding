import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProgrowComponent } from './progrow.component';

describe('ProgrowComponent', () => {
  let component: ProgrowComponent;
  let fixture: ComponentFixture<ProgrowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProgrowComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProgrowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

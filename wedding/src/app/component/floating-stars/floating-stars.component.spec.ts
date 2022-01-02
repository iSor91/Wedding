import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FloatingStarsComponent } from './floating-stars.component';

describe('FloatingStarsComponent', () => {
  let component: FloatingStarsComponent;
  let fixture: ComponentFixture<FloatingStarsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FloatingStarsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FloatingStarsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

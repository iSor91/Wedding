import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PreviouslyComponent } from './previously.component';

describe('PreviouslyComponent', () => {
  let component: PreviouslyComponent;
  let fixture: ComponentFixture<PreviouslyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PreviouslyComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PreviouslyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

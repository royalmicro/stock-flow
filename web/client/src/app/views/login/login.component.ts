import { ChangeDetectionStrategy, Component, signal } from '@angular/core';
import { Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';
import { MatIconModule } from '@angular/material/icon';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { AuthState } from '../../store/auth/auth.reducer';
import { Observable } from 'rxjs';
import { Store } from '@ngrx/store';
import * as AuthActions from '../../store/auth/auth.actions';

@Component({
  standalone: true,
  imports: [
    MatCardModule,
    MatButtonModule,
    MatDividerModule,
    MatIconModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatCheckboxModule,
  ],
  template: `
    <mat-card class="card">
      <mat-card-header class="card-header">
        <mat-card-title>Login</mat-card-title>
      </mat-card-header>
      <mat-card-content>
        <div class="button-container">
          <button mat-raised-button class="flat-button">
            <img src="apple.svg" alt="Apple Logo" class="icon" />
          </button>
          <button mat-raised-button class="flat-button">
            <img src="facebook.svg" alt="Facebook Logo" class="icon" />
          </button>
          <button mat-raised-button class="flat-button">
            <img src="google.svg" alt="Google Logo" class="icon" />
          </button>
        </div>
        <div class="horizontal-line">
          <span>or</span>
        </div>

        <form [formGroup]="loginForm" class="login-form">
          <mat-form-field appearance="outline" class="custom-form-field">
            <mat-label>User Name or Email</mat-label>
            <input matInput formControlName="username" />
            <mat-icon matSuffix>email</mat-icon>
          </mat-form-field>

          <mat-form-field appearance="outline" class="custom-form-field">
            <mat-label>Password</mat-label>
            <input
              matInput
              [type]="hide() ? 'password' : 'text'"
              formControlName="password"
            />
            <button
              mat-icon-button
              matSuffix
              (click)="clickEvent($event)"
              [attr.aria-label]="'Hide password'"
              [attr.aria-pressed]="hide()"
            >
              <mat-icon>{{
                hide() ? 'visibility_off' : 'visibility'
              }}</mat-icon>
            </button>
          </mat-form-field>
          <mat-checkbox class="example-margin" formControlName="rememberMe"
            >Remember me</mat-checkbox
          >
        </form>
      </mat-card-content>
      <mat-card-actions class="card-actions">
        <button mat-flat-button class="flat-button" (click)="onLogin()">
          Enviar
        </button>
      </mat-card-actions>
    </mat-card>
  `,
  styleUrl: 'login.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LoginComponent {
  authState$: Observable<AuthState>;
  loginForm = new FormGroup({
    username: new FormControl(''),
    password: new FormControl(''),
    rememberMe: new FormControl(false),
  });
  hide = signal(true);

  constructor(
    private router: Router,
    private store: Store<{ auth: AuthState }>,
  ) {
    this.authState$ = this.store.select('auth');
  }

  navigateToDashboard() {
    this.router.navigate(['/dashboard']);
  }

  clickEvent(event: MouseEvent) {
    this.hide.set(!this.hide());
    event.stopPropagation();
  }

  onLogin(): void {
    const username = this.loginForm.value.username;
    const password = this.loginForm.value.password;

    this.store.dispatch(AuthActions.login({ username, password }));
  }
}

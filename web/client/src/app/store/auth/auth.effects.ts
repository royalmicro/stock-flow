import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { of } from 'rxjs';
import { catchError, map, switchMap } from 'rxjs/operators';

import * as AuthActions from './auth.actions';
import { AuthService } from '../../services/http/auth.service';
import { AppModule } from '../../app.module';
import { Router } from '@angular/router';

@Injectable({ providedIn: AppModule })
export class AuthEffects {
  constructor(
    private actions$: Actions,
    private authService: AuthService,
    private router: Router,
  ) {}

  login$ = createEffect(() =>
    this.actions$.pipe(
      ofType(AuthActions.login),
      switchMap((action) => {
        return this.authService.login(action.username, action.password).pipe(
          map((response) => {
            return AuthActions.loginSuccess({
              token: response.token,
              user: response.user,
            });
          }),
          catchError((error) => of(AuthActions.loginFailure({ error }))),
        );
      }),
    ),
  );

  logout$ = createEffect(() =>
    this.actions$.pipe(
      ofType(AuthActions.logout),
      map(() => {
        this.authService.logout();
        return { type: '[Auth] Logout Success' };
      }),
    ),
  );

  redirectOnLoginSuccess$ = createEffect(
    () =>
      this.actions$.pipe(
        ofType(AuthActions.loginSuccess),
        map(() => {
          this.router.navigate(['/dashboard']);
        }),
      ),
    { dispatch: false },
  );
}

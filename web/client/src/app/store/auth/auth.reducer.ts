import { createReducer, on } from '@ngrx/store';
import * as AuthActions from './auth.actions';

export interface AuthState {
  token: string | null;
  user: any | null;
  error: string | null;
}

export const initialState: AuthState = {
  token: null,
  user: null,
  error: null,
};

export const _authReducer = createReducer(
  initialState,
  on(AuthActions.loginSuccess, (state, { token, user }) => ({
    ...state,
    token,
    user,
    error: null,
  })),
  on(AuthActions.loginFailure, (state, { error }) => ({
    ...state,
    token: null,
    user: null,
    error,
  })),
  on(AuthActions.logout, (state) => ({
    ...state,
    token: null,
    user: null,
    error: null,
  })),
);

export function authReducer(state: AuthState | undefined, action: any) {
  return _authReducer(state, action);
}

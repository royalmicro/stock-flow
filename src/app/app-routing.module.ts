import { Routes } from '@angular/router';

export const routes: Routes = [
    {
      path: '',
      loadComponent: () => import('./views/login/login.component').then(c => c.LoginComponent)
    },
    {
      path: 'dashboard',
      loadComponent: () => import('./views/dashboard/dashboard.component').then(c => c.DashboardComponent)
    }
  ];
  
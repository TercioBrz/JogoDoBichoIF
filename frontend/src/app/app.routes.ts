import { Routes } from '@angular/router';
import { authGuard } from './guards/auth.guard';

export const routes: Routes = [
  {
    path: '',
    canActivate: [authGuard],     
    
    loadComponent: () =>
      import('./layout/main/main').then(m => m.Main),
      children: [
        {
          path: 'home',
          loadComponent: () =>
            import('./pages/home/home').then(m => m.Home),
        },
        {
          path: 'extracts',
          loadComponent: () =>
            import('./pages/extracts/extracts').then(m => m.Extracts),
        },
        {
          path: 'bets',
          loadComponent: () =>
            import('./pages/bets/bets').then(m => m.Bets),
        },
        { path: '', redirectTo: 'home', pathMatch: 'full' },
      ]
  },

  {
    path: 'auth',
    loadComponent: () =>
      import('./layout/auth/auth').then(m => m.Auth),
      children: [
        {
          path: 'login',
          loadComponent: () =>
            import('./pages/login/login').then(m => m.Login),
        },
        {
          path: 'register',
          loadComponent: () =>
            import('./pages/register/register').then(m => m.Register),
        },
        { path: '', redirectTo: 'login', pathMatch: 'full' },
      ],
  },
];
// src/app/guards/auth.guard.ts
import { inject } from '@angular/core';
import { Router, CanActivateFn } from '@angular/router';
import { Auth } from '../services/auth';
import { catchError, map, of } from 'rxjs';

export const authGuard: CanActivateFn = () => {
  const auth = inject(Auth);
  const router = inject(Router);

  if (auth.isAuthenticated()) {
    return true;
  }

  return auth.refresh().pipe(
    map((res) => {
      auth.settoken(res.data.access_token);
      return true;                 
    }),
    
    catchError(() => {
      router.navigate(['/auth/login']); // ❌ cookie inválido → login
      return of(false);
    })
  );
};
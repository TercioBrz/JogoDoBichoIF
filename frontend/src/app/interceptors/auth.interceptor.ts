import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { Router } from '@angular/router';
import { catchError, switchMap, throwError } from 'rxjs';
import { Auth } from '../services/auth';

export const authInterceptor: HttpInterceptorFn = (req, next) => {

  const auth = inject(Auth);
  const router = inject(Router);

  const token = auth.gettoken();

  const authReq = token
    ? req.clone({
        setHeaders: {
          Authorization: `Bearer ${token}`
        },
        withCredentials: true
      })
    : req.clone({
        withCredentials: true
      });

  return next(authReq).pipe(

    catchError(error => {

      if (error.status !== 401) {
        return throwError(() => error);
      }

      return auth.refresh().pipe(

        switchMap(res => {

          const newToken = res.data.access_token;

          console.log('NOVO TOKEN:', newToken);

          auth.settoken(newToken);

          const retryReq = req.clone({
            setHeaders: {
              Authorization: `Bearer ${newToken}`
            },
            withCredentials: true
          });

          return next(retryReq);
        }),

        catchError(error => {

          router.navigate(['/auth/login']);

          return throwError(() => error);
        })
      );
    })
  );
};
import { Component, inject } from '@angular/core';
import { MatSelectModule } from "@angular/material/select";
import { MatInputModule } from "@angular/material/input";
import { MatFormFieldModule } from '@angular/material/form-field';
import {FormBuilder, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Auth } from '../../services/auth';
import { Buttongreen } from '../../shared/components/buttongreen/buttongreen';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-register',
  imports: [MatFormFieldModule, MatInputModule, MatSelectModule, ReactiveFormsModule,Buttongreen,RouterLink],
  templateUrl: './register.html',
  styleUrl: './register.css',
})
export class Register {

  fb = inject(FormBuilder)
  router = inject(Router);
  snackBar = inject(MatSnackBar);
  auth = inject(Auth)


  form = this.fb.group({
  username: ['', [Validators.minLength(3), Validators.required]],
  first_name: ['', [Validators.required]],
  email: ['', [Validators.required, Validators.email]],
  password: ['', [Validators.required, Validators.minLength(8)]]
})


  get username() {
    return this.form.get('username');
  }

  get password() {
    return this.form.get('password');
  }

  get firstname() {
    return this.form.get('first_name');
  }

  get email() {
    return this.form.get('email');
  }

  register = () => {

    const username = this.username?.value;
    const firstname = this.firstname?.value;
    const email = this.email?.value;
    const password = this.password?.value;

    if (!username || !firstname || !email || !password) return

    this.auth.register(username,firstname,email,password).subscribe({
      next: (res) => {
        this.router.navigate(['/auth/login']);
        console.log(res)

        this.snackBar.open("Tudo Certo", 'Fechar', {
          duration: 4000,
          verticalPosition: 'top'

        });

      },
      
      error: (err) => {

        const errors = err.error as Record<string,Record<string,string>>;
        console.log(errors)
        
        const mensagens = Object.values(errors)
        .flatMap(erro  => Object.values(erro))

        console.log(mensagens)
        console.log(10000)
        

        this.snackBar.open(mensagens.join("\n"), 'Fechar', {
          duration: 4000,
          verticalPosition: 'top'
        });
      }
    })

  }

}

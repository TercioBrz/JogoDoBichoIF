import { inject, Component, signal } from '@angular/core';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormBuilder, Validators, ReactiveFormsModule } from '@angular/forms';
import { Auth } from '../../services/auth';
import { Router, RouterLink } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatInputModule } from '@angular/material/input';
import { Buttongreen } from '../../shared/components/buttongreen/buttongreen';
import { LoginResponse } from '../../shared/Interfaces/InterfaceAccessToken';
import {Response} from '../../shared/Interfaces/InterfaceHttpResponse';
@Component({
  selector: 'app-login',
  imports: [MatFormFieldModule, MatSelectModule, ReactiveFormsModule, MatInputModule, Buttongreen, RouterLink], 
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class Login {

  fb = inject(FormBuilder);
  serviceAuth = inject(Auth);
  router = inject(Router);
  snackBar = inject(MatSnackBar);


  form = this.fb.group({
    username: ['', [Validators.required, Validators.minLength(3)]],
    password: ['', [Validators.required, Validators.minLength(8)]]
  });

  get username() {
    return this.form.get('username');
  }

  get password() {
    return this.form.get('password');
  }

  login = () => {

    const username = this.username?.value;
    const password = this.password?.value;

    if (!username || !password) return;

    this.serviceAuth.login(username, password).subscribe({

      next: (res:LoginResponse) => {
        this.serviceAuth.settoken(res.data.access_token)
        this.router.navigate(['/home']);
        console.log("Bem Vindo")

  
      },
      
      error: (err) => {

          const erros = err.error as Record<string, Record<string, string>>;
          console.log(erros)

          let mensagens = Object.values(erros)
            .flatMap(erro => Object.values(erro));
          
          let ans: string[] = []
          
          mensagens.forEach((linha) =>{
            ans.push(...linha)
          })

          console.log(mensagens)

          

        if (err.status === 401) {

          this.snackBar.open('Usuário ou Senha inválidos', 'Fechar', {
            duration: 4000
          });
        
        } else if (err.status === 400){

          this.snackBar.open(ans.join("---"), "Fechar", {
            duration: 4000,
            verticalPosition: 'top'
          });
          
        } else if (err.status === 404) {

          this.snackBar.open('Usuario não Cadastrado', 'Fechar', {
            duration: 4000,
            verticalPosition: 'top'
          });
 
          console.log(err)
          console.log(erros)
        }
      }
    });
  }
}
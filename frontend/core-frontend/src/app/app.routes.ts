import { Routes } from '@angular/router';

export const routes: Routes = [
    
    { 
        path: 'sign_up', 
        loadComponent: () => 
            import("./components/login/login").then(m => m.Login) 
    },

    {
        path: '',
        loadComponent: () =>
            import("./components/home/home").then(m => m.Home)
        // children: [

        //     {
                
        //     }

        // ]
    }
    

];

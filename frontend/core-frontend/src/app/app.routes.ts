import { Routes } from '@angular/router';

export const routes: Routes = [
    
    { 
        path: 'login', 
        loadComponent: () => 
            import("./telalogin/telalogin").then(m => m.Telalogin) 
    },

    {
        path: '',
        loadComponent: () =>
            import("./home/home").then(m => m.Home)
        // children: [

        //     {
                
        //     }

        // ]
    }
    

];

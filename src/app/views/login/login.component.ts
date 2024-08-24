import { Component } from "@angular/core";
import { Router } from "@angular/router";

@Component({
    standalone: true,
    template : `<h1>Login Page</h1> <button type="button" (click)="navigateToDashboard()">Sign in</button>`,
    styleUrl: 'login.component.scss'
})
export class LoginComponent{
    constructor(private router: Router) {}

    navigateToDashboard() {
        this.router.navigate(['/dashboard']);
    }
}
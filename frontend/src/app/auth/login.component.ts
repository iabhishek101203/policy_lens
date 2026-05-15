import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../services/auth.service';

@Component({
  standalone: true,
  imports: [CommonModule, FormsModule],
  selector: 'app-login',
  template: `
    <section class="login-panel">
      <h1>Welcome to Policy Lens</h1>
      <form (ngSubmit)="login()">
        <label>Email</label>
        <input type="email" [(ngModel)]="email" name="email" required />
        <label>Password</label>
        <input type="password" [(ngModel)]="password" name="password" required />
        <button type="submit">Login</button>
      </form>
      <button type="button" (click)="loginWithGoogle()">Continue with Google</button>
    </section>
  `,
  styles: [
    ".login-panel { max-width: 420px; margin: auto; padding: 2rem; background: rgba(15,23,42,0.95); border-radius: 1rem; }",
    "input, button { width: 100%; margin-top: 0.75rem; padding: 0.85rem; border-radius: 0.75rem; border: 1px solid #334155; background: #0f172a; color: #e2e8f0; }",
  ],
})
export class LoginComponent {
  email = '';
  password = '';

  constructor(private auth: AuthService, private router: Router) {}

  async login() {
    const token = await this.auth.loginWithEmail(this.email, this.password);
    localStorage.setItem('policyLensToken', token);
    this.router.navigate(['/dashboard']);
  }

  async loginWithGoogle() {
    const token = await this.auth.loginWithGoogle();
    localStorage.setItem('policyLensToken', token);
    this.router.navigate(['/dashboard']);
  }
}

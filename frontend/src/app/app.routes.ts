import { Routes } from '@angular/router';
import { LoginComponent } from './auth/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { PolicyListComponent } from './policies/policy-list.component';
import { PolicyDetailComponent } from './policies/policy-detail.component';
import { ChatbotComponent } from './chatbot/chatbot.component';
import { AdminPanelComponent } from './admin/admin-panel.component';

export const appRoutes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'dashboard' },
  { path: 'login', component: LoginComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'policies', component: PolicyListComponent },
  { path: 'policy/:id', component: PolicyDetailComponent },
  { path: 'chatbot', component: ChatbotComponent },
  { path: 'admin', component: AdminPanelComponent },
  { path: '**', redirectTo: 'dashboard' },
];

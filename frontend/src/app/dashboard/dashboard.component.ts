import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  imports: [CommonModule],
  selector: 'app-dashboard',
  template: `
    <section class="dashboard-shell">
      <div class="hero-card">
        <h1>Discover government policies with AI</h1>
        <p>Search by category, state, eligibility, or ask the policy assistant.</p>
      </div>
      <div class="overview-grid">
        <article *ngFor="let card of categories" class="category-card">
          <h3>{{ card }}</h3>
        </article>
      </div>
    </section>
  `,
  styles: [
    ".dashboard-shell { display: grid; gap: 1.5rem; }",
    ".hero-card { padding: 2rem; background: #111827; border-radius: 1rem; border: 1px solid rgba(148,163,184,0.12); }",
    ".overview-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px,1fr)); gap: 1rem; }",
    ".category-card { padding: 1rem; background: #0f172a; border-radius: 1rem; border: 1px solid rgba(148,163,184,0.08); }"
  ]
})
export class DashboardComponent {
  categories = [
    'Agriculture', 'Education', 'Finance', 'Healthcare', 'Employment',
    'Women Empowerment', 'Students', 'Startups', 'MSME', 'Housing',
    'Pension', 'Technology', 'Environment'
  ];
}

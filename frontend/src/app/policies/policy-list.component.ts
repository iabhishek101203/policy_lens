import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { PolicyService } from '../services/policy.service';

@Component({
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  selector: 'app-policy-list',
  template: `
    <section class="policy-list">
      <div class="search-bar">
        <input type="text" [(ngModel)]="query" placeholder="Search policies, scholarships, loans..." />
        <button (click)="search()">Search</button>
      </div>
      <div class="policy-grid">
        <article *ngFor="let policy of policies" class="policy-card">
          <h3>{{ policy.title }}</h3>
          <p>{{ policy.summary || policy.benefits }}</p>
          <a [routerLink]="['/policy', policy._id]">View details</a>
        </article>
      </div>
    </section>
  `,
  styles: [
    ".policy-list { display: grid; gap: 1rem; }",
    ".search-bar { display: flex; gap: 0.75rem; }",
    ".policy-card { padding: 1rem; background: #0f172a; border-radius: 0.85rem; }",
    "input { flex: 1; padding: 0.85rem; border-radius: 0.75rem; background: #111827; border: 1px solid #334155; color: #e2e8f0; }"
  ]
})
export class PolicyListComponent implements OnInit {
  query = '';
  policies: any[] = [];

  constructor(private policyService: PolicyService) {}

  ngOnInit() {
    this.search();
  }

  search() {
    this.policyService.search({ query: this.query }).subscribe(result => {
      this.policies = result.results || [];
    });
  }
}

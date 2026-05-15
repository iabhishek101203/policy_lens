import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  imports: [CommonModule],
  selector: 'app-admin-panel',
  template: `
    <section class="admin-panel">
      <h2>Admin Control Center</h2>
      <p>Use this panel to manage scraped policies, trigger ingestion, and review analytics.</p>
      <div class="actions">
        <button>Run Scraper</button>
        <button>Approve Policies</button>
      </div>
      <div class="admin-grid">
        <div class="admin-card">Policy approvals</div>
        <div class="admin-card">Scraper status</div>
        <div class="admin-card">Category management</div>
      </div>
    </section>
  `,
  styles: [
    ".admin-panel { display: grid; gap: 1rem; padding: 1.5rem; background: #111827; border-radius: 1rem; }",
    ".actions { display: flex; gap: 1rem; }",
    "button { padding: 0.8rem 1rem; border-radius: 0.85rem; border: none; background: #2563eb; color: white; }",
    ".admin-grid { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }",
    ".admin-card { padding: 1rem; background: #0f172a; border-radius: 1rem; }"
  ]
})
export class AdminPanelComponent {}

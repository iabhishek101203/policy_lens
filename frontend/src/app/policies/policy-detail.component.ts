import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { PolicyService } from '../services/policy.service';

@Component({
  standalone: true,
  imports: [CommonModule],
  selector: 'app-policy-detail',
  template: `
    <section *ngIf="policy" class="policy-detail">
      <h1>{{ policy.title }}</h1>
      <p class="meta">{{ policy.ministry }} • {{ policy.category }}</p>
      <div class="summary">{{ policy.summary || policy.benefits }}</div>
      <div class="section"><strong>Eligibility:</strong> {{ policy.eligibility }}</div>
      <div class="section"><strong>Benefits:</strong> {{ policy.benefits }}</div>
      <div class="section"><strong>Required Documents:</strong> {{ policy.required_documents }}</div>
      <div class="section"><strong>Application Process:</strong> {{ policy.application_process }}</div>
      <div class="section"><strong>Deadline:</strong> {{ policy.deadline || 'Ongoing' }}</div>
      <a [href]="policy.official_link" target="_blank">Official policy link</a>
    </section>
  `,
  styles: [
    ".policy-detail { padding: 1.5rem; background: #111827; border-radius: 1rem; }",
    ".meta { color: #94a3b8; margin-bottom: 1rem; }",
    ".section { margin-top: 1rem; }",
    "a { color: #7dd3fc; text-decoration: none; }"
  ]
})
export class PolicyDetailComponent implements OnInit {
  policy: any;

  constructor(private route: ActivatedRoute, private policyService: PolicyService) {}

  ngOnInit() {
    const id = this.route.snapshot.params['id'];
    this.policyService.getPolicy(id).subscribe(result => {
      this.policy = result.policy;
    });
  }
}

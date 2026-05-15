import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  imports: [CommonModule, FormsModule],
  selector: 'app-chatbot',
  template: `
    <section class="chatbot-shell">
      <h2>AI Policy Assistant</h2>
      <p>Ask policy-related questions or request simplified summaries.</p>
      <textarea [(ngModel)]="prompt" placeholder="Ask about scholarships, loans, eligibility, or state schemes"></textarea>
      <button (click)="askAssistant()">Ask Policy Lens</button>
      <div *ngIf="response" class="assistant-response">
        <h3>Answer</h3>
        <p>{{ response }}</p>
      </div>
    </section>
  `,
  styles: [
    ".chatbot-shell { display: grid; gap: 1rem; padding: 1.5rem; background: #111827; border-radius: 1rem; }",
    "textarea { width: 100%; min-height: 140px; padding: 1rem; border-radius: 0.9rem; border: 1px solid #334155; background: #0f172a; color: #e2e8f0; }",
    "button { width: 160px; padding: 0.85rem; border-radius: 0.85rem; background: #0284c7; border: none; color: white; }",
    ".assistant-response { padding: 1rem; background: #0f172a; border-radius: 0.9rem; border: 1px solid #334155; }"
  ]
})
export class ChatbotComponent {
  prompt = '';
  response = '';

  askAssistant() {
    this.response = 'This feature is coming online with the RAG assistant service.';
  }
}

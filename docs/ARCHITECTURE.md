# Policy Lens Architecture

## Overview

Policy Lens is a full-stack AI-powered platform for discovering, searching, and understanding government policies.

## Frontend

- Angular standalone components
- PrimeNG UI patterns
- Firebase Authentication for Email/Password and Google Sign-In
- Pages:
  - Login
  - Dashboard
  - Policy search and list
  - Policy detail
  - AI chatbot assistant
  - Admin panel

## Backend

- FastAPI REST API
- MongoDB for policy storage and user profiles
- Firebase Admin for ID token verification
- Scraper service using BeautifulSoup and Selenium
- RAG service using ChromaDB + OpenAI embeddings
- Recommendation service for personalized policy suggestions

## Database Schema

### policies collection

- title: string
- ministry: string
- category: string
- state_applicability: array[string]
- eligibility: string
- benefits: string
- required_documents: string
- application_process: string
- deadline: string
- official_link: string
- target_audience: string
- summary: string
- tags: array[string]
- source: string
- faqs: array[string]
- published_date: date

### users collection

- uid: string
- email: string
- name: string
- profile: object
- preferences: object
- history: array[object]

## API Design

### Auth

- POST /api/auth/verify
- GET /api/auth/me

### Policies

- POST /api/policies/search
- GET /api/policies/{policy_id}
- POST /api/policies/suggestions

### Admin

- POST /api/admin/scrape
- GET /api/admin/policies
- DELETE /api/admin/policies/{policy_id}

## RAG Flow

1. Collect policy text and metadata through scraper service.
2. Build a unified document per policy.
3. Generate embeddings with OpenAI.
4. Store embeddings in ChromaDB.
5. Query embeddings for natural language search.
6. Return relevance-ranked policies and AI summaries.

## Deployment Plan

1. Provision MongoDB and Firebase project.
2. Configure `backend/.env` with secrets.
3. Install Python and Node dependencies.
4. Run backend: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
5. Run frontend: `npm install && npm start` in `frontend`.
6. Connect Firebase Auth and verify tokens in backend.
7. Add production build and containerization as next step.

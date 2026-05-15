# Policy Lens

Policy Lens is a full-stack AI-powered platform for discovering, searching, and understanding government policies in one centralized system.

## Project Structure

- `frontend/` — Angular standalone frontend with PrimeNG and Firebase Authentication scaffolding.
- `backend/` — FastAPI backend, MongoDB integration, Firebase token verification, scraper service, and RAG service.
- `docs/ARCHITECTURE.md` — Architecture overview, database schema, API design, and deployment guidance.

## Tech Stack

- Frontend: Angular (standalone components), PrimeNG, Firebase Authentication
- Backend: FastAPI, Python, MongoDB, Firebase Admin SDK
- AI: OpenAI embeddings, ChromaDB, LangChain-compatible skeleton
- Scraping: BeautifulSoup, Selenium

## Setup

### Backend

1. Copy `backend/.env.sample` to `backend/.env`.
2. Install dependencies:
   - `python -m pip install -r backend/requirements.txt`
3. Run the API:
   - `cd backend`
   - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

### Frontend

1. Install dependencies:
   - `cd frontend`
   - `npm install`
2. Start the Angular app:
   - `npm start`

## Notes

- The app scaffold includes core modules for authentication, policy search, policy detail pages, admin management, and an AI assistant interface.
- The backend includes a RAG service and scraper service skeleton ready for policy ingestion.
- Replace Firebase config values and environment secrets before production.

## Next Steps

- Add actual government policy target URLs to `backend/app/services/scraper.py`.
- Implement vector ingestion and prompt chaining in `backend/app/services/rag.py`.
- Add frontend route guards and token management for protected routes.
- Build out admin actions and analytics dashboards.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, policies, admin
from app.core.config import settings
from app.services.mongo_client import init_mongo
from app.services.scheduler import SchedulerService

app = FastAPI(
    title="Policy Lens API",
    description="Backend API for Policy Lens intelligent policy discovery and RAG search.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(policies.router, prefix="/api/policies", tags=["policies"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])


@app.on_event("startup")
async def startup_event():
    await init_mongo()
    scheduler = SchedulerService()
    scheduler.start()


@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "Policy Lens API"}

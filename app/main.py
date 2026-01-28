from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Production-ready FastAPI REST API with JWT authentication, PostgreSQL, and Docker",
    version="1.0.0",
)

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "env": settings.env,
    }

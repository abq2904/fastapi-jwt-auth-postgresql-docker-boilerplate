from fastapi import FastAPI

app = FastAPI(
    title="FastAPI JWT Auth Boilerplate",
    description="Production-ready FastAPI REST API with JWT authentication, PostgreSQL, and Docker",
    version="1.0.0",
)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

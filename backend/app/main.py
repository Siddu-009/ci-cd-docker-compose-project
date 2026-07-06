from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CI/CD Demo API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to CI/CD Docker Compose Project"
    }


@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "Backend API",
        "time": datetime.now()
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0",
        "environment": "Development"
    }
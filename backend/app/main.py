from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables when the application starts
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="CI/CD Demo API",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
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
        "time": datetime.now().isoformat()
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0",
        "environment": "Development"
    }
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
models.Base.metadata.create_all(bind=engine)
from routers import auth, courses, progress, quiz
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="TechLearn API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://techlearn-frontend-five.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/seed-db-now-xk9q2m")
def seed_db():
    try:
        from data.seed import seed
        seed()
        return {"status": "seeded"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(progress.router)
app.include_router(quiz.router)

@app.get("/")
def root():
    return {"message": "TechLearn API running"}
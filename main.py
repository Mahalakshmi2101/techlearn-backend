from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import auth, courses, progress, quiz
from dotenv import load_dotenv
from data.seed import seed
load_dotenv()
models.Base.metadata.create_all(bind=engine)

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

@app.get("/seed-db-now")
def seed_database():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from data.seed import seed
    seed()
    return {"status": "seeded"}

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(progress.router)
app.include_router(quiz.router)

@app.get("/")
def root():
    return {"message": "TechLearn API running"}


@app.get("/seed-db-now")
def seed_db():
    try:
        seed()
        return {"status": "seeded"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import auth, courses, progress, quiz

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TechLearn API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(progress.router)
app.include_router(quiz.router)

@app.get("/")
def root():
    return {"message": "TechLearn API running"}
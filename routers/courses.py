from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from auth import get_current_user
import models, schemas

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/", response_model=List[schemas.CourseOut])
def get_courses(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Course).all()

@router.get("/{course_id}", response_model=schemas.CourseDetailOut)
def get_course(course_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.get("/{course_id}/quiz", response_model=schemas.QuizOut)
def get_quiz(course_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    quiz = db.query(models.Quiz).filter(models.Quiz.course_id == course_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found for this course")
    return quiz
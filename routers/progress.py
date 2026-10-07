from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from auth import get_current_user
import models, schemas

router = APIRouter(prefix="/progress", tags=["Progress"])

def get_or_create_progress(user_id: int, course_id: int, db: Session):
    progress = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == user_id,
        models.UserProgress.course_id == course_id
    ).first()

    if not progress:
        total = db.query(models.Lesson).filter(models.Lesson.course_id == course_id).count()
        progress = models.UserProgress(
            user_id=user_id,
            course_id=course_id,
            total_lessons=total
        )
        db.add(progress)
        db.commit()
        db.refresh(progress)

    return progress

@router.get("/", response_model=List[schemas.ProgressOut])
def get_all_progress(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.UserProgress).filter(models.UserProgress.user_id == current_user.id).all()

@router.get("/{course_id}", response_model=schemas.ProgressOut)
def get_course_progress(course_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    progress = get_or_create_progress(current_user.id, course_id, db)
    return progress

@router.post("/{course_id}/complete-lesson", response_model=schemas.ProgressOut)
def complete_lesson(course_id: int, body: schemas.MarkLessonRequest, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    lesson = db.query(models.Lesson).filter(
        models.Lesson.id == body.lesson_id,
        models.Lesson.course_id == course_id
    ).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found in this course")

    progress = get_or_create_progress(current_user.id, course_id, db)

    already_done = db.query(models.LessonCompletion).filter(
        models.LessonCompletion.progress_id == progress.id,
        models.LessonCompletion.lesson_id == body.lesson_id
    ).first()

    if not already_done:
        completion = models.LessonCompletion(progress_id=progress.id, lesson_id=body.lesson_id)
        db.add(completion)
        progress.completed_lessons += 1
        progress.percentage = (progress.completed_lessons / progress.total_lessons) * 100
        if progress.completed_lessons >= progress.total_lessons:
            progress.is_completed = True
        db.commit()
        db.refresh(progress)

    return progress

@router.delete("/{course_id}/uncomplete-lesson", response_model=schemas.ProgressOut)
def uncomplete_lesson(course_id: int, body: schemas.MarkLessonRequest, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    progress = get_or_create_progress(current_user.id, course_id, db)

    completion = db.query(models.LessonCompletion).filter(
        models.LessonCompletion.progress_id == progress.id,
        models.LessonCompletion.lesson_id == body.lesson_id
    ).first()

    if completion:
        db.delete(completion)
        progress.completed_lessons = max(0, progress.completed_lessons - 1)
        progress.percentage = (progress.completed_lessons / progress.total_lessons) * 100 if progress.total_lessons > 0 else 0
        progress.is_completed = False
        db.commit()
        db.refresh(progress)

    return progress
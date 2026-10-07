from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from auth import get_current_user
import models, schemas

router = APIRouter(prefix="/quiz", tags=["Quiz"])

@router.post("/submit", response_model=schemas.QuizResultOut)
def submit_quiz(result: schemas.QuizResultIn, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    quiz = db.query(models.Quiz).filter(models.Quiz.id == result.quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    percentage = (result.score / result.total) * 100 if result.total > 0 else 0

    db_result = models.QuizResult(
        user_id=current_user.id,
        quiz_id=result.quiz_id,
        score=result.score,
        total=result.total,
        percentage=percentage,
        time_taken=result.time_taken
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

@router.get("/results", response_model=List[schemas.QuizResultOut])
def get_my_results(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.QuizResult).filter(models.QuizResult.user_id == current_user.id).all()

@router.post("/check-answer")
def check_answer(body: schemas.QuizAnswerCheck, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    question = db.query(models.Question).filter(models.Question.id == body.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    is_correct = question.correct_option == body.selected_option
    return {
        "is_correct": is_correct,
        "correct_option": question.correct_option,
        "explanation": question.explanation
    }
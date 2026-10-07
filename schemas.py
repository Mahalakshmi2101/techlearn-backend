from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


# Auth
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None


# Lessons
class LessonOut(BaseModel):
    id: int
    title: str
    content: str
    order: int
    duration: str
    class Config:
        from_attributes = True


# Questions
class QuestionOut(BaseModel):
    id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    class Config:
        from_attributes = True

class QuestionWithAnswer(QuestionOut):
    correct_option: str
    explanation: str


# Quiz
class QuizOut(BaseModel):
    id: int
    title: str
    time_limit: int
    questions: List[QuestionOut]
    class Config:
        from_attributes = True


# Courses
class CourseOut(BaseModel):
    id: int
    title: str
    description: str
    category: str
    difficulty: str
    thumbnail: str
    duration: str
    instructor: str
    class Config:
        from_attributes = True

class CourseDetailOut(CourseOut):
    lessons: List[LessonOut]


# Progress
class ProgressOut(BaseModel):
    course_id: int
    completed_lessons: int
    total_lessons: int
    percentage: float
    is_completed: bool
    class Config:
        from_attributes = True

class MarkLessonRequest(BaseModel):
    lesson_id: int


# Quiz Result
class QuizResultIn(BaseModel):
    quiz_id: int
    score: int
    total: int
    time_taken: int

class QuizResultOut(BaseModel):
    id: int
    quiz_id: int
    score: int
    total: int
    percentage: float
    time_taken: int
    attempted_at: datetime
    class Config:
        from_attributes = True

class QuizAnswerCheck(BaseModel):
    question_id: int
    selected_option: str
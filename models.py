from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    progress = relationship("UserProgress", back_populates="user")
    quiz_results = relationship("QuizResult", back_populates="user")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    category = Column(String)
    difficulty = Column(String)  # Beginner, Intermediate, Advanced
    thumbnail = Column(String)
    duration = Column(String)  # e.g. "4 hours"
    instructor = Column(String)

    lessons = relationship("Lesson", back_populates="course")
    quiz = relationship("Quiz", back_populates="course", uselist=False)
    progress = relationship("UserProgress", back_populates="course")


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String)
    content = Column(Text)
    order = Column(Integer)
    duration = Column(String)

    course = relationship("Course", back_populates="lessons")
    completions = relationship("LessonCompletion", back_populates="lesson")


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String)
    time_limit = Column(Integer)  # seconds

    course = relationship("Course", back_populates="quiz")
    questions = relationship("Question", back_populates="quiz")
    results = relationship("QuizResult", back_populates="quiz")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    text = Column(Text)
    option_a = Column(String)
    option_b = Column(String)
    option_c = Column(String)
    option_d = Column(String)
    correct_option = Column(String)  # "a", "b", "c", "d"
    explanation = Column(Text)

    quiz = relationship("Quiz", back_populates="questions")


class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    completed_lessons = Column(Integer, default=0)
    total_lessons = Column(Integer, default=0)
    percentage = Column(Float, default=0.0)
    is_completed = Column(Boolean, default=False)
    last_accessed = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="progress")
    course = relationship("Course", back_populates="progress")
    lesson_completions = relationship("LessonCompletion", back_populates="progress")


class LessonCompletion(Base):
    __tablename__ = "lesson_completions"

    id = Column(Integer, primary_key=True, index=True)
    progress_id = Column(Integer, ForeignKey("user_progress.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    completed_at = Column(DateTime(timezone=True), server_default=func.now())

    progress = relationship("UserProgress", back_populates="lesson_completions")
    lesson = relationship("Lesson", back_populates="completions")


class QuizResult(Base):
    __tablename__ = "quiz_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Integer)
    total = Column(Integer)
    percentage = Column(Float)
    time_taken = Column(Integer)  # seconds
    attempted_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="quiz_results")
    quiz = relationship("Quiz", back_populates="results")
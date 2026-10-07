🚀 TechLearn --- Backend

A FastAPI-powered backend providing authentication, courses,
progress tracking, quizzes, and AI-assisted learning services for the
TechLearn platform.

This repository contains the backend API of TechLearn.

The backend is responsible for application logic, authentication,
database operations, learning-progress management, quiz functionality,
and communication with AI services.

✨ Highlights

⚡ FastAPI REST API

🔐 JWT-based authentication

🔑 Secure password hashing

👤 User registration and login

📚 Course management

📖 Lesson/content delivery

📊 Learning-progress tracking

🧠 Quiz functionality

🤖 AI assistant integration

🗄️ SQLAlchemy database layer

📦 Pydantic request/response validation

🌱 Database seeding

🔒 Environment-based configuration

🧩 Modular router architecture

🚀 Production-ready ASGI deployment with Uvicorn

🏗️ Backend Architecture

techlearn-backend/
│
├── data/
│   └── seed.py
│
├── routers/
│   ├── __init__.py
│   ├── ai.py
│   ├── auth.py
│   ├── courses.py
│   ├── progress.py
│   └── quiz.py
│
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── main.py
├── requirements.txt
├── .env
└── README.md

🧩 Core Modules

Module                  Responsibility

database.py           Database engine, session and database configuration
models.py             SQLAlchemy database models
schemas.py            Pydantic request/response schemas
auth.py               Authentication and JWT-related utilities
main.py               FastAPI application entry point
routers/auth.py       Registration and login endpoints
routers/courses.py    Course-related API operations
routers/progress.py   Learning-progress operations
routers/quiz.py       Quiz-related functionality
routers/ai.py         AI assistant endpoints
data/seed.py          Initial database/course data

🔐 Authentication Architecture

TechLearn uses token-based authentication.

┌──────────────┐
│    Client    │
└──────┬───────┘
       │
       │ username + password
       ▼
┌──────────────┐
│ Auth Router  │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ Verify User      │
│ + Password Hash  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Create JWT Token │
└────────┬─────────┘
         │
         ▼
      Client
         │
         │ Bearer Token
         ▼
┌──────────────────┐
│ Protected Routes │
└──────────────────┘

Passwords are not intended to be stored as plain text. Password
verification is handled through the configured password-hashing
mechanism.

🗄️ Database Layer

The backend uses:

SQLAlchemy for ORM/database interaction

Pydantic for data validation

Environment variables for database configuration

The database configuration is centralized in:

database.py

This separation allows the application to use different database
configurations for local development and production.

🌱 Database Seeding

Initial application data can be inserted using:

python data/seed.py

A successful seed operation should report:

Database seeded successfully.

Seeding is useful for preparing a development environment with initial
users, courses, lessons, quizzes, or other required application data.

Avoid running destructive seed logic against a production database
unless the seed script is explicitly designed for production use.

🔌 API Modules

🔐 Authentication

The authentication router handles operations such as:

User registration

User login

Authentication-related validation

📚 Courses

The course router provides the frontend with learning content and course
information.

📊 Progress

The progress router manages learner progress so the frontend can display
a personalized learning state.

🧠 Quiz

The quiz router handles quiz-related data and learner interactions.

🤖 AI Assistant

The AI router provides the API layer used by the TechLearn learning
assistant.

AI credentials should be supplied through environment variables rather
than committed to source control.

🛠️ Tech Stack

Technology                  Purpose

Python                      Backend language
FastAPI                     REST API framework
Uvicorn                     ASGI server
SQLAlchemy                  ORM/database layer
Pydantic                    Data validation
Python-Jose                 JWT handling
Passlib + bcrypt            Password hashing
python-dotenv               Environment configuration
Python Multipart            Form/request handling
Render / similar platform   Backend deployment

📦 Installation

1. Clone the repository

git clone <your-repository-url>
cd techlearn-backend

2. Create a virtual environment

Windows PowerShell:

python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1

If PowerShell execution policy prevents activation:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Then activate again:

.\venv\Scripts\Activate.ps1

📥 Install Dependencies

pip install -r requirements.txt

🔐 Environment Variables

Create a .env file in the backend root.

Example structure:

DATABASE_URL=your_database_connection_string
SECRET_KEY=your_secret_key
AI_API_KEY=your_ai_api_key

Use your actual values locally or through the deployment platform's
environment-variable settings.

⚠️ Important

Never commit secrets such as:

Database passwords

JWT secret keys

AI API keys

Production credentials

Add .env to .gitignore.

🌱 Initialize the Database

After configuring the environment:

python data/seed.py

▶️ Run Locally

Start the FastAPI application with:

uvicorn main:app --reload

The API will normally be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

Alternative documentation:

http://127.0.0.1:8000/redoc

The correct Uvicorn syntax is main:app, not main:py.

🔄 Development Flow

Frontend
   │
   │ HTTP / JSON
   ▼
FastAPI
   │
   ├── Authentication
   │
   ├── Courses
   │
   ├── Progress
   │
   ├── Quiz
   │
   └── AI Assistant
   │
   ▼
SQLAlchemy
   │
   ▼
Database

🚀 Production Deployment

A typical deployment architecture is:

                ┌─────────────────────┐
                │       Vercel        │
                │  React Frontend     │
                └──────────┬──────────┘
                           │
                           │ HTTPS / REST API
                           ▼
                ┌─────────────────────┐
                │       Backend       │
                │ FastAPI + Uvicorn   │
                └──────────┬──────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       ┌──────────────┐          ┌──────────────┐
       │   Database   │          │  AI Service  │
       └──────────────┘          └──────────────┘

For production deployment:

Push the backend repository to GitHub.

Create a backend web service on the chosen hosting platform.

Configure environment variables.

Install dependencies from requirements.txt.

Start the application with the appropriate Uvicorn command.

Configure the frontend to use the deployed backend URL.

Verify authentication, courses, progress, quizzes, and AI
functionality.

🧪 API Documentation

FastAPI automatically provides interactive documentation.

Once the server is running:

Swagger UI

/docs

ReDoc

/redoc

These interfaces are useful for testing API endpoints independently of
the React frontend.

🛡️ Security Practices

TechLearn follows several important backend security principles:

Passwords are hashed rather than stored as plain text.

JWT tokens are used for authenticated API access.

Sensitive configuration is stored in environment variables.

Request data is validated using Pydantic schemas.

Protected resources require authentication.

Secrets should never be committed to Git.

🧯 Common Development Issues

Uvicorn error

Incorrect:

uvicorn main:py --reload

Correct:

uvicorn main:app --reload

The value after : must refer to the FastAPI application object inside
main.py.

Authentication returns 401 Unauthorized

Check:

The user exists in the database.

The production database is the expected database.

The password matches the stored password hash.

The frontend is calling the correct backend URL.

Production environment variables are configured correctly.

Database connection errors

Check:

DATABASE_URL

and verify that the deployed service can reach the configured database.

🔮 Future Enhancements

Potential backend improvements include:

🔔 Notification service

🏆 Achievement and badge system

📈 Detailed learning analytics

🔎 Search and filtering APIs

🧑‍🏫 Instructor/admin roles

📝 More advanced assessment types

📚 Personalized course recommendations

⚡ Caching for frequently accessed content

🧪 Automated unit and integration testing

🐳 Docker-based deployment

📊 Administrative analytics APIs

🎯 Project Vision

TechLearn is designed around a simple idea:

Learning should be active, measurable, and personalized --- not just
a sequence of static pages.

The backend provides the foundation for that experience by connecting
authentication, learning content, progress, assessments, and AI
assistance through a single API.

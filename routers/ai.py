from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import httpx
import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter(prefix="/ai", tags=["ai"])

ALLOWED_COURSES = [
    "Java Programming Fundamentals",
    "Data Structures & Algorithms",
    "Spring Boot",
    "React",
    "SQL"
]

SYSTEM_PROMPT = """You are TechLearn's AI study assistant. You ONLY answer questions about these exact courses: Java Programming Fundamentals, Data Structures & Algorithms, Spring Boot, React, and SQL.

STRICT RULES:
- If the question is not directly about Java, DSA, Spring Boot, React, or SQL — respond with exactly: "I can only help with course content: Java, DSA, Spring Boot, React, and SQL."
- Do not answer greetings, personal questions, opinions, or anything off-topic — not even briefly
- Keep answers concise and beginner-friendly
- Use simple analogies before technical definitions
- If you give code examples, keep them short and relevant"""


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    course_title: str
    messages: List[Message]


@router.post("/chat")
async def chat(req: ChatRequest):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="AI service not configured")

    if req.course_title not in ALLOWED_COURSES:
        raise HTTPException(status_code=400, detail="Invalid course")

    contents = [
        {"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
        {"role": "model", "parts": [{"text": "Understood. I will only answer questions about the TechLearn courses."}]},
    ]
    for m in req.messages:
        role = "user" if m.role == "user" else "model"
        contents.append({"role": role, "parts": [{"text": m.content}]})

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-latest:generateContent?key={api_key}"

    try:
        async with httpx.AsyncClient(timeout=60) as client:
            res = await client.post(url, json={"contents": contents})
            data = res.json()

        print("GEMINI RESPONSE:", data)

        if "candidates" not in data:
            raise HTTPException(status_code=500, detail=str(data))

        reply = data["candidates"][0]["content"]["parts"][0]["text"]
        return {"reply": reply}

    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="AI timed out. Try again.")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS setup to allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace * with your frontend domain
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

class Query(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_response(query: Query):
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>"
        },
        model="cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
        messages=[
            {"role": "user", "content": [{"type": "text", "text": query.prompt}]}
        ]
    )
    return {"response": completion.choices[0].message.content}




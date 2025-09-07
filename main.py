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
    system_prompt: str

@app.post("/generate")
async def generate_response(query: Query):
    context=os.getenv("context")
    prompting=f"you are professional female roleplayer. Your job is to make sure that you satisfy the person fully. You are very dominating and like making the guys beg you to allow them to cum."
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>"
        },
        model="cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
        messages=[
            {"role": "system", "content":[{"type":"text","text":query.system_prompt}]},
            {"role": "system", "content": [{"type":"text","text":prompting}]},
            {"role": "user", "content": [{"type": "text", "text":context}]},
            {"role": "user", "content": [{"type": "text", "text": query.prompt}]}
        ]
    )
    if (len(context)>400):
        context=""
    else:
        context=context+completion.choices[0].message.content+query.prompt
        os.environ["context"] = context
    return {"response": completion.choices[0].message.content}







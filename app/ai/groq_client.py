import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_ai_response(messages: list) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
    )

    return response.choices[0].message.content


def stream_ai_response(messages: list):
    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        stream=True,
    )

    for chunk in stream:
        if (
            chunk.choices
            and chunk.choices[0].delta.content
        ):
            yield chunk.choices[0].delta.content
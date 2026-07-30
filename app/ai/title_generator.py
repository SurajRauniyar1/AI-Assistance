from app.ai.groq_client import get_ai_response


def generate_chat_title(message: str) -> str:
    prompt = [
        {
            "role": "system",
            "content": (
                "Generate a short chat title (maximum 5 words). "
                "Return ONLY the title. "
                "Do not use quotes or punctuation."
            ),
        },
        {
            "role": "user",
            "content": message,
        },
    ]

    title = get_ai_response(prompt)

    return title.strip()
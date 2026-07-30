from app.ai.groq_client import get_ai_response

reply = get_ai_response("Introduce yourself in one sentence.")

print(reply)
from app.ai.retriever import get_context

context = get_context(
    "What projects are mentioned in the resume?"
)

print(context)
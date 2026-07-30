from app.ai.embeddings import create_embeddings

embeddings = create_embeddings(
    [
        "FastAPI is awesome.",
        "Python is easy."
    ]
)

print(len(embeddings))
print(len(embeddings[0]))
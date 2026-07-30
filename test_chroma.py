from app.ai.vector_store import add_chunks, search
from app.ai.embeddings import create_embeddings

chunks = [
    "FastAPI is a Python framework.",
    "PostgreSQL is a relational database.",
    "Docker containers package applications."
]

embeddings = create_embeddings(chunks)

add_chunks(
    chunks,
    embeddings,
    document_id=1
)

query = create_embeddings(
    ["What is FastAPI?"]
)[0]

results = search(query)

print(results["documents"][0])
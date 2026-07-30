from app.ai.embeddings import model
from app.ai.vector_store import retrieve_chunks

def get_context(query: str):
    chunks = retrieve_chunks(
        query=query,
        embedding_model=model
    )

    unique_chunks = list(dict.fromkeys(chunks))

    print("\n========== RETRIEVED CONTEXT ==========\n")
    for i, chunk in enumerate(unique_chunks):
        print(f"Chunk {i+1}:\n{chunk}\n")
    print("======================================\n")

    return "\n\n".join(unique_chunks)
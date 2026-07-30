import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="documents"
)


def add_chunks(chunks, embeddings, document_id):
    ids = []

    metadatas = []

    for i in range(len(chunks)):
        ids.append(f"{document_id}_{i}")

        metadatas.append(
            {
                "document_id": document_id,
                "chunk": i
            }
        )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search(query_embedding, top_k=5):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results

def retrieve_chunks(query: str, embedding_model, top_k: int = 5):
    """
    Search the vector database using a query.
    """

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]
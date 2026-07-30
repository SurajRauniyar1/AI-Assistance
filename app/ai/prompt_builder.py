from app.models.message import Message


def build_messages(chat_messages, context=""):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI Developer Assistant.\n\n"
                "Use the provided document context whenever it is relevant.\n"
                "If the answer is not contained in the context, clearly say so and "
                "then answer using your general knowledge.\n\n"
                f"Document Context:\n{context}"
            )
        }
    ]

    for msg in chat_messages:
        messages.append(
            {
                "role": msg.role,
                "content": msg.content
            }
        )

    return messages
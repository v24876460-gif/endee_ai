def generate_answer(question, retrieved_docs):

    context = "\n".join([doc for doc,score in retrieved_docs])

    answer = f"""
Question: {question}

Answer:
Based on the retrieved context, the following information was found.

Context:
{context}
"""

    return answer
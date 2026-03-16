import streamlit as st
from document_loader import load_pdf
from chunking import chunk_text
from rag_pipeline import index_chunks, retrieve
from llm_engine import generate_answer
from chat_memory import add, history

st.title("Endee AI Knowledge Copilot")

uploaded_files = st.file_uploader(
    "Upload PDFs",
    accept_multiple_files=True
)

if uploaded_files:

    for file in uploaded_files:

        text = load_pdf(file)

        chunks = chunk_text(text)

        index_chunks(chunks)

    st.success("Documents indexed successfully!")


question = st.text_input("Ask a question")

if question:

    add("user",question)

    retrieved = retrieve(question)

    answer = generate_answer(question,retrieved)

    add("assistant",answer)

    st.subheader("AI Answer")
    st.write(answer)

    st.subheader("Retrieved Context")

    for doc,score in retrieved:

        st.write(f"Score: {score:.2f}")
        st.write(doc)


st.subheader("Conversation")

for role,msg in history():

    st.write(f"**{role}:** {msg}")
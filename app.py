import streamlit as st
from dotenv import load_dotenv
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq


load_dotenv()

st.set_page_config(page_title="Sanskrit QA", page_icon="📜")
st.title("📜 Sanskrit Question Answering System")

question = st.text_input("Ask a question in Sanskrit:")

@st.cache_resource
def load_rag():
    # ---- SAFE FILE LOADING  ----
    from pathlib import Path

    file_path = Path("data/sanskrit.txt")

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    documents = [Document(page_content=text)]

    # ---- SPLITTING ----
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200,
        separators=["\n\n", "\n", "।", " ", ""]
    )
    chunks = splitter.split_documents(documents)

    # ---- EMBEDDINGS ----
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)

    # ---- LLM ----
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    return vectorstore, llm


vectorstore, llm = load_rag()

if st.button("Get Answer") and question.strip():
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n".join(d.page_content for d in docs)

    prompt = f"""
Answer the question using the context below.
Answer ONLY in Sanskrit.
If the answer is not present, say: उत्तरं न उपलब्धम्।

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)
    st.subheader("Answer:")
    st.write(response.content)

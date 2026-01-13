# 📜 Sanskrit Question Answering System (RAG)

A **Retrieval-Augmented Generation (RAG)** based application that answers **Sanskrit questions** using a **document-driven knowledge base**, ensuring **accurate, non-hallucinated responses**.

---

## ✨ Project Overview

This project allows users to ask questions in **Sanskrit or simple transliteration**, and the system generates answers **strictly based on the provided Sanskrit text**.

Unlike general-purpose chatbots, this system **does not guess or hallucinate answers**.  
If the answer is not present in the document, it clearly responds with:

> **उत्तरं न उपलब्धम्।**  
(*Answer not available*)

This makes the system **reliable, safe, and suitable for academic use**.

---

## 🧠 Key Concepts Used

- **Retrieval-Augmented Generation (RAG)**
- **Semantic Search using Embeddings**
- **Vector Database (FAISS)**
- **Large Language Model (Groq – LLaMA 3.1)**
- **Sanskrit Natural Language Processing**

---

## 🚀 Features

✅ Ask questions in **Sanskrit**  
✅ Context-aware answers from documents  
✅ Zero hallucination (safe RAG)  
✅ Clean & interactive **Streamlit UI**  
✅ Expandable retrieved context for transparency  
✅ Easy to extend with more Sanskrit documents  

---

## 🏗️ Tech Stack

- **Python**
- **Streamlit** – UI
- **LangChain**
- **FAISS** – Vector store
- **Sentence Transformers** – Embeddings
- **Groq LLM (LLaMA 3.1)**
- **dotenv** – Environment variable management

---

## 📁 Project Structure

```text
sanskrit-rag-question-answering/
│
├── app.py                 # Main Streamlit application
├── data/
│   └── sanskrit.txt       # Knowledge base (Sanskrit text)
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignore secrets & virtual environment
├── README.md              # Project documentation

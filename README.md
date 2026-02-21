<div align="center">

## RAG Medical ChatBot  
### Technical Architecture & System Documentation

</div>

## 1. Project Overview
The RAG Medical ChatBot is an intelligent, document-aware conversational system built on the Retrieval-Augmented Generation (RAG) paradigm. It enables users to upload medical PDF documents and ask natural language questions, receiving accurate answers grounded in the uploaded content.
The application combines a LangGraph-powered agentic reasoning loop with FAISS vector search and a cloud-hosted LLM (Groq / LLaMA 3.1), delivered through a responsive Streamlit web interface.

## 2. Key Features
-	Upload and process one or more medical PDF documents
-	Automatic text extraction, chunking, and embedding generation
-	FAISS vector store for fast semantic similarity search
-	LangGraph ReAct agent with memory and tool-use capabilities
-	Groq-hosted LLaMA 3.1 (8B) for low-latency inference
-	Persistent conversation history within a session via thread IDs
-	Modular, extensible architecture for adding new tools (e.g., web search)

## 3. Technology Stack

| Layer              | Technology                         | Purpose                                                |
|--------------------|------------------------------------|--------------------------------------------------------|
| Frontend / UI      | Streamlit                          | Web interface, file upload, chat display              |
| LLM Inference      | Groq API + LLaMA 3.1 8B            | Fast cloud-based language model                       |
| Agent Framework    | LangGraph (ReAct)                  | Agentic reasoning loop with memory                    |
| Embeddings         | HuggingFace all-MiniLM-L6-v2       | Sentence-level vector embeddings                      |
| Vector Store       | FAISS (CPU)                        | Approximate nearest-neighbour search                  |
| PDF Parsing        | pypdf + LangChain                  | Text extraction from PDF pages                        |
| Orchestration      | LangChain / LangChain-Community    | Document loading, text splitting                      |
| Configuration      | python-dotenv                      | Environment variable management                       |


## Current limitations:
- Single-user only (MemorySaver is per-process, not shared)
- PDF processing is synchronous — blocks the UI for large files
- FAISS index lives on disk locally, cannot scale horizontally
- No authentication or rate limiting
- Guardrails module exists but is commented out
- No job queue — one large upload can freeze the entire app

## Improvements:
1. FastAPI Backend — Replace Streamlit for Production
2. Redis Caching Layer
3. Celery Worker — Async PDF Processing
4. Scalable Vector Store — Replace Local FAISS
5. Guardrails — Activate Existing Module
6. Docker Compose — Full Stack Deployment

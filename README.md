<img width="1360" height="207" alt="image" src="https://github.com/user-attachments/assets/d6675ca5-c0cf-4f4f-a68d-69f5d43ac66b" /><div align="center">

## RAG Medical ChatBot  
### Technical Architecture & System Documentation
</div>

## 1. Project Overview
The RAG Medical ChatBot is an intelligent, document-aware conversational system built on the Retrieval-Augmented Generation (RAG) paradigm. It enables users to upload medical PDF documents and ask natural language questions, receiving accurate answers grounded in the uploaded content.
The application combines a LangGraph-powered agentic reasoning loop with FAISS vector search and a cloud-hosted LLM (Groq / LLaMA 3.1), delivered through a responsive Streamlit web interface.

<img width="1360" height="207" alt="image" src="https://github.com/user-attachments/assets/2d2262d8-5fad-47d6-b10c-9962c4132b01" />


## 2. Key Features
-	Upload and process one or more medical PDF documents
-	Text extraction, chunking, and embedding generation
-	FAISS vector store for semantic similarity search
-	LangGraph ReAct agent with memory and tool-use capabilities
-	Groq-hosted LLaMA 3.1 (8B) for low-latency inference
-	Persistent conversation history within a session via thread IDs

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
- Guardrails module exists but is commented out now
- Langfuse commented out and can activate for Observability and Monitoring. 
- No job queue — one large upload can freeze the entire app

## Improvements:
1. FastAPI Backend — Replace for Production and can be binded to Streamlit or React App
2. Redis Caching Layer
3. Celery Worker — Async PDF Processing
4. Scalable Vector Store DB  — Can Replace Local FAISS
5. Guardrails — To activate Existing Module
6. Docker Compose + CI/CD + Kubernetes(AKS or EKS) — Full Stack Deployment

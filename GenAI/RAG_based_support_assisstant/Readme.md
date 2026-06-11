# RAG-Based Customer Support Assistant

## Project Overview

This project is an AI-powered Customer Support Assistant built using Retrieval-Augmented Generation (RAG). The assistant retrieves relevant information from company documents and generates accurate responses to customer queries using Large Language Models (LLMs).

The system combines semantic search with generative AI to provide context-aware answers from a custom knowledge base.

---

## Features

* Document ingestion and preprocessing
* Text chunking for efficient retrieval
* Embedding generation using Sentence Transformers
* Vector database creation using FAISS
* Semantic search and document retrieval
* LLM-powered response generation
* Interactive Streamlit web application
* Context-aware customer support responses

---

## Tech Stack

* Python
* LangChain
* FAISS
* Hugging Face Embeddings
* Sentence Transformers
* Groq LLM
* Streamlit
* Python Dotenv

---

## Project Structure

```text
RAG/
│
├── data/
│   ├── faq.txt
│   ├── return_policy.txt
│   └── shipping_policy.txt
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
├── ingest.py
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## Workflow

1. Load support documents from the data folder.
2. Split documents into smaller chunks.
3. Generate embeddings using Hugging Face models.
4. Store embeddings in a FAISS vector database.
5. Retrieve relevant chunks based on user queries.
6. Pass retrieved context to the LLM.
7. Generate accurate responses using retrieved knowledge.

---

## Installation

### Clone Repository

```bash
git clone <repository_url>
cd RAG
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Create Vector Database

Run:

```bash
python ingest.py
```

This command loads documents, creates embeddings, and stores them in the FAISS vector database.

---

## Run Application

```bash
streamlit run app.py
```

---

## Example Queries

* What is the return policy?
* How long does shipping take?
* How can I reset my password?
* How do I contact customer support?
* When will I receive my refund?

---

## Applications

* Customer Support Automation
* FAQ Chatbots
* Knowledge Base Search
* Internal Documentation Assistants
* Enterprise Information Retrieval

---

## Future Enhancements

* PDF document support
* Chat history memory
* Multi-document retrieval
* Hybrid search
* Deployment on cloud platforms
* User authentication

---

## Results

The system successfully retrieves relevant information from custom documents and generates accurate responses using Retrieval-Augmented Generation (RAG), improving answer quality and reducing hallucinations.

---

## Author

Amrutha Reddy

Data Science | AI & Machine Learning Enthusiast

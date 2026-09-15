# Support AI Agent

An AI-powered customer support agent built with Google's Agent Development Kit (ADK). The project combines an AI agent with a knowledge base to provide context-aware support responses and maintain conversation history through session management.

## 🚀 Project Status

**Prototype / Proof of Concept**

The current version focuses on establishing the core architecture:

* AI support agent
* Knowledge-base retrieval
* ChromaDB vector search
* Google Gemini embeddings
* ADK agent integration
* FastAPI backend
* Conversation session management
* Basic frontend chat interface

## ✨ Key Features

### AI Support Agent

The agent assists users with support questions by using information retrieved from the project's knowledge base.

### Knowledge Base Retrieval

Support documentation is stored in a structured knowledge base and indexed using ChromaDB.

The retrieval pipeline works as follows:

```text
User Question
     ↓
Gemini Embedding
     ↓
ChromaDB Similarity Search
     ↓
Relevant Knowledge
     ↓
ADK Agent
     ↓
Support Response
```

### Conversation Sessions

The application uses ADK sessions to maintain conversation context.

A session is created through:

```http
POST /session
```

The frontend receives a `session_id` and uses that same ID for subsequent questions.

Questions are sent through:

```http
POST /ask
```

This allows multiple messages to belong to the same conversation instead of creating a new session for every request.

---

## 🧠 Session Flow

```text
POST /session
      │
      ▼
Create ADK Session
      │
      ▼
Return session_id
      │
      ▼
Frontend stores session_id
      │
      ▼
POST /ask
      │
      ├── question
      └── session_id
              │
              ▼
        ADK Runner
              │
              ▼
      Existing Session
              │
              ▼
    Context-aware response
```

### Why Sessions?

Without session management, every request could create a separate conversation:

```text
Question 1 → Session A
Question 2 → Session B
Question 3 → Session C
```

With session management:

```text
Question 1 ─┐
Question 2 ─┼──→ Session A
Question 3 ─┘
```

The agent can therefore maintain context throughout the conversation.

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Google Agent Development Kit (ADK)
* Google Gemini
* Pydantic

### AI / Knowledge Retrieval

* ChromaDB
* Gemini Embeddings
* Vector similarity search
* Structured JSON knowledge base

### Frontend

* HTML
* CSS
* JavaScript
* Fetch API

---

## 📁 Project Structure

The structure may evolve as the project grows.

```text
project/
│
├── adk/
│   └── my_agent/
│       ├── agent.py
│       └── __init__.py
│
├── knowledge/
│   └── knowledge_base.json
│
├── my_chroma_data/
│   └── ...
│
├── knowledge_search.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> The exact structure may change as the project moves beyond the prototype stage.

---

## 🔑 Environment Variables

Create a `.env` file for local development.

Example:

```env
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=your-location
GOOGLE_GENAI_USE_VERTEXAI=true
```

Do not commit credentials, API keys, service-account files, or other secrets to Git.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file and add the required Google Cloud / Gemini configuration.

### 6. Start the backend

For example:

```bash
uvicorn main:app --reload
```

---

## 🔌 API Endpoints

### Create Session

```http
POST /session
```

Example response:

```json
{
  "session_id": "example-session-id"
}
```

The frontend stores this session ID and reuses it throughout the conversation.

---

### Ask a Question

```http
POST /ask
```

Example request:

```json
{
  "question": "I'm having an issue with MFA",
  "session_id": "example-session-id"
}
```

Example response:

```json
{
  "answer": "Here are some steps you can try..."
}
```

---

## 🔍 Knowledge Base

The knowledge base uses structured support information containing fields such as:

```text
id
type
category
subtopic
title
summary
keywords
steps
```

These fields are combined into searchable documents and embedded using Gemini.

The resulting vectors are stored in ChromaDB for semantic retrieval.

Example:

```text
User Question
      ↓
Generate Embedding
      ↓
ChromaDB Search
      ↓
Retrieve Relevant Information
      ↓
ADK Agent
      ↓
Generate Response
```

---


All questions should use the **same `session_id`**.

---

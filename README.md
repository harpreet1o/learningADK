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

The session architecture is currently being validated before expanding the application further.

---

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │    Frontend      │
                    │   Chat Client    │
                    └────────┬─────────┘
                             │
                             │ HTTP
                             ▼
                    ┌──────────────────┐
                    │    FastAPI       │
                    │     Backend      │
                    └────────┬─────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
      ┌─────────────────┐          ┌─────────────────┐
      │ Session Service │          │ Knowledge Search│
      │                 │          │                 │
      │ ADK Sessions    │          │ ChromaDB        │
      └────────┬────────┘          │ Gemini Embedding│
               │                   └────────┬────────┘
               │                            │
               ▼                            ▼
        ┌────────────────────────────────────────┐
        │              ADK Runner                │
        │                                        │
        │          Support AI Agent              │
        └────────────────────┬───────────────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Gemini Model   │
                    └──────────────────┘
```

---

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

## 🎯 Current Goals

The prototype is intentionally focused on validating the fundamentals before adding production-level complexity.

### Completed

* [x] Initial ADK agent
* [x] Knowledge-base ingestion
* [x] ChromaDB vector storage
* [x] Gemini embeddings
* [x] Knowledge retrieval
* [x] FastAPI backend
* [x] Basic chat interface
* [x] Session creation
* [x] Session ID passed between frontend and backend
* [x] Conversation context maintained through the same session

### Potential Next Steps

* [ ] Proper user authentication
* [ ] Replace temporary user ID with authenticated user identity
* [ ] Persistent session storage
* [ ] Session expiration / cleanup
* [ ] Improved error handling
* [ ] Improved frontend UI/UX
* [ ] Streaming agent responses
* [ ] Improved knowledge retrieval
* [ ] Logging and monitoring
* [ ] Automated testing
* [ ] Production deployment
* [ ] Security and access controls

---

## 🔐 Security Considerations

This project is currently a prototype.

Before production deployment, additional security considerations will be required, including:

* Authentication and authorization
* Secure session management
* Input validation
* Secret management
* Rate limiting
* Logging and monitoring
* Protection of internal knowledge
* Proper handling of user data

The current prototype uses a temporary user identifier for session creation and should not be considered a production authentication mechanism.

---

## 🧪 Testing Session Persistence

A simple way to test session persistence is to ask related questions sequentially.

```text
User:
"I'm having trouble logging in."

Agent:
Provides troubleshooting information.

User:
"I'm having an issue with MFA."

Agent:
Provides MFA troubleshooting.

User:
"What about the Authy issue?"

Agent:
Should understand that the question relates to the previous MFA discussion.
```

All questions should use the **same `session_id`**.

---

## 📌 Development Approach

The project is being developed incrementally.

The goal is to establish a small, understandable prototype first, validate the architecture with the team, and then introduce additional functionality based on feedback and requirements.

```text
Basic Prototype
      ↓
Team Feedback
      ↓
Architecture Decisions
      ↓
Feature Development
      ↓
Testing
      ↓
Production Hardening
```

---

## 📄 License

This project is intended for internal development and experimentation.

Add the appropriate license or internal-use statement based on the project's organizational requirements.

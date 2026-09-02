Trying to learn the adk provided by google with the python
Created a RAG knowledge base 
How it work?
User:
"I'm not receiving my 2FA code"
        ↓
Gemini Embedding 2
        ↓
Query embedding (3072 numbers)
        ↓
ChromaDB
        ↓
Finds relevant knowledge
        ↓
AUTH-003, AUTH-002, AUTH-001
        ↓
Those results are given to the AI/ADK Agent
        ↓
Gemini reads the retrieved knowledge
        ↓
Decides what answer to give
        ↓
User gets the final response
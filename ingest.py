import os #for the files path 
import json # read/write json
import chromadb

from dotenv import load_dotenv
from google import genai

# Load the environment variables from the .env file
load_dotenv()

project = os.getenv("GOOGLE_CLOUD_PROJECT")
location = os.getenv("GOOGLE_CLOUD_LOCATION")

load_dotenv()
print(location)

ai_client = genai.Client(
    vertexai=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION", "global")
)
print("GenAI client created successfully!")

client = chromadb.PersistentClient(path="./my_chroma_data")

heartbeat = client.heartbeat()
print(f"✅ ChromaDB Connected! Heartbeat: {heartbeat}")

with open("test.json", "r", encoding="utf-8") as file:
    data = json.load(file)

#For clearing out the old because the 3072 instead of 384
# client.delete_collection("velocity_knowledge")
# print("Old collection deleted")

collection = client.get_or_create_collection(
    name="velocity_knowledge",
    embedding_function=None
)

print("Collection created!")

for article in data:
    print(article["id"])
      # Combine the useful information into one searchable document
    document = f"""
Title: {article["title"]}
Category: {article["category"]}
Subtopic: {article["subtopic"]}
Summary: {article["summary"]}
Keywords: {", ".join(article["keywords"])}

Steps:
{chr(10).join(article["steps"])}
"""
    # Generate embedding
    result = ai_client.models.embed_content(
        model="gemini-embedding-2",
        contents=document
    )

    embedding = result.embeddings[0].values
    print("Embedding dimensions:", len(embedding))
# Add the article to ChromaDB
    collection.upsert(
     ids=[article["id"]],
        documents=[document],
        embeddings=[embedding],
        metadatas=[
            {
                "type": article["type"],
                "category": article["category"],
                "subtopic": article["subtopic"]
            }
        ]
    )

results = collection.get(ids=["AUTH-003"],
                         include=["documents", "metadatas", "embeddings"])

print(results)

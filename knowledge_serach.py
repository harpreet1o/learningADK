import os
import chromadb

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()


# Connect to Gemini
ai_client = genai.Client(
    vertexai=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION", "global")
)


# Connect to our existing ChromaDB
chroma_client = chromadb.PersistentClient(
    path="./my_chroma_data"
)

collection = chroma_client.get_collection(
    name="velocity_knowledge"
)


def search_knowledge(query: str):
    """
    Search the Velocity knowledge base using semantic similarity.
    """

    # Create an embedding for the user's question
    result = ai_client.models.embed_content(
        model="gemini-embedding-2",
        contents=query
    )

    query_embedding = result.embeddings[0].values

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    return results

# Basically for the testing if the main file is ran directly the below function will run good for testing but still putting in comments to be safe
# if __name__ == "__main__":

#     query = "I'm not receiving my 2FA code"

#     results = search_knowledge(query)

#     print(results)
import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Establish absolute path for local database per Phase 2 specifications
DB_DIR = os.path.join(os.getcwd(), "local_db")

def get_embedding_model():
    """Initializes the HuggingFace embedding utility."""
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_vector_store() -> Chroma:
    """Initializes or connects to the local ChromaDB instance."""
    return Chroma(
        collection_name="nexus_intel",
        embedding_function=get_embedding_model(),
        persist_directory=DB_DIR
    )

def ingest_data(raw_text: str):
    """
    Bridges reconnaissance and storage. Chunks raw text, generates embeddings,
    and inserts them into the local vector database.
    """
    if not raw_text.strip():
        print("[ALERT] Empty payload received. Aborting ingestion.")
        return

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200,
        add_start_index=True
    )
    chunks = text_splitter.split_text(raw_text)
    docs = [Document(page_content=chunk) for chunk in chunks]
    
    vector_store = get_vector_store()
    vector_store.add_documents(docs)
    print(f"[SYSTEM] Successfully indexed {len(docs)} intelligence chunks into local memory.")

def query_memory(query: str, top_k: int = 2):
    """Retrieves contextually relevant text chunks from local storage."""
    vector_store = get_vector_store()
    return vector_store.similarity_search(query, k=top_k)
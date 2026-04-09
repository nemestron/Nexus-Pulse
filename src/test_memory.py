import os

# Runtime Threading Protection: Prevents OpenMP crashes during C++ execution on Windows
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from dotenv import load_dotenv
from reconnaissance.search import execute_search
from memory.vector_store import ingest_data, query_memory

def main():
    # Ensure credentials are loaded into memory
    load_dotenv()
    print("[SYSTEM] Initiating Phase 2 Local Intelligence Pipeline Test...")

    # Hardcoded test parameters
    target_acquisition = "What are the core principles of Zero Trust Architecture?"
    retrieval_query = "Define Zero Trust Architecture"

    try:
        # Phase 2 - Step 8: Reconnaissance
        print(f"\n[reconnaissance] Executing intelligence gathering for: '{target_acquisition}'")
        raw_intel = execute_search(target_acquisition, max_results=2)
        print("[reconnaissance] Payload acquired.")

        # Phase 2 - Step 10: Ingestion
        print("\n[memory] Ingesting payload into vector database...")
        ingest_data(raw_intel)

        # Phase 2 - Step 11: Verification
        print(f"\n[memory] Querying vector storage for: '{retrieval_query}'")
        results = query_memory(retrieval_query)

        print("\n[VERIFICATION] Retrieved Intelligence Documents:")
        for i, doc in enumerate(results):
            print(f"\n--- Document {i+1} ---")
            print(f"{doc.page_content[:500]}...\n")
            
        print("\n[OPERATION SUCCESS] Phase 2 Testing Complete. local_db provisioned securely.")
        
    except Exception as e:
        print(f"\n[FATAL ERROR] Pipeline execution failed: {e}")

if __name__ == "__main__":
    main()
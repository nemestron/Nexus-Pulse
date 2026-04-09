import os
from dotenv import load_dotenv

# Load environment before any local imports to guarantee system stability
load_dotenv()

from state import GraphState
from agents.nodes import formatting_node

def main():
    print("[SYSTEM] Initiating Phase 3 Cognitive Node Test...")
    
    # Construct mock state per Step 16 requirements
    mock_state = GraphState(
        raw_text="Zero trust architecture implies strict identity verification.",
        filtered_topics=["zero trust", "identity"],
        verification_status=True,
        finalized_draft="Zero trust architecture is a security framework requiring all users, whether in or outside the organization's network, to be authenticated, authorized, and continuously validated for security configuration and posture before being granted or keeping access to applications and data."
    )
    
    try:
        print("\n[agents] Injecting mock state into Formatting Node...")
        result_state = formatting_node(mock_state)
        
        print("\n[VERIFICATION] Formatted Intelligence Payload:")
        print("-" * 60)
        print(result_state.get("finalized_draft"))
        print("-" * 60)
        print("\n[OPERATION SUCCESS] Phase 3 Testing Complete. LLM personas are functional.")
        
    except Exception as e:
        print(f"\n[FATAL ERROR] Node execution failed: {e}")
        print("Ensure GROQ_API_KEY is properly populated in your .env file.")

if __name__ == "__main__":
    main()
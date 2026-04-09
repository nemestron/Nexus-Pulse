import os
from dotenv import load_dotenv

# Enforce environment loading prior to graph traversal
load_dotenv()

from state import GraphState
from graph_engine import app

def main():
    print("\n[SYSTEM] Initiating Phase 4 Stateful Routing Test...")
    
    # Construct initial state simulating a raw command
    initial_state = GraphState(
        raw_text="Retrieve intelligence regarding Zero Trust Architecture protocols.",
        filtered_topics=[],
        verification_status=False,
        finalized_draft=""
    )
    
    try:
        print("[graph] Invoking autonomous state machine traversal...")
        print("-" * 50)
        
        # Stream the graph execution to monitor node transitions dynamically
        for output in app.stream(initial_state):
            for node_name, node_state in output.items():
                print(f"[EXECUTED NODE] -> {node_name.upper()}")
                
        print("-" * 50)
        print("[OPERATION SUCCESS] Phase 4 Testing Complete. State machine routed successfully.")
        
    except Exception as e:
        print(f"\n[FATAL ERROR] Graph traversal failed: {e}")

if __name__ == "__main__":
    main()
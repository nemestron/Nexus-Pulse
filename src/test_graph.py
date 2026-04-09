import os
from dotenv import load_dotenv

load_dotenv()

from state import GraphState
from graph_engine import app

def main():
    print("\n[SYSTEM] Initiating Phase 6 Dissemination Dry Run...")
    
    initial_state = GraphState(
        raw_text="Retrieve intelligence regarding Zero Trust Architecture protocols.",
        filtered_topics=[],
        verification_status=False,
        finalized_draft=""
    )
    
    # Checkpointer mandates a thread ID to track state persistently
    config = {"configurable": {"thread_id": "nexus_thread_001"}}
    
    try:
        print("[graph] Invoking autonomous state machine traversal...")
        print("-" * 50)
        
        # Step 26: Run graph until the interruption barrier
        for output in app.stream(initial_state, config=config):
            for node_name, node_state in output.items():
                print(f"[EXECUTED NODE] -> {node_name.upper()}")
                
        print("-" * 50)
        
        # Step 25: Resume Protocol Logic
        current_state = app.get_state(config)
        
        # Validate if the graph is paused at an execution boundary
        if current_state.next:
            print(f"[ALERT] Graph execution halted. Pending next node: {current_state.next}")
            print("\n[INSPECTION] Reviewing pending intelligence draft:")
            print(">>>", current_state.values.get("finalized_draft", "No draft found."))
            
            # Terminal yielding for Human-in-the-Loop authorization
            auth = input("\n[ACTION REQUIRED] Approve dissemination? (Y/N): ")
            
            if auth.strip().upper() == "Y":
                print("[SYSTEM] Authorization granted. Resuming execution...")
                # Passing None as the input automatically resumes from the checkpoint
                for output in app.stream(None, config=config):
                     for node_name, node_state in output.items():
                        print(f"[EXECUTED NODE] -> {node_name.upper()}")
                print("[OPERATION SUCCESS] Phase 6 Testing Complete. Payload authorized and delivered.")
            else:
                print("[SYSTEM] Authorization denied. Purging thread.")
        else:
            print("[SYSTEM] Graph reached END without interruption. Verification likely failed.")
            
    except Exception as e:
        print(f"\n[FATAL ERROR] Graph traversal failed: {e}")

if __name__ == "__main__":
    main()
import os
import sqlite3
import logging
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
from state import GraphState
from agents.nodes import triage_node, authentication_node, synthesis_node, formatting_node
from delivery.transmission import send_telegram_briefing

# Step 29: Functional Dissemination Node
def dissemination_node(state: GraphState) -> dict:
    """
    The absolute final node in the state machine.
    Triggered only after Human-in-the-Loop (HITL) authorization.
    """
    print("[NODE: Dissemination] Initiating secure transmission...")
    payload = state.get("finalized_draft", "Empty Briefing")
    
    success = send_telegram_briefing(payload)
    
    if success:
        print("[SYSTEM] Intelligence successfully delivered to Telegram.")
    else:
        print("[ERROR] Transmission failed. Check nexus_ops.log for details.")
        
    return {}

# Graph Architecture Construction
workflow = StateGraph(GraphState)

workflow.add_node("triage", triage_node)
workflow.add_node("authentication", authentication_node)
workflow.add_node("synthesis", synthesis_node)
workflow.add_node("formatting", formatting_node)
workflow.add_node("dissemination", dissemination_node)

workflow.set_entry_point("triage")

# Routing Logic
workflow.add_edge("triage", "authentication")

def verification_routing(state: GraphState) -> str:
    if state.get("verification_status") is True:
        return "synthesis"
    return "terminate"

workflow.add_conditional_edges(
    "authentication",
    verification_routing,
    {
        "synthesis": "synthesis",
        "terminate": END
    }
)

workflow.add_edge("synthesis", "formatting")
workflow.add_edge("formatting", "dissemination")
workflow.add_edge("dissemination", END)

# Checkpointer for HITL Persistence
db_path = os.path.join(os.getcwd(), "checkpoints.sqlite")
conn = sqlite3.connect(db_path, check_same_thread=False)
memory = SqliteSaver(conn)

# Compile with Interruption Barrier before dissemination
app = workflow.compile(
    checkpointer=memory, 
    interrupt_before=["dissemination"]
)
import os
import sqlite3
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
from state import GraphState
from agents.nodes import triage_node, authentication_node, synthesis_node, formatting_node

# Phase 5 Placeholder for Phase 6 Delivery
def dissemination_node(state: GraphState) -> dict:
    """External transmission placeholder."""
    print("[NODE: Dissemination] Transmitting intelligence payload to external network...")
    return {}

print("[SYSTEM] Initializing StateGraph engine with SQLite Checkpointer...")
workflow = StateGraph(GraphState)

# Add Official Nodes
workflow.add_node("triage", triage_node)
workflow.add_node("authentication", authentication_node)
workflow.add_node("synthesis", synthesis_node)
workflow.add_node("formatting", formatting_node)
workflow.add_node("dissemination", dissemination_node)

# Set Entry Point
workflow.set_entry_point("triage")

# Sequential Edges (Phase 1)
workflow.add_edge("triage", "authentication")

# Conditional Logic Implementation
def verification_routing(state: GraphState) -> str:
    """Routes based on verification status."""
    if state.get("verification_status") is True:
        return "synthesis"
    else:
        return "terminate"

# Inject Conditional Edge
workflow.add_conditional_edges(
    "authentication",
    verification_routing,
    {
        "synthesis": "synthesis",
        "terminate": END
    }
)

# Sequential Edges (Phase 2)
workflow.add_edge("synthesis", "formatting")
workflow.add_edge("formatting", "dissemination")
workflow.add_edge("dissemination", END)

# Step 23: Initialize SQLite checkpointer for local persistence
db_path = os.path.join(os.getcwd(), "checkpoints.sqlite")
# check_same_thread=False prevents threading errors in standard Windows environments
conn = sqlite3.connect(db_path, check_same_thread=False)
memory = SqliteSaver(conn)

# Step 24: Graph Compilation with Interruption Barrier
print("[SYSTEM] Compiling operational graph with HITL interruption barrier...")
app = workflow.compile(
    checkpointer=memory, 
    interrupt_before=["dissemination"]
)
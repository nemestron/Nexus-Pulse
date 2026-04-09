import os
from langgraph.graph import StateGraph, END
from state import GraphState
from agents.nodes import triage_node, authentication_node, synthesis_node, formatting_node

# Step 18: Graph Initialization
print("[SYSTEM] Initializing StateGraph engine...")
workflow = StateGraph(GraphState)

# Add Official Nodes
workflow.add_node("triage", triage_node)
workflow.add_node("authentication", authentication_node)
workflow.add_node("synthesis", synthesis_node)
workflow.add_node("formatting", formatting_node)

# Set Entry Point
workflow.set_entry_point("triage")

# Sequential Edges (Phase 1)
workflow.add_edge("triage", "authentication")

# Step 19: Conditional Logic Implementation
def verification_routing(state: GraphState) -> str:
    """
    Evaluates the verification status from the Authentication Node.
    Routes to Synthesis if verified, otherwise terminates the graph.
    """
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
workflow.add_edge("formatting", END)

# Step 20: Graph Compilation
print("[SYSTEM] Compiling operational graph...")
app = workflow.compile()
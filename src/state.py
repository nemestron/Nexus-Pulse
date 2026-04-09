from typing import TypedDict, List

# Setting total=False ensures the graph doesn't crash if optional keys are missing
class GraphState(TypedDict, total=False):
    """
    Global state dictionary for the LangGraph state machine.
    Defines the strict payload structure passed between autonomous nodes.
    """
    topic: str
    raw_text: str
    filtered_topics: List[str]
    verification_status: bool
    finalized_draft: str
    draft: str
    verified: bool
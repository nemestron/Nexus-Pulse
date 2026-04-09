from typing import TypedDict, List

class GraphState(TypedDict):
    """
    Global state dictionary for the LangGraph state machine.
    Defines the strict payload structure passed between autonomous nodes.
    """
    raw_text: str
    filtered_topics: List[str]
    verification_status: bool
    finalized_draft: str
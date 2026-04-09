import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from state import GraphState

# CRITICAL FIX: Load environment variables into memory prior to client instantiation
load_dotenv()

# Model Assignments per Phase 3 specifications and operator overrides
# High-speed model for Triage and Formatting operations
fast_llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)
# Heavy-lifter model for Authentication and Synthesis operations
heavy_llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.1)

def triage_node(state: GraphState) -> dict:
    """Evaluates raw text and filters irrelevant data."""
    print("[NODE: Triage] Analyzing raw payload...")
    # Logic to be fully implemented during Phase 4 graph routing
    return {"filtered_topics": ["Extracted Topic 1", "Extracted Topic 2"]}

def authentication_node(state: GraphState) -> dict:
    """Cross-references data with ChromaDB local storage."""
    print("[NODE: Authentication] Verifying claims against memory bank...")
    # Logic to be fully implemented during Phase 4 graph routing
    return {"verification_status": True}

def synthesis_node(state: GraphState) -> dict:
    """Compresses and rewrites verified intelligence."""
    print("[NODE: Synthesis] Compressing verified intelligence...")
    # Logic to be fully implemented during Phase 4 graph routing
    return {"finalized_draft": "Synthesized intelligence draft based on verified sources."}

def formatting_node(state: GraphState) -> dict:
    """Formats the final payload for external dissemination."""
    print("[NODE: Formatting] Applying rigid dissemination constraints...")
    raw_draft = state.get("finalized_draft", "")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a military-grade intelligence formatter. Format the provided text using strict headers, bullet points, and a professional, objective tone. Do not add hallucinated information."),
        ("human", "Format the following intelligence draft:\n\n{draft}")
    ])
    
    chain = prompt | fast_llm
    response = chain.invoke({"draft": raw_draft})
    
    return {"finalized_draft": response.content}
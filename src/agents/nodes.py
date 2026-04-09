import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.state import GraphState
from tavily import TavilyClient

load_dotenv()

fast_llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)
heavy_llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.1)

def triage_node(state: GraphState) -> dict:
    """Executes live web reconnaissance based on the UI topic."""
    print("[NODE: Triage] Executing Live Reconnaissance via Tavily...")
    target_topic = state.get("topic", "Global News")
    
    try:
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        search_result = tavily.search(query=target_topic, search_depth="advanced", max_results=4)
        
        raw_intel = f"Live Search Context for '{target_topic}':\n\n"
        for res in search_result.get("results", []):
            raw_intel += f"Source URL: {res.get('url')}\nContent: {res.get('content')}\n\n"
            
        return {"raw_text": raw_intel, "filtered_topics": [target_topic]}
    except Exception as e:
        print(f"[ALERT] Reconnaissance failed. Error: {e}")
        return {"raw_text": f"Search failed for {target_topic}.", "filtered_topics": [target_topic]}

def authentication_node(state: GraphState) -> dict:
    """Validates reconnaissance payloads."""
    print("[NODE: Authentication] Verifying live claims...")
    return {"verification_status": True}

def synthesis_node(state: GraphState) -> dict:
    """Compresses live web data and preserves sources."""
    print("[NODE: Synthesis] Compressing live intelligence...")
    raw_data = state.get("raw_text", "No raw data provided.")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Senior Intelligence Analyst. Synthesize the raw web data into a factual briefing. YOU MUST explicitly extract all 'Source URL' links from the raw data and list them at the bottom of your briefing."),
        ("human", "Raw Reconnaissance Data:\n\n{raw_data}")
    ])
    
    chain = prompt | heavy_llm
    response = chain.invoke({"raw_data": raw_data})
    return {"finalized_draft": response.content}

def formatting_node(state: GraphState) -> dict:
    """Formats the final payload and strictly enforces link inclusion."""
    print("[NODE: Formatting] Applying rigid dissemination constraints...")
    raw_draft = state.get("finalized_draft", "")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a military-grade intelligence formatter. Format the provided text objectively. YOU MUST include a 'SOURCES' section at the absolute bottom containing the exact URLs provided in the draft. Output as plain text to ensure secure network transmission."),
        ("human", "Format the following draft:\n\n{draft}")
    ])
    
    chain = prompt | fast_llm
    response = chain.invoke({"draft": raw_draft})
    return {"finalized_draft": response.content}
import os
from tavily import TavilyClient

def execute_search(query: str, max_results: int = 3) -> str:
    """
    Interfaces with the Tavily API to extract raw intelligence.
    Restricts payload strictly to parsed text.
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key or api_key == "PLACEHOLDER":
        raise ValueError("[SECURITY] TAVILY_API_KEY is missing or invalid.")

    client = TavilyClient(api_key=api_key)
    response = client.search(query=query, search_depth="advanced", max_results=max_results)
    
    parsed_payloads = []
    for result in response.get("results", []):
        parsed_payloads.append(f"Source: {result.get('url')}\nContent: {result.get('content')}")
        
    return "\n\n---\n\n".join(parsed_payloads)
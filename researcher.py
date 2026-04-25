from tavily import TavilyClient
import os

# API key (fallback)
api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    print("⚠️ Using manual Tavily key")
    api_key = "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"

client = TavilyClient(api_key=api_key)

def impact_researcher(topic):
    query = f"{topic} environmental impact statistics causes effects"

    response = client.search(query=query, max_results=5)

    results = []
    for r in response["results"]:
        results.append(r["content"])

    return "\n".join(results)
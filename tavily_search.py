from tavily import TavilyClient
import os

# 🔑 API Key (fallback for reliability)
api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    print("⚠️ Using manual Tavily key")
    api_key = "PASTE_YOUR_TAVILY_API_KEY_HERE"

client = TavilyClient(api_key=api_key)

# ✅ THIS FUNCTION MUST EXIST
def search(query):
    response = client.search(query=query, max_results=5)
    results = []

    for r in response["results"]:
        results.append(r["content"])

    return "\n".join(results)
from groq import Groq
import os

# API key (fallback)
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("⚠️ Using manual GROQ key")
    api_key = "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"

client = Groq(api_key=api_key)

# ✅ THIS FUNCTION MUST EXIST
def data_extractor(raw_text):
    prompt = f"""
Extract structured environmental data:

{raw_text}

Format:
- Key Facts
- Statistics
- Causes
- Effects
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
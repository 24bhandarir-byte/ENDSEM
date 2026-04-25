from groq import Groq
import os

# API key (fallback)
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("⚠️ Using manual GROQ key")
    api_key = "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"

client = Groq(api_key=api_key)

# ✅ THIS FUNCTION MUST EXIST
def brief_writer(extracted_data, topic):
    prompt = f"""
Write a professional Environmental Impact Brief.

Topic: {topic}

Use this data:
{extracted_data}

Structure:
- Executive Summary
- Key Findings
- Environmental Impact
- Recommendations
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
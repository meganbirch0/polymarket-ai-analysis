from openai import OpenAI

client = OpenAI(api_key="key")
# need to set up billing method and get keyS
question = "Will Bitcoin exceed $100k by 2025?"

prompt = f"""
Estimate the probability of the following event.

Event: {question}

Respond ONLY in this format:
Probability: <number between 0 and 1>
Reasoning: <2-3 sentences>
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
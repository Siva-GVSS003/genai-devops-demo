from openai import OpenAI
import os

# Read API key from GitHub Secrets
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Read log file
with open("logs/error.log", "r") as f:
    log_data = f.read()

prompt = f"""
You are a senior DevOps engineer.

Analyze the following CI/CD or application error log.
Explain:
1. Root cause
2. Why it happened
3. Exact steps to fix it
4. How to prevent it in future

LOG:
{log_data}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are an expert DevOps engineer."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3
)

print("===== AI ANALYSIS =====")
print(response.choices[0].message.content)

1)	OPENAI_API_KEYS :-
import os
from openai import OpenAI
from dotenv import load_dotenv
# Load API key
load_dotenv()
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = input("Enter your prompt: ")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    print("\nResponse:\n", response.choices[0].message.content)
except Exception as e:
    print("Error:", e)

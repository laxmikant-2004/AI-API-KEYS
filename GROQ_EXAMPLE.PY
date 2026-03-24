2)	GROQ_API_KEY :-
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    prompt = input("Enter your prompt: ")
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"
    )
    print("\nResponse:\n", response.choices[0].message.content)
except Exception as e:
    print("Error:", e)

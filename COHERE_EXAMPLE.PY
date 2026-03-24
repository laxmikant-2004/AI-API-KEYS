4)	COHERE_API_KEY :-
import os
import cohere
from dotenv import load_dotenv
load_dotenv()
try:
    co = cohere.Client(os.getenv("COHERE_API_KEY"))
    prompt = input("Enter your prompt: ")
    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=100
    )
    print("\nResponse:\n", response.generations[0].text)
except Exception as e:
    print("Error:", e)

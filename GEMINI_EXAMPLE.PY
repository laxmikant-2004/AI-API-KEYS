3)	GEMINI_API_KEYS :-
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-pro")
    prompt = input("Enter your prompt: ")
    response = model.generate_content(prompt)
    print("\nResponse:\n", response.text)
except Exception as e:
    print("Error:", e)

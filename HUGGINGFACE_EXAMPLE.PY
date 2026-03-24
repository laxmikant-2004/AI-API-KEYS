5) HUGGING FACE API KEY
import os
import requests
from dotenv import load_dotenv
load_dotenv()
try:
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {
        "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
    }
    prompt = input("Enter your prompt: ")
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    result = response.json()
    print("\nResponse:\n", result[0]["generated_text"])
except Exception as e:
    print("Error:", e)

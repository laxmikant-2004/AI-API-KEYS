6)Ollama API Key
import requests
try:
    prompt = input("Enter your prompt: ")
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    data = response.json()
    print("\nResponse:\n", data["response"])
except Exception as e:
    print("Error:", e)

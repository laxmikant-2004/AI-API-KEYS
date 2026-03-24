AI API Integration Project
Overview
This project demonstrates how to integrate multiple AI APIs using Python.
Each API is implemented in a separate Python file as per assignment requirements.

APIs Implemented
- OpenAI
- Groq
- Ollama (Local Model)
- Hugging Face
- Google Gemini
- Cohere

Project Structure

ai-api-project/
│── openai_example.py
│── groq_example.py
│── ollama_example.py
│── huggingface_example.py
│── gemini_example.py
│── cohere_example.py
│── requirements.txt
│── README.md
│── screenshots/
│── .env (not included in repo)

Setup Instructions

1. Clone Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install Dependencies
pip install -r requirements.txt

3. Create ".env" File
Create a ".env" file in the root folder and add your API keys:
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
HUGGINGFACE_API_KEY=your_key
GEMINI_API_KEY=your_key
COHERE_API_KEY=your_key

How to Run
Run any Python file:
python openai_example.py

Security Note
- API keys are stored in ".env" file
- ".env" is not uploaded to GitHub for security reasons

Requirements
- Python 3.x
- Internet connection
- API keys for respective services

Conclusion
This project helps in understanding how to work with different AI APIs and integrate them into Python applications.

Author
Your Name 
laxmikant

# 🤖 CLI Chatbot

A simple and fast **command-line chatbot** built using the OpenAI API and Python.

---

## 🧠 Features
- Uses OpenAI GPT models for responses
- Reads API key securely from `.env` file
- Lightweight and easy to run in any terminal
- Written in pure Python

---

## ⚙️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/AdityaAjay07/cli-chatbot.git
   cd cli-chatbot

2.Create a virtual environment and activate it

python3 -m venv .venv
source .venv/bin/activate

3.Install dependencies

pip install -r requirements.txt

4.Add your OpenAI API key

Create a file named .env in the project folder and add:

OPENAI_API_KEY=your_api_key_here

5.Run the chatbot

Once everything is set up, run:

python3 chatbot.py

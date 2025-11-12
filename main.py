import requests
import json
import os
from dotenv import load_dotenv

# get api key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash-lite"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={api_key}"
HEADERS = {"Content-Type": "application/json"}

chat_history = []

print("Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # Add the new user message to history
    chat_history.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    # 2. build json payload
    payload = {"contents": chat_history}
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    response_data = response.json()

    bot_reply = response_data["candidates"][0]["content"]["parts"][0]["text"]

    print("Gemini:", bot_reply)

    #  Add the bot's reply to history
    chat_history.append({
        "role": "model",
        "parts": [{"text": bot_reply}]
    })
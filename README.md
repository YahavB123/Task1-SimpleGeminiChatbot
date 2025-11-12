An initial demo of a chat with gemini using its api via https requests (because the gemini python sdk doesn't support python3.7)

how to run:

first you need python 3.7 and git.

clone the repo:
* git clone https://github.com/YahavB123/Task1-SimpleGeminiChatbot.git
* cd Task1-SimpleGeminiChatbot

make a virtual environment
* mac/linux: python3 -m venv venv, then run source venv/bin/activate
* on windows: python -m venv venv, then .\venv\Scripts\activate

install the requirements:

* pip install -r requirements.txt

make a .env file. and put an api key from google ai studio
* SECRET_API_KEY="your_actual_api_key_goes_here" 

then run
* python main.py

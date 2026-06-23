# Smart Chatbot Projects

Welcome to the smart chatbot project. Here you will find two simple, easy-to-use chatbots powered by Google's Gemini AI.

Inside this folder, you have:
- `app.py`: A general-purpose chatbot you can talk to about anything.
- `college_chatbot.py`: A specialized assistant that only answers questions about specific college information.

---

## Prerequisites

Before we get started, just make sure you have these two things:
1. **Python**: You'll need Python installed on your computer. If you don't have it yet, you can grab it from [python.org](https://www.python.org/downloads/).
2. **Gemini API Key**: You will also need a free API key from Google so the bots can use their AI. You can get yours at the [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## Setup and Installation

Here is how you can get the chatbots running on your computer:

### 1. Open your terminal
First, open your command prompt or terminal and navigate to this folder:
```bash
cd path/to/smartchatbot
```

### 2. Install the required library
These bots need the `google-genai` library to talk to Google's servers. You can install it by running:
```bash
pip install google-genai
```

### 3. Add your API Key
Open the python files (`app.py` and `college_chatbot.py`) in any text editor. Look for this line near the top:
```python
client = genai.Client(api_key="[ENCRYPTION_KEY]") # enter your api key from gemini api key 
```
Just replace `"[ENCRYPTION_KEY]"` with the actual Gemini API key you got earlier. Make sure to keep the quotation marks around your key.

---

## Running the Chatbots

### General Chatbot
To chat with the general bot, type this into your terminal:
```bash
python app.py
```
You can ask it anything you want. When you are done, just type `exit`.

### College FAQ Chatbot
To run the college assistant, type this:
```bash
python college_chatbot.py
```
This bot is strictly set up to answer questions about the predefined college info (like attendance rules and library timings). Again, type `exit` when you want to leave.

---

## Troubleshooting

If things don't work right away, don't worry. Here are a couple of common fixes:

- **"ModuleNotFoundError: No module named 'google'"**: This usually means the `google-genai` library didn't install properly. Try running `pip install google-genai` one more time.
- **API Key Errors**: Double-check that you pasted the API key correctly inside the quotation marks in both of the Python files.

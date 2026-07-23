# DebugBot — Code Debug Assistant

Welcome to DebugBot! This is a simple, self-contained chatbot that helps you debug your Python code. Paste in your code, and the bot will analyze it for bugs and suggest fixes. You can also enter practice mode to sharpen your debugging skills with randomly generated buggy code challenges.

Inside this folder, you have:
- `debug_chatbot.py`: The main chatbot. Paste your Python code and it will analyze it for syntax errors, common bugs, and suggest fixes.
- `practice_mode.py`: Practice mode that generates random buggy code snippets for you to debug. Score points as you find bugs!

---

## Prerequisites

Before we get started, just make sure you have this:
1. **Python**: You'll need Python 3 installed on your computer. If you don't have it yet, you can grab it from [python.org](https://www.python.org/downloads/).

That's it! No API keys or extra libraries are needed — the bot works entirely offline using Python's built-in tools.

---

## Setup and Installation

Here is how you can get DebugBot running on your computer:

### 1. Open your terminal
First, open your command prompt or terminal and navigate to this folder:
```bash
cd path/to/debugbot
```

### 2. No extra libraries needed
DebugBot only uses Python's built-in modules (`ast`, `py_compile`, `random`), so there is nothing extra to install!

---

## Running the Chatbots

### Debug Assistant
To run the main debug bot, type this into your terminal:
```bash
python debug_chatbot.py
```
Paste your Python code when prompted, type `DONE` on its own line when you are finished, and the bot will analyze it for bugs. When you are done, type `exit`.

### Practice Mode
To run the practice bot, type this:
```bash
python practice_mode.py
```
You will be shown a buggy code snippet. Try to find the bug! Type your answer, `hint` for a hint, `answer` to see the solution, or `exit` to quit. You can track your score as you go.

---

## Troubleshooting

If things don't work right away, don't worry. Here are a couple of common fixes:

- **"ModuleNotFoundError"**: DebugBot only uses built-in modules, so this should not happen. Make sure you are running with Python 3.
- **Code Analysis Not Detecting Issues**: The bot checks for common bugs using pattern matching and Python's built-in parsers. It may not catch every possible issue, but it covers the most frequent mistakes.

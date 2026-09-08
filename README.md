# AI Assistant (Python)

A simple, personal AI assistant built in Python. It understands typed text
commands and responds using voice (text-to-speech), just like a mini Jarvis.

## Features
- Tells current time and date
- Searches Wikipedia and reads out a short summary
- Opens common websites (YouTube, Google, Gmail, GitHub, LinkedIn)
- Performs basic calculations
- Saves and shows personal notes
- Speaks every response out loud

## Tech Stack
- Python 3
- `pyttsx3` – for text-to-speech (offline, no internet needed)
- `wikipedia` – to fetch summaries from Wikipedia
- Built-in libraries: `datetime`, `webbrowser`

## How to Run

1. Install Python 3 (if not already installed) from https://www.python.org/downloads/
2. Open a terminal / command prompt in this project folder.
3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```
4. Run the assistant:
   ```
   python assistant.py
   ```
5. Type commands like:
   - `time`
   - `date`
   - `search python programming`
   - `open youtube`
   - `calculate 25*4`
   - `note buy groceries`
   - `show notes`
   - `help`
   - `exit`

## Example Interaction
```
You: time
Assistant: The current time is 04:30 PM

You: search machine learning
Assistant: Searching Wikipedia for machine learning
Assistant: Machine learning is a field of study in artificial intelligence...

You: open youtube
Assistant: Opening youtube
```

## Future Improvements
- Add voice input (speech recognition) so commands can be spoken instead of typed
- Add weather updates using a weather API
- Add reminders with specific times/alarms
- Build a simple GUI using Tkinter

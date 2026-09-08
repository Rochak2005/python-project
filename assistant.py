"""
AI Assistant - A simple Python-based personal assistant
Author: Rochak Swami

Features:
1. Greets the user
2. Tells current date and time
3. Searches Wikipedia for a topic
4. Opens websites (YouTube, Google, etc.)
5. Does basic calculations
6. Takes notes / reminders
7. Speaks responses out loud (text-to-speech)
"""

import datetime
import webbrowser
import requests
import pyttsx3

def speak(text):
    """Make the assistant speak and also print the text.

    Note: a fresh pyttsx3 engine is created on every call. This works
    around a well-known Windows/SAPI5 bug where reusing a single engine
    across multiple say()/runAndWait() calls causes the assistant to
    go silent after the first one or two responses.
    """
    print(f"Assistant: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)  # speaking speed
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def get_time():
    now = datetime.datetime.now()
    return now.strftime("The current time is %I:%M %p")


def get_date():
    today = datetime.datetime.now()
    return today.strftime("Today's date is %d %B, %Y")


def search_wikipedia(query):
    try:
        title = query.strip().replace(" ", "_")
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
        headers = {"User-Agent": "PersonalAIAssistant/1.0 (student project)"}
        response = requests.get(url, headers=headers, timeout=6)

        if response.status_code == 200:
            data = response.json()
            extract = data.get("extract")
            if extract:
                return extract
            return "I found the page but could not get a summary for it."
        elif response.status_code == 404:
            return "Sorry, I could not find anything on that topic. Try a different spelling."
        else:
            return "Sorry, Wikipedia did not respond properly. Please try again."
    except requests.exceptions.RequestException:
        return "I could not reach Wikipedia. Please check your internet connection."
    except Exception as e:
        return f"Something went wrong while searching Wikipedia. (Error: {e})"


def open_website(site_name):
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "gmail": "https://mail.google.com",
        "github": "https://www.github.com",
        "linkedin": "https://www.linkedin.com",
    }
    site_name = site_name.lower().strip()
    if site_name in sites:
        webbrowser.open(sites[site_name])
        return f"Opening {site_name}"
    else:
        return "Sorry, I don't know that website. Try youtube, google, gmail, github, or linkedin."


def calculate(expression):
    try:
        # Only allow safe characters for basic calculations
        allowed_chars = "0123456789+-*/(). "
        if all(char in allowed_chars for char in expression):
            result = eval(expression)
            return f"The answer is {result}"
        else:
            return "Please enter a valid mathematical expression."
    except Exception:
        return "Sorry, I could not calculate that."


def save_note(note_text):
    with open("notes.txt", "a") as f:
        f.write(note_text + "\n")
    return "Note saved successfully."


def show_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.read()
        if notes.strip() == "":
            return "You have no saved notes."
        return "Here are your notes:\n" + notes
    except FileNotFoundError:
        return "You have no saved notes yet."


def show_help():
    return """
You can try commands like:
- time
- date
- search <topic>            (e.g. search python programming)
- open <website>            (e.g. open youtube)
- calculate <expression>    (e.g. calculate 12*8+5)
- note <your note>          (e.g. note buy groceries)
- show notes
- help
- exit
"""


def run_assistant():
    speak("Hello! I am your personal AI assistant. Type 'help' to see what I can do.")

    while True:
        command = input("\nYou: ").lower().strip()

        if command == "":
            continue

        elif "time" in command:
            speak(get_time())

        elif "date" in command:
            speak(get_date())

        elif command.startswith("search"):
            topic = command.replace("search", "", 1).strip()
            if topic:
                speak("Searching Wikipedia for " + topic)
                speak(search_wikipedia(topic))
            else:
                speak("Please tell me what to search for. Example: search python")

        elif command.startswith("open"):
            site = command.replace("open", "", 1).strip()
            speak(open_website(site))

        elif command.startswith("calculate"):
            expression = command.replace("calculate", "", 1).strip()
            speak(calculate(expression))

        elif command.startswith("note"):
            note_text = command.replace("note", "", 1).strip()
            if note_text:
                speak(save_note(note_text))
            else:
                speak("Please tell me what to note down.")

        elif "show notes" in command:
            print(show_notes())
            speak("I've printed your notes above.")

        elif command == "help":
            print(show_help())

        elif command in ("exit", "quit", "bye"):
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I did not understand that. Type 'help' to see available commands.")


if __name__ == "__main__":
    run_assistant()

import os
import time
import webbrowser
import pyautogui
import pyperclip
import pyjokes
import pyttsx3

# Define the google_search function to generate the Google search URL
def google_search(query):
    # Construct the URL for the Google search query
    url = 'https://www.google.com/search?q=' + query
    # Return the URL
    return url

def main():
    query = input("What do you want to search for? ")
    url = google_search(query)
    pyperclip.copy(url)

    os.system("start chrome")
    time.sleep(5)
    pyautogui.hotkey("ctrl", "t")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    time.sleep(5)
    pyautogui.click(x=500, y=300)

    time.sleep(5)
    pyautogui.click(x=500, y=300)

    time.sleep(5)
    pyautogui.click(x=500, y=300)

    message = "Hello, I am looking for information about " + query
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v") 
    pyautogui.press("enter")

    time.sleep(5)
    pyautogui.click(x=500, y=300)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

if __name__ == "__main__":
    query = input("What do you want to do? ").lower()  # Convert input to lowercase for case-insensitivity

    if "google" in query:
        main()
    elif "youtube" in query:
        webbrowser.open("https://www.youtube.com/")
    elif "joke" in query:
        joke_1 = pyjokes.get_joke(language="en", category="neutral")
        print(joke_1)
        engine.say(joke_1)  # Use the text-to-speech engine to speak the joke
        engine.runAndWait()
    elif "facebook" in query:
        webbrowser.open("https://www.facebook.com/")
    elif "linkedin" in query:
        webbrowser.open("https://www.linkedin.com/")
    elif "instagram" in query:
        webbrowser.open("https://www.instagram.com/")
    elif "maps" in query:
        webbrowser.open("https://www.google.com/maps")
    else:
        main()

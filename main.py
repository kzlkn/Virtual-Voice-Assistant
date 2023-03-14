import speech_recognition as sr
import pyttsx3
import webbrowser

# initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define a function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        speech_text = r.recognize_google(audio)
        print(f"You said: {speech_text}")
        return speech_text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""

# define a function to handle user commands
def handle_command(command):
    if "set a reminder for" in command:
        # extract the reminder text from the command
        reminder = command.split("set a reminder for")[1].strip()
        # code to set the reminder goes here
        speak(f"Reminder set for {reminder}")
    elif "search for" in command:
        # extract the search query from the command
        query = command.split("search for")[1].strip()
        # search the web for the query
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {query}")
    else:
        speak("Sorry, I don't understand that command.")

# main program loop
while True:
    command = recognize_speech()
    if command:
        handle_command(command)

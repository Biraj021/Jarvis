import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am JARVIS. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    return command

def run_jarvis():
    greet()
    while True:
        command = take_command()

        if "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")
        elif "music" in command :
            speak("opening music")
            webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DWVDvBpGQbzXj?si=777ea6415fc145b3")
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break

        elif command:
            speak("I can't do that yet, but I will learn.")

# Start the assistant
run_jarvis()

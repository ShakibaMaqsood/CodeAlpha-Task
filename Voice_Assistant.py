import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import webbrowser
import pygame

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, there was an issue with the service."

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("assistant_response.mp3")
    playsound.playsound("assistant_response.mp3")
    os.remove("assistant_response.mp3")

def process_command(command):
    if "hello" in command:
        return "Hello! How can I help you?"
    elif "open browser" in command:
        webbrowser.open("chrome")
        return "Opening a web browser."
    elif "play music" in command:
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/DELL/Music")
        pygame.mixer.music.play()
        return "Playing music."
    elif "stop music" in command:
        pygame.mixer.music.stop()
        return "Music stopped."
    elif "exit" in command:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that command."

# Main loop for the voice assistant
while True:
    user_input = listen()
    print("User said:", user_input)

    response = process_command(user_input)
    print("Assistant:", response)
    speak(response)

    if "exit" in user_input:
        break
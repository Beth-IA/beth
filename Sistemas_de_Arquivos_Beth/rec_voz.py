import speech_recognition as sr
from datetime import date
from gpiozero import LED
from time import sleep

r = sr.Recognizer()
mic = sr.Microphone()

print("hello")

while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)

import pyaudio
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
	r.adjust_for_ambient_noise(source)
	print("Diga alguma coisa")
	audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
try:
    #frase_portugues = r.recognize_google(audio,language='pt-BR')
    #print("Você disse: " + frase_portugues)
    #print("You said " + r.recognize(audio,language='pt-BR')    # recognize speech using Google Speech Recognition
    print("Você disse: " + r.recognize(audio))
    #print("Você disse: " + r.recognize_google(audio,language='pt-BR'))
    #print("Você disse: " + r.recognize_google(audio))
except LookupError:
    print("Could not understand audio")

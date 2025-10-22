import speech_recognition as sr

# Inicialize o reconhecedor
r = sr.Recognizer()

# Abra o arquivo de áudio
with sr.AudioFile('output.wav') as source:
    # Ouça o conteúdo do arquivo
    audio_data = r.record(source)
    
    # Transcreva o áudio
    text = r.recognize_google(audio_data,language='pt-BR')

    # Exiba o texto transcrito
    print(text)

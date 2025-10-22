from gtts import gTTS

# Texto que você deseja converter em áudio
texto = "Olá! Este é um exemplo de conversão de texto em fala."

# Criação do objeto gTTS
tts = gTTS(text=texto, lang='pt-br')

# Salva o arquivo de áudio
tts.save("audio.mp3")

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
audio_file= open("pergunta_1.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)

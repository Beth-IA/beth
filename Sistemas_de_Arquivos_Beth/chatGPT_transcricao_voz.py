import openai
import time
model_engine = "gpt-3.5-turbo-instruct"
openai.api_key = ""
def GPT(query):
   response = openai.Completion.create(
       engine=model_engine,
       prompt=query,
       max_tokens=1024,
       temperature=0.5,
   )
   return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']
exit_words = ("q","Q","quit","QUIT","EXIT")

audio_file= open("output.wav", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)
time.sleep(2)

conteudo = str(transcript)
print(conteudo)

arquivo = open('./Arquivo_167_transcricao_chatGPT', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_167_transcricao_chatGPT', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[1]
comprimento = len(conteudo)
comprimento = comprimento - 2
conteudo = conteudo[11:comprimento]
print(conteudo)

arquivo = open('./Arquivo_167_transcricao_chatGPT', 'w')
arquivo.writelines(conteudo)
arquivo.close()


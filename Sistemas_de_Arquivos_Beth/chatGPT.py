import openai
model_engine = "gpt-3.5-turbo-instruct"
openai.api_key =""
def GPT(query):
   response = openai.Completion.create(
       engine=model_engine,
       prompt=query,
       max_tokens=1024,
       temperature=0.5,
   )
   return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']
exit_words = ("q","Q","quit","QUIT","EXIT")

#audio_file= open("output.wav", "rb")
#transcript = openai.Audio.translate("whisper-1", audio_file)
#print(transcript)

query = "O que é Arduino?"

(res, usage) = GPT(query)
print(res)

arquivo = open('./Arquivo_175_resultado_assistente_chatGPT', 'w')
arquivo.writelines(res)
arquivo.close()


print("="*20)
print("You have used %s tokens" % usage)
print("="*20)

try:
   while True:
     print("Type q, Q, quit, QUIT or EXIT and press Enter to end the chat session")
     query = input("What is your question?> ")
     if query in exit_words:
           print("ENDING CHAT")
           break
     else:
           (res, usage) = GPT(query)
           print(res)
           print("="*20)
           print("You have used %s tokens" % usage)
           print("="*20)
except KeyboardInterrupt:
     print("\nExiting ChatGPT")

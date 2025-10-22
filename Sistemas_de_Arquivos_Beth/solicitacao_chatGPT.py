import openai
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

arquivo = open('./Arquivo_172_transcricao_traduzida', 'r')
transcricao_traduzida = arquivo.readlines()
transcricao_traduzida = transcricao_traduzida[0]
print(transcricao_traduzida)

query = transcricao_traduzida

(res, usage) = GPT(query)
print(res)

arquivo = open('./Arquivo_175_resultado_assistente_chatGPT', 'w')
arquivo.writelines(res)
arquivo.close()

arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(res)
arquivo.close()



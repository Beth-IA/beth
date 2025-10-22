#Passo 01 - Tirar a foto da expressão matemática
#Passo 02 - Enviar para API Vision, e usar a função OCR da Google Cloud plataforma
#Passo 03 - Armazenar o texto recebido
#Passo 04 - Passo 04 - Concatenar os textos: "Resolva a expressão matemática:" + "texto da foto OCR"
#Passo 05 - Fazer solicitação ao chatGPT
#Passo 06 - Reproduzir a resposta do Robô  



import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid
import openai

model_engine = "gpt-3.5-turbo-instruct"
openai.api_key = ""


os.system('play ocr_rec_texto.mp3')
time.sleep(5)

#Passo 01 - Tirar a foto da expressão matemática
os.system('bash Arquivo_151_Tirar_Foto_OCR.sh')

#time.sleep(6)

#Passo 02 - Enviar para API Vision, e usar a função OCR da Google Cloud plataforma
#Montagem solicitação VISION (Vários Objetos) + Solicitação.sh
arquivo = open('./Arquivo_95_Parte_01_solicitacao_Texto_imagem_OCR', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_97_Solicitacao_Texto_imagem_OCR.json', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_94_codigo_b64_Texto_imagem_OCR', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_97_Solicitacao_Texto_imagem_OCR.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_96_Parte_02_solicitacao_Texto_imagem_OCR', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_97_Solicitacao_Texto_imagem_OCR.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_98_Solicitacao_Nuvem_Texto_imagem_OCR.sh')

time.sleep(5)

#Passo 03 - Armazenar o texto recebido
#os.system('python Tratamento_Resposta_OCR.py')
#Extrair a descrição de todas as palavras dentro da imagem - Arquivo_99_Resposta_Texto_imagem_OCR - Na linha 06 (conteúdo[6])
arquivo = open('./Arquivo_99_Resposta_Texto_imagem_OCR', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[6]
#print(conteudo)

comprimento = len(conteudo)
comprimento = comprimento - 27
conteudo = conteudo[26:comprimento]
#conteudo = conteudo.split(":")[0]
#print(conteudo)

#Passo 05 - Realizar o tratamento da resposta para a nuvem, e armazenar no arquivo: resposta robô (Arquivo 19)
#conteudo = conteudo.split(":")[-1]
#conteudo = conteudo.split(",")[0]
#comprimento = len(conteudo)
#comprimento = comprimento - 1
#conteudo = conteudo[2:comprimento]

conteudo = conteudo.replace("n"," ")

conteudo = "Resolva a expressão matemática: " + conteudo

print(conteudo)


def GPT(query):
   response = openai.Completion.create(
       engine=model_engine,
       prompt=query,
       max_tokens=1024,
       temperature=0.5,
   )
   return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']
exit_words = ("q","Q","quit","QUIT","EXIT")

query = conteudo

(res, usage) = GPT(query)
print(res)

arquivo = open('./Arquivo_175_resultado_assistente_chatGPT', 'w')
arquivo.writelines(res)
arquivo.close()

arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(res)
arquivo.close()


#reproduzir a resposta via Google Cloud Plataforma
os.system('python Arquivo_24_reproduzir_resposta.py')































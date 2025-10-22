import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid

#Passo 04 - Extrair a descrição de todas as palavras dentro da imagem - Arquivo_99_Resposta_Texto_imagem_OCR - Na linha 06 (conteúdo[6])
arquivo = open('./Arquivo_99_Resposta_Texto_imagem_OCR', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[6]

comprimento = len(conteudo)
comprimento = comprimento - 28
conteudo = conteudo[26:comprimento]
#conteudo = conteudo.split(":")[0]

#Passo 05 - Realizar o tratamento da resposta para a nuvem, e armazenar no arquivo: resposta robô (Arquivo 19)
#conteudo = conteudo.split(":")[-1]
#conteudo = conteudo.split(",")[0]
#comprimento = len(conteudo)
#comprimento = comprimento - 1
#conteudo = conteudo[2:comprimento]


conteudo = conteudo.replace("n"," ")

print(conteudo)


inicio = "As palavras que eu estou vendo são: "

arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(inicio)
arquivo.close()

arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()

#Passo 06 - Fazer uma solicitação para o robô reproduzir a resposta
os.system('python Arquivo_24_reproduzir_resposta.py') 
time.sleep(2)



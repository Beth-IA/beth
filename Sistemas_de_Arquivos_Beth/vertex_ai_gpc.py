#API de Inteligência Artificial da Google Cloud Plataforma - VERTEX AI
print("API de Inteligência Artificial da Google Cloud Plataforma - VERTEX AI")

#Importação de Bibliotecas
import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid
#import google.auth.transport.grpc
#import google.auth.transport.requests
#import google.oauth2.credentials
import serial

ser = serial.Serial("/dev/ttyS0",9600)

dado_arduino = str()
dado_valido= str()
controle = ""

#Passo 01 - Reproduzir o arquivo de áudio padrão da API
#mensagem de áudio: API VERTEX da Inteligência Artificial: Coloque uma imagem na frente da câmera e faça qualquer pergunta sobre ela
os.system('play API_VERTEX.mp3')


#Passo 02 - Gravar 10 segundos de áudio da voz captada pelo microfone
#iniciar gravação da voz
os.system('python gravacao_da_voz.py')

#Passo 03 - Converter o arquivo de áudio em texto em português

#transcrição
os.system('python chatGPT_transcricao_voz.py')

#tradução
#os.system('python codigo_traducao_chatGPT.py')


#Passo 04 - Captar a imagem da câmera, e converter para B64
os.system('bash arquivo_175_captar_imagem_vertex_ai.sh')

#Passo 05 - Montar o arquivo JSON referente à solicitação API VERTEX AI

#PARTE 1
#Técnica 01 - ler o conteúdo de um arquivo
arquivo = open('./Arquivo_178_parte_01_vertex', 'r')
conteudo = arquivo.readlines()
arquivo = open('./Arquivo_181_Solicitacao_VERTEX.json', 'w')
arquivo.writelines(conteudo)
arquivo.close()


#Parte 2 - texto do usuário
arquivo = open('./Arquivo_167_transcricao_chatGPT', 'r')
conteudo = arquivo.readlines()
arquivo = open('./Arquivo_181_Solicitacao_VERTEX.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()


#Parte 3
arquivo = open('./Arquivo_179_parte_02_vertex', 'r')
conteudo = arquivo.readlines()
arquivo = open('./Arquivo_181_Solicitacao_VERTEX.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()



#Parte 4 - código B64 da Imagem 
arquivo = open('./Arquivo_177_codigo_b64_vertex', 'r')
conteudo = arquivo.readlines()
arquivo = open('./Arquivo_181_Solicitacao_VERTEX.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()




#Parte 5
arquivo = open('./Arquivo_180_parte_03_vertex', 'r')
conteudo = arquivo.readlines()
arquivo = open('./Arquivo_181_Solicitacao_VERTEX.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()



#Passo 06 - Montar o arquivo bash para a solicitação para a API VERTEX AI
os.system('bash Arquivo_183_Enviar_Solicitacao_VERTEX.sh')

#Passo 07 - Fazer o tratamento da Resposta recebida pela nuvem e reproduzir resposta
os.system('python Tratamento_Resposta_VERTEX.py')

#Passo 08 - Tradução da resposta recebida de inglês para português
os.system('python traducao_texto_padrao.py')

#Passo 09 - Montar a resposta

inicio = "A minha análise da imagem é: "

arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(inicio)
arquivo.close()


arquivo = open('./Arquivo_78_traducao_final','r')
conteudo = arquivo.readlines()


arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()

#Passo 10 - Fazer uma solicitação para o robô reproduzir a resposta
os.system('python Arquivo_24_reproduzir_resposta.py')
time.sleep(2)



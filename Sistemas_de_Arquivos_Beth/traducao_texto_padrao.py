#Codigo principal do Robo
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
#Passo 5 - Montagem solicitação Tradução

print("Iniciando traducao...")

arquivo = open('./Arquivo_73_parte_1_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./texto_para_traducao_1', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_74_parte_2_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_70_Solicitacao_Traducao.sh')
time.sleep(5)
#Passo 6 - Tratamento da Resposta Tradução 
os.system('python Arquivo_75_extracao_resultados_traducao.py')
time.sleep(1)


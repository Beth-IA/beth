import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid


os.system('play marcas_famosas.mp3')
time.sleep(2)

#Tirar foto
os.system('bash Arquivo_153_tirar_foto_logotipo.sh')

time.sleep(6)
#Montagem solicitação VISION (Vários Objetos) + Solicitação.sh

arquivo = open('./Arquivo_88_Parte_01_solicitacao_logotipo', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_90_Solicitacao_logotipo.json', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_87_codigo_b64_logotipo', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_90_Solicitacao_logotipo.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_89_Parte_02_solicitacao_logotipo', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_90_Solicitacao_logotipo.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_91_Solicitacao_Nuvem_logotipo.sh')

time.sleep(5)

os.system('python Tratamento_Resposta_Logotipo.py ')




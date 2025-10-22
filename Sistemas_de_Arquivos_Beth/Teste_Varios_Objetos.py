import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid



   #Montagem solicitação VISION (Vários Objetos) + Solicitação.sh

arquivo = open('./Arquivo_81_Parte_01_solicitacao_desafio', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_83_Solicitacao_desafio.json', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_80_codigo_b64_desafio', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_83_Solicitacao_desafio.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_82_Parte_02_solicitacao_desafio', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_83_Solicitacao_desafio.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_84_Solicitacao_Nuvem_desafio.sh')


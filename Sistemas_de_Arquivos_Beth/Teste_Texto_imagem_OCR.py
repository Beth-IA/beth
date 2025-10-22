import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid


os.system('play ocr_rec_texto.mp3')
time.sleep(5)

#tirar foto do cartaz

os.system('bash Arquivo_151_Tirar_Foto_OCR.sh')

#time.sleep(6)

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

os.system('python Tratamento_Resposta_OCR.py')







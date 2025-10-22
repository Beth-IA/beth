import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid

#Passo 04 - Extrair a descrição de todas as palavras dentro da imagem - Arquivo_99_Resposta_Texto_imagem_OCR - Na linha 06 (conteúdo[6])
arquivo = open('./Arquivo_182_Resposta_Solicitacao_VERTEX', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[2]

comprimento = len(conteudo)
comprimento = comprimento - 2
conteudo = conteudo[5:comprimento]
#conteudo = conteudo.split(":")[0]

#Passo 05 - Realizar o tratamento da resposta para a nuvem, e armazenar no arquivo: resposta robô (Arquivo 19)
#conteudo = conteudo.split(":")[-1]
#conteudo = conteudo.split(",")[0]
#comprimento = len(conteudo)
#comprimento = comprimento - 1
#conteudo = conteudo[2:comprimento]


#conteudo = conteudo.replace("n"," ")

print(conteudo)


arquivo = open('./texto_para_traducao_1', 'w')
arquivo.writelines(conteudo)
arquivo.close()




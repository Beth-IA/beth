import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid

#Passo 04 - Extrair a descrição de todas as palavras dentro da imagem - Arquivo_99_Resposta_Texto_imagem_OCR - Na linha 06 (conteúdo[6])
arquivo = open('./Arquivo_92_Resposta_logotipo', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[6]

#Passo 05 - Realizar o tratamento da resposta para a nuvem, e armazenar no arquivo: resposta robô (Arquivo 19)
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]
#res = conteudo.translate(str.maketrans('' n '', chars))
#conteudo = res
#Extrair palavras separadas
#Palavra 01

#palavra_separada_01 = conteudo
#comprimento = len(palavra_separada_01)
#palavra_separada_01 = palavra_separada_01[2:comprimento]


#arquivo = open('./arquivo_teste', 'w')
#arquivo.writelines(conteudo)
#arquivo.close()

#comprimento = len(conteudo)
#comprimento = comprimento - 1
#conteudo = conteudo[2:comprimento]
print(conteudo)
inicio = "Esta marca é: "

arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(inicio)
arquivo.close()

arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()

#Guardar a posição "x" da marca
arquivo = open('./Arquivo_92_Resposta_logotipo', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[11]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
conteudo = conteudo[1:comprimento]
print("Posição da Marca")
print(conteudo)
arquivo = open('./posicao_marca', 'w')
arquivo.writelines(conteudo)
arquivo.close()



#Passo 06 - Fazer uma solicitação para o robô reproduzir a resposta
os.system('python Arquivo_24_reproduzir_resposta.py')
time.sleep(2)

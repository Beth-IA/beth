import serial
import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid


ser = serial.Serial("/dev/ttyS0",9600)
dado_arduino = str()
dado_valido= str()

controle = ""

os.system('play desafio_inicio.mp3')
time.sleep(5)

#Passo 01 - Tirar foto
#Passo 02 - Converter foto para B64
os.system('bash Arquivo_143_tirar_foto_4_objetos.sh')


#Passo 03 - Montar solicitação JSON - API VISION - Vários Objetos
arquivo = open('./Arquivo_81_Parte_01_solicitacao_desafio', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_83_Solicitacao_desafio.json', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_124_codigo_B64_resposta_objetos', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_83_Solicitacao_desafio.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_82_Parte_02_solicitacao_desafio', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_83_Solicitacao_desafio.json', 'a')
arquivo.writelines(conteudo)
arquivo.close()

#Passo 04 - Executar o arquivo BASH para realizar a solicitação à nuvem
os.system('bash Arquivo_84_Solicitacao_Nuvem_desafio.sh')


#Passo 05 - Extrair os nomes dos objetos da resposta da nuvem
#extrair os nomes que estão no arquivo resposta
#executar o arquivo tipo bash - Arquivo_100_extracao_nomes_varios_objetos.sh
os.system('bash Arquivo_100_extracao_nomes_varios_objetos.sh')


#separar o nome de cada objeto em um arquivo diferente

#Extrair Objeto 0
arquivo = open('./Arquivo_101_nomes_varios_objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_102_nome_objeto_0', 'w')
arquivo.writelines(conteudo)
arquivo.close()

#Extrair Objeto 1
arquivo = open('./Arquivo_101_nomes_varios_objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[1]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_103_nome_objeto_01', 'w')
arquivo.writelines(conteudo)
arquivo.close()

#Extrair Objeto 2
arquivo = open('./Arquivo_101_nomes_varios_objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[2]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_104_nome_objeto_02', 'w')
arquivo.writelines(conteudo)
arquivo.close()



#EXTRAIR A LINHA EXATA DE CADA OBJETO NO Arquivo_85_Resposta_Varios_Objetos

#Extrair a LINHA do objeto 0
arquivo = open('./Arquivo_106_2_extrair_linha_objeto_parte_01', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_108_extrair_linha_objeto.sh', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_102_nome_objeto_0', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_108_extrair_linha_objeto.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_107_extrair_linha_objeto_parte_02', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_108_extrair_linha_objeto.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_108_extrair_linha_objeto.sh')

#Montar extração da linha exata do objeto 0
arquivo = open('./Arquivo_132_resultado_extracao_linha_objeto', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
comprimento = len(conteudo)
conteudo = conteudo[4:6]
conteudo = int(conteudo)
conteudo = conteudo + 5
linha_exata_unica = conteudo - 1
#print("Linha exata única:")
#print(linha_exata_unica)
conteudo = str(conteudo)

arquivo = open('./Arquivo_109_linha_exata_objeto_0', 'w')
arquivo.writelines(conteudo)
arquivo.close()

#Ir na linha EXATA ÚNICA 
arquivo = open('./Arquivo_85_Resposta_Varios_Objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[linha_exata_unica]


#Coletar posição x do objeto 0
#arquivo = open('./Arquivo_133_extracao_posicao_x_parte_1', 'r')
#conteudo = arquivo.readlines()

#arquivo = open('./Arquivo_138_extrair_posicao_x.sh', 'w')
#arquivo.writelines(conteudo)
#arquivo.close()

#arquivo = open('./Arquivo_109_linha_exata_objeto_0', 'r')
#conteudo = arquivo.readlines()

#arquivo = open('./Arquivo_138_extrair_posicao_x.sh', 'a')
#arquivo.writelines(conteudo)
#arquivo.close()

#arquivo = open('./Arquivo_134_extracao_posicao_x_parte_2_objeto_0', 'r')
#conteudo = arquivo.readlines()

#arquivo = open('./Arquivo_138_extrair_posicao_x.sh', 'a')
#arquivo.writelines(conteudo)
#arquivo.close()

#os.system('bash Arquivo_138_extrair_posicao_x.sh')


#arquivo = open('./Arquivo_113_posicao_x_objeto_0', 'r')
#conteudo = arquivo.readlines()
#conteudo = conteudo[0]

arquivo = open('./Arquivo_113_posicao_x_objeto_0', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_113_posicao_x_objeto_0', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]

comprimento = len(conteudo)
comprimento = comprimento - 5

conteudo = conteudo[3:6]

arquivo = open('./Arquivo_113_posicao_x_objeto_0', 'w')
arquivo.writelines(conteudo)
arquivo.close()


############Extrair a posição do objeto 1#########################################################
#arquivo = open('./Arquivo_106_extrair_linha_objeto_parte_01', 'r')
arquivo = open('./Arquivo_106_2_extrair_linha_objeto_parte_01', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_108_extrair_linha_objeto.sh', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_103_nome_objeto_01', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_108_extrair_linha_objeto.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_107_extrair_linha_objeto_parte_02', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_108_extrair_linha_objeto.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_108_extrair_linha_objeto.sh')

arquivo = open('./Arquivo_132_resultado_extracao_linha_objeto', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
comprimento = len(conteudo)
conteudo = conteudo[4:6]
conteudo = int(conteudo)
conteudo = conteudo + 5
linha_exata_unica = conteudo - 1
#print("Linha exata única- objeto 01:")
conteudo = str(conteudo)

arquivo = open('./Arquivo_110_linha_exata_objeto_1', 'w')
arquivo.writelines(conteudo)
arquivo.close()
#Ir na linha EXATA ÚNICA
arquivo = open('./Arquivo_85_Resposta_Varios_Objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[linha_exata_unica]


#Coletar posição x do objeto 1
#arquivo = open('./Arquivo_133_extracao_posicao_x_parte_1', 'r')
#conteudo = arquivo.readlines()

#arquivo = open('./Arquivo_138_extrair_posicao_x.sh', 'w')
#arquivo.writelines(conteudo)
#arquivo.close()

#arquivo = open('./Arquivo_110_linha_exata_objeto_1', 'r')
#conteudo = arquivo.readlines()

#arquivo = open('./Arquivo_138_extrair_posicao_x.sh', 'a')
#arquivo.writelines(conteudo)
#arquivo.close()

#arquivo = open('./Arquivo_135_extracao_posicao_x_parte_2_objeto_1', 'r')
#conteudo = arquivo.readlines()

#arquivo = open('./Arquivo_138_extrair_posicao_x.sh', 'a')
#arquivo.writelines(conteudo)
#arquivo.close()

#os.system('bash Arquivo_138_extrair_posicao_x.sh')

        #Garantir a primeira LINHA
#arquivo = open('./Arquivo_114_posicao_x_objeto_1', 'r')
#conteudo = arquivo.readlines()
#conteudo = conteudo[0]


arquivo = open('./Arquivo_114_posicao_x_objeto_1', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_114_posicao_x_objeto_1', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]

comprimento = len(conteudo)
comprimento = comprimento - 5

conteudo = conteudo[3:6]

arquivo = open('./Arquivo_114_posicao_x_objeto_1', 'w')
arquivo.writelines(conteudo)
arquivo.close()

############################################################################################






############Extrair a posição do objeto 2#########################################################
#arquivo = open('./Arquivo_106_extrair_linha_objeto_parte_01', 'r')
arquivo = open('./Arquivo_106_2_extrair_linha_objeto_parte_01', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_108_extrair_linha_objeto.sh', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_104_nome_objeto_02', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_108_extrair_linha_objeto.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_107_extrair_linha_objeto_parte_02', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_108_extrair_linha_objeto.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_108_extrair_linha_objeto.sh')


arquivo = open('./Arquivo_132_resultado_extracao_linha_objeto', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
comprimento = len(conteudo)
conteudo = conteudo[4:6]
conteudo = int(conteudo)
conteudo = conteudo + 5
linha_exata_unica = conteudo - 1
#print("Linha exata única- objeto 02:")
conteudo = str(conteudo)

arquivo = open('./Arquivo_111_linha_exata_objeto_2', 'w')
arquivo.writelines(conteudo)
arquivo.close()


#Coletar posição x do objeto 1
#arquivo = open('./Arquivo_133_extracao_posicao_x_parte_1', 'r')
#conteudo = arquivo.readlines()

#arquivo = open('./Arquivo_138_extrair_posicao_x.sh', 'w')
#arquivo.writelines(conteudo)
#arquivo.close()

#arquivo = open('./Arquivo_111_linha_exata_objeto_2', 'r')
#conteudo = arquivo.readlines()

#arquivo = open('./Arquivo_138_extrair_posicao_x.sh', 'a')
#arquivo.writelines(conteudo)
#arquivo.close()

#arquivo = open('./Arquivo_136_extracao_posicao_x_parte_2_objeto_2', 'r')
#conteudo = arquivo.readlines()

#arquivo = open('./Arquivo_138_extrair_posicao_x.sh', 'a')
#arquivo.writelines(conteudo)
#arquivo.close()

#os.system('bash Arquivo_138_extrair_posicao_x.sh')

        #Garantir a primeira LINHA
#arquivo = open('./Arquivo_115_posicao_x_objeto_2', 'r')
#conteudo = arquivo.readlines()
#conteudo = conteudo[0]

#Ir na linha EXATA ÚNICA
arquivo = open('./Arquivo_85_Resposta_Varios_Objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[linha_exata_unica]

arquivo = open('./Arquivo_115_posicao_x_objeto_2', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_115_posicao_x_objeto_2', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]

comprimento = len(conteudo)
comprimento = comprimento - 5

conteudo = conteudo[3:6]

arquivo = open('./Arquivo_115_posicao_x_objeto_2', 'w')
arquivo.writelines(conteudo)
arquivo.close()

############################################################################################




#Resultados dos nomes e posições dos objetos
print("Nome do  objeto 0:")
arquivo = open('./Arquivo_102_nome_objeto_0', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
print(conteudo)
print("posição do  objeto 0:")
arquivo = open('./Arquivo_113_posicao_x_objeto_0', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
print(conteudo)
#Enviar posição do objeto 0 ou A
#controle ="o"+"a"+conteudo
#ser.write(str.encode(controle))



print("Nome do  objeto 1:")
arquivo = open('./Arquivo_103_nome_objeto_01', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
print(conteudo)
print("posição do  objeto 1:")
arquivo = open('./Arquivo_114_posicao_x_objeto_1', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
print(conteudo)
#Enviar posição do objeto 1 ou b
#controle = "b"+conteudo
#ser.write(str.encode(controle))




print("Nome do  objeto 2:")
arquivo = open('./Arquivo_104_nome_objeto_02', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
print(conteudo)
print("posição do  objeto 2:")
arquivo = open('./Arquivo_115_posicao_x_objeto_2', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
print(conteudo)
#Enviar posição do objeto 2 ou c
#controle = "c"+conteudo
#ser.write(str.encode(controle))

#Colocar os nomes na ordem posição
os.system('python colocar_ordem_desafio.py')
time.sleep(1)


#montar as respostas dos 3 objetos

print("Traduzindo objeto 1...")

arquivo = open('./Arquivo_73_parte_1_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./objeto_posicao_01', 'r')
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



conteudo = "Eu estou segurando o objeto da posição 01, e ele é um "
arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_78_traducao_final', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('python Arquivo_146_reproduzir_resposta_objeto_1.py')


print("Traduzindo objeto 2...")

arquivo = open('./Arquivo_73_parte_1_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./objeto_posicao_02', 'r')
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

conteudo = "Eu estou segurando o objeto da posição 02, e ele é um "
arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_78_traducao_final', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('python Arquivo_147_reproduzir_resposta_objeto_2.py')



print("Traduzindo objeto 3...")

arquivo = open('./Arquivo_73_parte_1_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./objeto_posicao_03', 'r')
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

conteudo = "Eu estou segurando o objeto da posição 03, e ele é um "
arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_78_traducao_final', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('python Arquivo_148_reproduzir_resposta_objeto_3.py')



os.system('play desafio_objeto_01.mp3')
time.sleep(1)
controle = "x"
ser.write(str.encode(controle))
dado_arduino = ser.read()
dado_valido = dado_arduino[0]
dado_valido = int(dado_valido)
print(dado_valido)
os.system('play Arquivo_126_audio_resposta_objeto_1.mp3')
dado_arduino = ser.read()
dado_valido = dado_arduino[0]
dado_valido = int(dado_valido)
print(dado_valido)

os.system('play desafio_objeto_02.mp3')
time.sleep(1)
controle = "y"
ser.write(str.encode(controle))
dado_arduino = ser.read()
dado_valido = dado_arduino[0]
dado_valido = int(dado_valido)
print(dado_valido)
os.system('play Arquivo_127_audio_resposta_objeto_2.mp3')
dado_arduino = ser.read()
dado_valido = dado_arduino[0]
dado_valido = int(dado_valido)
print(dado_valido)

os.system('play desafio_objeto_03.mp3')
time.sleep(1)
controle = "z"
ser.write(str.encode(controle))
dado_arduino = ser.read()
dado_valido = dado_arduino[0]
dado_valido = int(dado_valido)
print(dado_valido)
os.system('play Arquivo_128_audio_resposta_objeto_3.mp3')


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

controle = ""

#Passo 01 - Criar solicitação JSON para tradução da frase do objeto 0
arquivo = open('./Arquivo_73_parte_1_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_102_nome_objeto_0', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_74_parte_2_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_70_Solicitacao_Traducao.sh')

time.sleep(5)

#Passo 6 - Tratamento da Resposta Tradução 
os.system('python Arquivo_75_extracao_resultados_traducao.py')
time.sleep(1)
#Passo 7 - Montagem da Resposta do RObô - Resposta 4

conteudo = "Eu estou vendo "
arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_78_traducao_final', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()


#Passo 6 - Reprodução da Resposta do Robô
os.system('python Arquivo_145_reproduzir_resposta_objeto_0.py') 


###################################### OBJETO 01
#Passo 01 - Criar solicitação JSON para tradução da frase do objeto 0
arquivo = open('./Arquivo_73_parte_1_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_103_nome_objeto_01', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_74_parte_2_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_70_Solicitacao_Traducao.sh')
time.sleep(5)

#Passo 6 - Tratamento da Resposta Tradução 
os.system('python Arquivo_75_extracao_resultados_traducao.py')
time.sleep(1)
#Passo 7 - Montagem da Resposta do RObô - Resposta 4

conteudo = "Eu estou vendo "
arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_78_traducao_final', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()

#Passo 6 - Reprodução da Resposta do Robô
os.system('python Arquivo_146_reproduzir_resposta_objeto_1.py') 
##################################################################################






###################################### OBJETO 02
#Passo 01 - Criar solicitação JSON para tradução da frase do objeto 0
arquivo = open('./Arquivo_73_parte_1_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_104_nome_objeto_02', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_74_parte_2_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_70_Solicitacao_Traducao.sh')
time.sleep(5)

#Passo 6 - Tratamento da Resposta Tradução 
os.system('python Arquivo_75_extracao_resultados_traducao.py')
time.sleep(1)
#Passo 7 - Montagem da Resposta do RObô - Resposta 4

conteudo = "Eu estou vendo "
arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_78_traducao_final', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()

#Passo 6 - Reprodução da Resposta do Robô
os.system('python Arquivo_147_reproduzir_resposta_objeto_2.py') 
##################################################################################














###################################### OBJETO 03
#Passo 01 - Criar solicitação JSON para tradução da frase do objeto 0
arquivo = open('./Arquivo_73_parte_1_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_105_nome_objeto_03', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_74_parte_2_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('Arquivo_71_conteudo_solicitacao.json','a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_70_Solicitacao_Traducao.sh')
time.sleep(5)

#Passo 6 - Tratamento da Resposta Tradução 
os.system('python Arquivo_75_extracao_resultados_traducao.py')
time.sleep(1)
#Passo 7 - Montagem da Resposta do RObô - Resposta 4

conteudo = "Eu estou vendo "
arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_78_traducao_final', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_19_resposta_robo', 'a')
arquivo.writelines(conteudo)
arquivo.close()

#Passo 6 - Reprodução da Resposta do Robô
os.system('python Arquivo_148_reproduzir_resposta_objeto_3.py') 
##################################################################################





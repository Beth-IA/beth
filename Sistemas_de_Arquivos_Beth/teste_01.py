import os
import time

#Extrair a LINHA do objeto 0
#arquivo = open('./Arquivo_106_2_extrair_linha_objeto_parte_01', 'r')
arquivo = open('./Arquivo_11_parte_1_extracao_dado_desejado', 'r')
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

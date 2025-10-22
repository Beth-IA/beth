#extracao resultados traducao
import os
import time

os.system('bash Arquivo_76_extrair_caracteristicas_traducao.sh')
arquivo = open('./Arquivo_77_traducoes', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 2
conteudo = conteudo[2:comprimento]

arquivo = open('Arquivo_78_traducao_final','w')
arquivo.writelines(conteudo)
arquivo.close()


print(conteudo)

import os
import time

#extracao de resultados do objeto
os.system('bash Arquivo_62_extracao_caracteristicas_objetos.sh')

arquivo = open('./Arquivo_63_todos_objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_64_objeto_0', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_63_todos_objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[1]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_65_objeto_1', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_63_todos_objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[2]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_66_objeto_2', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_63_todos_objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[3]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_67_objeto_3', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_63_todos_objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[4]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_68_objeto_4', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_63_todos_objetos', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[5]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_69_objeto_5', 'w')
arquivo.writelines(conteudo)
arquivo.close()


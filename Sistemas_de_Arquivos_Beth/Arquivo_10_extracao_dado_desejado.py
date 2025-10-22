import os
import time
#extracao do dado desejado
arquivo = open('./Arquivo_11_parte_1_extracao_dado_desejado', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_13__solicitacao_extracao_dado_desejado_PLN.sh', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_9_linha_exata', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_13__solicitacao_extracao_dado_desejado_PLN.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_12_parte_2_extracao_dado_desejado', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_13__solicitacao_extracao_dado_desejado_PLN.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_13__solicitacao_extracao_dado_desejado_PLN.sh')
time.sleep(1)
os.system('bash Arquivo_15_garantir_nome.sh')

arquivo = open('./Arquivo_16_dado_desejado', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]

comprimento = len(conteudo)
comprimento = comprimento - 1

conteudo = conteudo[2:comprimento]

arquivo = open('./Arquivo_17_informacao_desejada', 'w')
arquivo.writelines(conteudo)
arquivo.close()






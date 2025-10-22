import os
import time
#pegar a transcrição da voz
arquivo = open('./Arquivo_167_transcricao_chatGPT', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
#print(conteudo)

#traduzir o texto da transcrição
arquivo = open('./Arquivo_169_parte_inicial_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_171_traduzir_texto.sh', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_167_transcricao_chatGPT', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_171_traduzir_texto.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_170_parte_final_traducao', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_171_traduzir_texto.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

time.sleep(1)

os.system('bash Arquivo_171_traduzir_texto.sh')

time.sleep(2)

arquivo = open('./Arquivo_172_transcricao_traduzida', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[2]
print(conteudo)

time.sleep(1)

#conteudo = str(conteudo)
arquivo = open('./Arquivo_172_transcricao_traduzida', 'w')
arquivo.writelines(conteudo)
arquivo.close()



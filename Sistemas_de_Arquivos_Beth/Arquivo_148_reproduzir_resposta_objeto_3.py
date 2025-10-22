#Codigo para reproduzir a resposta do robo
import os
import time


arquivo = open('./Arquivo_20_parte_1_API_TEXTO_VOZ', 'r')
conteudo = arquivo.readlines()


arquivo = open('./Arquivo_23_Solicitacao_API_TEXTO_VOZ.sh', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_19_resposta_robo', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_23_Solicitacao_API_TEXTO_VOZ.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_21_parte_2_API_TEXTO_VOZ', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_23_Solicitacao_API_TEXTO_VOZ.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()


os.system('bash Arquivo_23_Solicitacao_API_TEXTO_VOZ.sh')

time.sleep(5)

arquivo = open('./Arquivo_22_codigoB64_resposta_robo', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[1]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
print("Comprimento da STRING:")
print(len(conteudo))
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

arquivo = open('Arquivo_22_codigoB64_resposta_robo','w')
arquivo.writelines(conteudo)
arquivo.close()

os.system('bash Arquivo_150_converter_codigo_b64_em_mp3_objeto_3.sh')

time.sleep(1)

#os.system('play Arquivo_128_audio_resposta_objeto_3.mp3')











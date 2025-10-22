import time
import os
#iniciar gravação da voz
os.system('python gravacao_da_voz.py')

#transcrição
os.system('python chatGPT_transcricao_voz.py')

#tradução
os.system('python codigo_traducao_chatGPT.py')

#incrementar o resultado da tradução da transcrição na resposta do robô
arquivo = open('./Arquivo_172_transcricao_traduzida', 'r')
conteudo = arquivo.readlines()

arquivo = open('./Arquivo_19_resposta_robo', 'w')
arquivo.writelines(conteudo)
arquivo.close()

#reproduzir a resposta via Google Cloud Plataforma
os.system('python Arquivo_24_reproduzir_resposta.py')

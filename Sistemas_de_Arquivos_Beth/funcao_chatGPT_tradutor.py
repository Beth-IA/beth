import time
import os
#iniciar gravação da voz
os.system('python gravacao_da_voz.py')

#transcrição
os.system('python chatGPT_transcricao_voz.py')

#tradução
os.system('python codigo_tradutor_idiomas.py')

#solicitação de resposta no chatGPT
#os.system('python solicitacao_chatGPT_tradutor.py')

#reproduzir a resposta via Google Cloud Plataforma
os.system('python Arquivo_24_reproduzir_resposta.py')

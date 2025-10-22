#Codigo principal do Robo
import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid

#import google.auth.transport.grpc
#import google.auth.transport.requests
#import google.oauth2.credentials
import serial

ser = serial.Serial("/dev/ttyS0",9600)

dado_arduino = str()
dado_valido= str()
controle = ""

def funcao_reconhecimento_facial():
    #Pergunta 03 - Você pode olhar para mim?

    print('Reconhecimento de Imagens - FACIAL')
    #Passo 1 - Emitir pergunta 03
    #os.system('play pergunta_3.mp3')
    os.system('play audio_rec_facial.mp3')
    #Passo 2 - Tirar uma foto + conversão em b64
    os.system('bash Arquivo_47_tirar_foto_face.sh')
    time.sleep(5)
    #Passo 3 - Montagem solicitação VISION (facial) + Solicitação.sh

    arquivo = open('./Arquivo_51_parte_1_vision', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_49_solicitacao_vision_facial.json', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

    arquivo = open('./Arquivo_43_codigo_b64_rosto', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_49_solicitacao_vision_facial.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    arquivo = open('./Arquivo_52_parte_2_vision_facial', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_49_solicitacao_vision_facial.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    os.system('bash Arquivo_54_solicitacao_vision_facial.sh')
    time.sleep(5)

    #Passo 4 - Tratamento da Resposta VISION Facial
    os.system('python Arquivo_58_extracao_resultados_face.py')
    time.sleep(1)
    #
    #Passo 5 - Montagem da Resposta do RObô - Resposta 3
    arquivo = open('./Arquivo_45_informacao_desejada', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('Arquivo_19_resposta_robo','w')
    arquivo.writelines(conteudo)
    arquivo.close()
    #Passo 6 - Reprodução da Resposta do Robô
    os.system('python Arquivo_24_reproduzir_resposta.py') 
    time.sleep(2)

def funcao_reconhecimento_objetos():
    #Reconhecimento de Objetos
    #Pergunta 04 - Você pode colocar algum objeto na minha frente?
    print('Iniciando Reconhecimento de Objetos...')
    #Passo 1 - Emitir pergunta 04
    #os.system('play pergunta_4.mp3')
    os.system('play audio_rec_objetos.mp3')
    #Passo 2 - Tirar uma foto + conversão em b64
    os.system('bash Arquivo_48_tirar_foto_objeto.sh')
    time.sleep(5)
    #Passo 3 - Montagem solicitação VISION (objetos) + Solicitação.sh
    arquivo = open('./Arquivo_51_parte_1_vision', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_50_solicitacao_vision_objetos.json', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

    arquivo = open('./Arquivo_44_codigo_b64_objeto', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_50_solicitacao_vision_objetos.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    arquivo = open('./Arquivo_53_parte_2_vision_objeto', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_50_solicitacao_vision_objetos.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    os.system('bash Arquivo_55_solicitacao_vision_objeto.sh')
    time.sleep(5)

    #Passo 4 - Tratamento da Resposta VISION objetos
    os.system('python Arquivo_61_extracao_resultados_objetos.py') 
    #Passo 5 - Montagem solicitação Tradução

    print("Iniciando traducao...")

    arquivo = open('./Arquivo_73_parte_1_traducao', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

    arquivo = open('./Arquivo_64_objeto_0', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    conteudo = " "

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()


    arquivo = open('./Arquivo_65_objeto_1', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    conteudo = " "

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()


    arquivo = open('./Arquivo_66_objeto_2', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    conteudo = " "

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()


    arquivo = open('./Arquivo_67_objeto_3', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    conteudo = " "

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()


    arquivo = open('./Arquivo_68_objeto_4', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    conteudo = " "

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()


    arquivo = open('./Arquivo_69_objeto_5', 'r')
    conteudo = arquivo.readlines()

    arquivo = open('./Arquivo_71_conteudo_solicitacao.json', 'a')
    arquivo.writelines(conteudo)
    arquivo.close()

    conteudo = " "

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


    #Passo 8 - Reprodução da Resposta do Robô
    os.system('python Arquivo_24_reproduzir_resposta.py') 
    time.sleep(2)

while True:
#    print("Enviando x para o Arduino NANO") 
#    controle = "x"
#    ser.write(str.encode(controle))
#    time.sleep(1)
#    funcao_reconhecimento_objetos()
#    funcao_reconhecimento_facial()
    print("Aguardando dado do Arduino...")
    dado_arduino = ser.read()
    dado_valido = dado_arduino[0]
    dado_valido = int(dado_valido)
    print(dado_valido)
    if(dado_valido==99):
        print("Função 01 -Reconhecimento FACIAL")
        funcao_reconhecimento_facial()
    if(dado_valido==97):
        print("Função 02 - Reconhecimento de Objetos")
        funcao_reconhecimento_objetos()
    if(dado_valido==122):
        #é preciso realizar o ajuste fino da programação com o Arduino após a montagem
        print("Função 03 - Desafio dos 3 objetos")
        os.system('python Detectar_varios_objetos.py')
    if(dado_valido==98):
        #é preciso realizar o ajuste fino da programação com o Arduino após a montagem 
        print("Função 04 - Ler texto")
        os.system('python Teste_Texto_imagem_OCR.py')
    if(dado_valido==104):
        #print("Função 05 - Reconhecer Marcas famosas")
        #os.system('python Teste_logotipo.py')
        print("Função 08 - API VERTER IA") 
        os.system('python vertex_ai_gpc.py')
    if(dado_valido==103):
        print("Função 06 - Corpo ATIVADA")   
        os.system('play funcao_movimento.mp3')
    if(dado_valido==109):
        print("Ativando a inteligência do robô")
    if(dado_valido==100):
        print("Assistente chatGPT")
        os.system('python funcao_chatGPT_assistente.py')
    if(dado_valido==102):
        print("Tradutor de Inglês para Português Ativado")
        os.system('python funcao_chatGPT_tradutor.py')
    if(dado_valido==101):
        print("Cálculos Matemáticos ativados")
        os.system('python matematica.py')








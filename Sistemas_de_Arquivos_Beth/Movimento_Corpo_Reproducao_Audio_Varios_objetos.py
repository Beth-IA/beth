#importar bibliotecas
import serial
import concurrent.futures
import json
import logging
import os
import os.path
import sys
import time
import uuid

#declarar variáveis e configurar parâmetros
ser = serial.Serial("/dev/ttyS0",9600)
dado_arduino = str()
dado_valido= str()
controle = ""

##########################-------OBJETO 0---------------##############################################
#enviar mensagem serial para o Arduino mover o robô para a posição do objeto 0
controle = "x"
ser.write(str.encode(controle))
#aguardar a mensagem serial chegar do Arduino informando que o corpo já se deslocou para a posição do objeto zero
print("Aguardando o Arduino movimentar o corpo até o objeto 0...")
dado_arduino = ser.read()
dado_valido = dado_arduino[0]
dado_valido = int(dado_valido)
print(dado_valido)

#reproduzir a resposta do objeto ZERO
os.system('play Arquivo_125_audio_resposta_objeto_0.mp3')


##########################-------OBJETO 1---------------##############################################
#enviar mensagem serial para o Arduino mover o robô para a posição do objeto 1
controle = "y"
ser.write(str.encode(controle))
#aguardar a mensagem serial chegar do Arduino informando que o corpo já se deslocou para a posição do objeto 1
print("Aguardando o Arduino movimentar o corpo até o objeto 1...")
dado_arduino = ser.read()
dado_valido = dado_arduino[0]
dado_valido = int(dado_valido)
print(dado_valido)

#reproduzir a resposta do objeto ZERO
os.system('play Arquivo_126_audio_resposta_objeto_1.mp3')


##########################-------OBJETO 2---------------##############################################
#enviar mensagem serial para o Arduino mover o robô para a posição do objeto 2
controle = "z"
ser.write(str.encode(controle))
#aguardar a mensagem serial chegar do Arduino informando que o corpo já se deslocou para a posição do objeto 2
print("Aguardando o Arduino movimentar o corpo até o objeto 2...")
dado_arduino = ser.read()
dado_valido = dado_arduino[0]
dado_valido = int(dado_valido)
print(dado_valido)

#reproduzir a resposta do objeto ZERO
os.system('play Arquivo_127_audio_resposta_objeto_2.mp3')


##########################-------OBJETO 3---------------##############################################
#enviar mensagem serial para o Arduino mover o robô para a posição do objeto 3
controle = "w"
ser.write(str.encode(controle))
#aguardar a mensagem serial chegar do Arduino informando que o corpo já se deslocou para a posição do objeto 3
print("Aguardando o Arduino movimentar o corpo até o objeto 3...")
dado_arduino = ser.read()
dado_valido = dado_arduino[0]
dado_valido = int(dado_valido)
print(dado_valido)

#reproduzir a resposta do objeto ZERO
os.system('play Arquivo_128_audio_resposta_objeto_3.mp3')

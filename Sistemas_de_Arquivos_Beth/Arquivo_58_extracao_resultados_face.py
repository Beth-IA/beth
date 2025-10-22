#Arquivo_58_extracao_resultados_face
import os
import time
import serial

ser = serial.Serial("/dev/ttyS0",9600)

controle = ""

os.system('bash Arquivo_59_extracao_facial.sh')

arquivo = open('./Arquivo_60_extracao_caracteristica_facial', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
comprimento = len(conteudo)
comprimento = comprimento - 1
conteudo = conteudo[2:comprimento]

if(conteudo == "VERY_LIKELY"):
    controle = "f"
    ser.write(str.encode(controle))
    print("Ele está alegre!")
    conteudo = "Que maravilha, você está feliz. Depois de conversar comigo, você saltará de alegria"

if(conteudo == "POSSIBLE"):
    print("Ele está alegre!")
    controle = "f"
    ser.write(str.encode(controle))
    conteudo = "Que maravilha, você está feliz. Depois de conversar comigo, você saltará de alegria"

if(conteudo == "VERY_UNLIKELY"):
    controle = "t"
    ser.write(str.encode(controle))
    print("Ele está triste!")
    conteudo = "Que pena que você está triste. Espero que depois de conversar comigo você fique mais alegre"

arquivo = open('Arquivo_45_informacao_desejada','w')
arquivo.writelines(conteudo)
arquivo.close()

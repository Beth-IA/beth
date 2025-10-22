import serial
import time

ser = serial.Serial("/dev/ttyS0",9600)

dado_arduino = str()
dado_valido= str()
controle = ""


while True:
    #Bloco de instruções responsáveis por receber dados via SERIAL
    #print("Aguardando dado do Arduino...")
    #dado_arduino = ser.read()
    #dado_valido = dado_arduino[0]
    #dado_valido = int(dado_valido)
    #print(dado_valido)
    #if(dado_valido==97):
    #    print("Função 01 -Reconhecimento FACIAL")
    print("Enviando dados para o Arduino...")
    controle = "x"
    ser.write(str.encode(controle))
    time.sleep(5)
    controle = "y"
    ser.write(str.encode(controle))
    time.sleep(5)
    controle = "z"
    ser.write(str.encode(controle))
    time.sleep(5)

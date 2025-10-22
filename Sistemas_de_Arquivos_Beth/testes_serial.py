import time
import serial

ser = serial.Serial("/dev/ttyS0",9600)

dado_arduino = str()
dado_valido= str()

while True:
    dado_arduino = ser.read()
    dado_valido = dado_arduino[0]
    #dado_valido = int(dado_valido)
    print(dado_valido)
    if(dado_valido==97):
        print("Conversar com o Robô")
        print("Conversar com o Robô")
    if(dado_valido==98):
        print("Reconhecimento FACIAL")
    if(dado_valido==99):
        print("Reconhecimento de Objetos")   


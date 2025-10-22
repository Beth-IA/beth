import serial
import time

ser = serial.Serial("/dev/ttyS0",9600)
dado_arduino = str()
dado_valido= str()

controle = ""



while True:
#Envio da informação via SERIAL
	print("Enviando x")
	controle = "x"
	ser.write(str.encode(controle))
	time.sleep(3)

	print("Enviando y")
	controle = "y"
	ser.write(str.encode(controle))
	time.sleep(3)

	print("Enviando z")
	controle = "z"
	ser.write(str.encode(controle))
	time.sleep(3)

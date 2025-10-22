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

controle = "f"
ser.write(str.encode(controle))
print("Ele está alegre!")
time.sleep(5)

controle = "t"
ser.write(str.encode(controle))
print("Ele está triste!")
time.sleep(5)

controle = "x"
ser.write(str.encode(controle))
print("Coloque na posição 01!")
time.sleep(5)

controle = "y"
ser.write(str.encode(controle))
print("Coloque na posição 02!")
time.sleep(5)

controle = "z"
ser.write(str.encode(controle))
print("Coloque na posição 03!")
time.sleep(5)










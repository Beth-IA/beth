import time
import serial

ser = serial.Serial("/dev/ttyS0",9600)
dado_arduino = str()
dado_valido= str()

#os.system('python /home/pi/env/lib/python3.7/site-packages/googlesamples/assistant/grpc/codigo_loop_robo.py')

while True:
        #controle = "b"
        #ser.write(str.encode(controle))
        #time.sleep(3)
        #controle = 'b'
        #ser.write(str.encode(controle))
        #time.sleep(3)
        dado_arduino = ser.read()
        dado_valido = dado_arduino[0]
        dado_valido = int(dado_valido)
        print(dado_valido)
        if(dado_valido==97):
            print('Conversar com o Robô')
        if(dado_valido==98):
            print('Reconhecimento FACIAL')
        if(dado_valido==99):
            print('Reconhecimento de Objetos')    

import os
import time
import subprocess

process = subprocess.Popen(['sox', '-t', 'alsa', 'default', 'output.wav'])
#os.system('bash gravacao_da_voz.sh')
time.sleep(10)
process.terminate()



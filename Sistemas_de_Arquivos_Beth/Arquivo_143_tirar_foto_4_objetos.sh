#libcamera-still -r -o Arquivo_144_foto_4_objetos.jpg
fswebcam -r 640x480 --jpeg 85 -D 1 Arquivo_144_foto_4_objetos.jpg
sleep 5
base64 Arquivo_144_foto_4_objetos.jpg > Arquivo_124_codigo_B64_resposta_objetos

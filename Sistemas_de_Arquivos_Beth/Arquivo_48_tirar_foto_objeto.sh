fswebcam -r 640x480 --jpeg 85 -D 1 Arquivo_46_foto_objeto.jpg
#libcamera-still -r -o Arquivo_46_foto_objeto.jpg
sleep 5
base64 Arquivo_46_foto_objeto.jpg > Arquivo_44_codigo_b64_objeto

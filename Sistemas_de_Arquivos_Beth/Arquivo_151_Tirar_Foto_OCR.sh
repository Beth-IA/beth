fswebcam -r 640x480 --jpeg 85 -D 1 Arquivo_152_foto_OCR.jpg
#libcamera-still -r -o Arquivo_152_foto_OCR.jpg
#fswebcam -r 268x188 --jpeg 85 -D 1 Arquivo_152_foto_OCR.jpg
sleep 5
base64 Arquivo_152_foto_OCR.jpg > Arquivo_94_codigo_b64_Texto_imagem_OCR

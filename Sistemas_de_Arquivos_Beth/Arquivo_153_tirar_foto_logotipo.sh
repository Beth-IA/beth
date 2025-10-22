fswebcam -r 640x480 --jpeg 85 -D 1 Arquivo_154_foto_OCR.jpg
#libcamera-still -r -o Arquivo_154_foto_OCR.jpg
sleep 5
base64 Arquivo_154_foto_OCR.jpg > Arquivo_87_codigo_b64_logotipo

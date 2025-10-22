#libcamera-still -r -o Arquivo_45_foto_rosto.jpg
fswebcam -r 640x480 --jpeg 85 -D 1 Arquivo_45_foto_rosto.jpg
sleep 5
base64 Arquivo_45_foto_rosto.jpg > Arquivo_43_codigo_b64_rosto
#base64 face_luiz_gustavo.jpg > Arquivo_43_codigo_b64_rosto


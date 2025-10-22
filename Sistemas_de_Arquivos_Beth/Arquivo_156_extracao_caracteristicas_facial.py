#Extracao caracteristicas facial

#arquivo = open('./Arquivo_155_caracteristica_facial', 'r')
#conteudo = arquivo.readlines()
conteudo = " "
arquivo = open('./Arquivo_159_face_detectada', 'w')
arquivo.writelines(conteudo)
arquivo.close()

for i in range(0,34):
	arquivo = open('./Arquivo_155_caracteristica_facial', 'r')
	conteudo = arquivo.readlines()
	#print("Características do Tipo",i)
	conteudo = conteudo[i]
	conteudo = conteudo[3:6]
	linha_valor_x = int(conteudo)
	linha_valor_x = linha_valor_x - 1
	linha_valor_y = linha_valor_x + 1
	linha_valor_z = linha_valor_x + 2

	arquivo = open('./Arquivo_56_resposta_solicitacao_vision_facial', 'r')
	conteudo = arquivo.readlines()

	conteudo_x = conteudo[linha_valor_x]
	#print(conteudo_x)

	conteudo_y = conteudo[linha_valor_y]
	#print(conteudo_y)

	conteudo_z = conteudo[linha_valor_z]
	#print(conteudo_z)

	arquivo = open('./Arquivo_159_face_detectada', 'a')
	arquivo.writelines(conteudo_x)
	arquivo.close()

	arquivo = open('./Arquivo_159_face_detectada', 'a')
	arquivo.writelines(conteudo_y)
	arquivo.close()

	arquivo = open('./Arquivo_159_face_detectada', 'a')
	arquivo.writelines(conteudo_z)
	arquivo.close()

#Testar a face detectada com a face da mulher
acumulador = 0
for i in range(1,102):
	arquivo = open('./Arquivo_159_face_detectada', 'r')
	conteudo1 = arquivo.readlines()
	conteudo1 = conteudo1[i]
	conteudo1 = conteudo1[21:27]
	#print(conteudo1)
	conteudo1 = float(conteudo1)

	arquivo = open('./Arquivo_165_face_larissa', 'r')
	conteudo2 = arquivo.readlines()
	conteudo2 = conteudo2[i]
	conteudo2 = conteudo2[21:27]
	#print(conteudo2)
	conteudo2 = float(conteudo2)

	if(conteudo1>conteudo2):
		diferenca = conteudo1-conteudo2
	if(conteudo2>conteudo1):
		diferenca = conteudo2-conteudo1
	if(conteudo1==conteudo2):
		diferenca = 0
	#print(diferenca)
	acumulador = acumulador + diferenca


print("Fator Identificação de Pessoas - Larissa ",acumulador)

#Testar a face detectada com a face de Luiz Gustavo
acumulador = 0
for i in range(1,102):
        arquivo = open('./Arquivo_159_face_detectada', 'r')
        conteudo1 = arquivo.readlines()
        conteudo1 = conteudo1[i]
        conteudo1 = conteudo1[21:27]
        #print(conteudo1)
        conteudo1 = float(conteudo1)

        arquivo = open('./Arquivo_166_face_luiz_gustavo', 'r')
        conteudo2 = arquivo.readlines()
        conteudo2 = conteudo2[i]
        conteudo2 = conteudo2[21:27]
        #print(conteudo2)
        conteudo2 = float(conteudo2)

        if(conteudo1>conteudo2):
                diferenca = conteudo1-conteudo2
        if(conteudo2>conteudo1):
                diferenca = conteudo2-conteudo1
        if(conteudo1==conteudo2):
                diferenca = 0
        #print(diferenca)
        acumulador = acumulador + diferenca


print("Fator Identificação de Pessoas - Luiz Gustavo ",acumulador)


conteudo = " "
arquivo = open('./Arquivo_166_face_luiz_gustavo', 'w')
arquivo.writelines(conteudo)
arquivo.close()

for i in range(0,34):
        arquivo = open('./Arquivo_155_caracteristica_facial', 'r')
        conteudo = arquivo.readlines()
        print("Características do Tipo",i)
        conteudo = conteudo[i]
        conteudo = conteudo[3:6]
        linha_valor_x = int(conteudo)
        linha_valor_x = linha_valor_x + 1
        linha_valor_y = linha_valor_x + 1
        linha_valor_z = linha_valor_x + 2

        arquivo = open('./Arquivo_56_resposta_solicitacao_vision_facial', 'r')
        conteudo = arquivo.readlines()

        conteudo_x = conteudo[linha_valor_x]
        print(conteudo_x)

        conteudo_y = conteudo[linha_valor_y]
        print(conteudo_y)

        conteudo_z = conteudo[linha_valor_z]
        print(conteudo_z)


        arquivo = open('./Arquivo_166_face_luiz_gustavo', 'a')
        arquivo.writelines(conteudo_x)
        arquivo.close()

        arquivo = open('./Arquivo_166_face_luiz_gustavo', 'a')
        arquivo.writelines(conteudo_y)
        arquivo.close()

        arquivo = open('./Arquivo_166_face_luiz_gustavo', 'a')
        arquivo.writelines(conteudo_z)
        arquivo.close()

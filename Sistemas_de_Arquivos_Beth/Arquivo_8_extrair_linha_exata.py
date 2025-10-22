arquivo = open('./Arquivo_7_extracao_caracteristica_PLN', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
comprimento = len(conteudo)
conteudo = conteudo[4:6]
conteudo = int(conteudo)
conteudo = conteudo - 2
conteudo = str(conteudo)

arquivo = open('./Arquivo_9_linha_exata', 'w')
arquivo.writelines(conteudo)
arquivo.close()



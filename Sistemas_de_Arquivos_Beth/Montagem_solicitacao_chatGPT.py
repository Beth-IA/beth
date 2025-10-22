import os
#pegar a primeira parte 

arquivo = open('./Arquivo_173_parte_inicial_solicitacao_chatGPT', 'r')
conteudo = arquivo.readlines()

arquivo = open('./solicitacao_chatGPT.py', 'w')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./Arquivo_172_transcricao_traduzida', 'r')
conteudo_traducao = arquivo.readlines()
conteudo_traducao = conteudo_traducao[0]
print(conteudo_traducao)

arquivo = open('./solicitacao_chatGPT.py', 'a')
arquivo.writelines(conteudo_traducao)
arquivo.close()

arquivo = open('./Arquivo_174_parte_final_solicitacao_chatGPT', 'r')
conteudo = arquivo.readlines()

arquivo = open('./solicitacao_chatGPT.py', 'a')
arquivo.writelines(conteudo)
arquivo.close()

arquivo = open('./solicitacao_chatGPT.py', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[15]
print(conteudo)


#os.system('python solicitacao_chatGPT.py')



arquivo = open('./Arquivo_173_parte_inicial_solicitacao_chatGPT', 'r')
conteudo1 = arquivo.readlines()

arquivo = open('./Arquivo_172_transcricao_traduzida', 'r')
conteudo2 = arquivo.readlines()

arquivo = open('./Arquivo_174_parte_final_solicitacao_chatGPT', 'r')
conteudo3 = arquivo.readlines()

conteudo_total = conteudo1 + conteudo2 + conteudo3

arquivo = open('./solicitacao_chatGPT.py', 'w')
arquivo.writelines(conteudo_total)
arquivo.close()

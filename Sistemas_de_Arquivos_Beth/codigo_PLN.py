#Codigo PLN

#ler conteudo da parte inicial da solicitacao PLN
arquivo = open('./Arquivo_2_Parte_Inicial_SolicitacaoPLN', 'r')
conteudo = arquivo.readlines()    

#gravar no arquivo 4 da solicitacao PLN
arquivo = open('./Arquivo_4_Solicitacao_PLN.sh', 'w')
arquivo.writelines(conteudo)
arquivo.close()
    

#ler conteudo da transcricao
arquivo = open('./Arquivo_1_Transcricao_da_VOZ', 'r')
conteudo = arquivo.readlines()    

#gravar no arquivo 4 da solicitacao PLN (adicionar conteudo)
arquivo = open('./Arquivo_4_Solicitacao_PLN.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()

#ler conteudo da parte FINAL da solicitacao PLN
arquivo = open('./Arquivo_3_Parte_Final_SolicitacaoPLN', 'r')
conteudo = arquivo.readlines()    


#gravar no arquivo 4 da solicitacao PLN (adicionar conteudo)
arquivo = open('./Arquivo_4_Solicitacao_PLN.sh', 'a')
arquivo.writelines(conteudo)
arquivo.close()




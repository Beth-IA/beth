#extracao_sentimento
import os
import serial

ser = serial.Serial("/dev/ttyS0",9600)
controle = ""

os.system('bash Arquivo_35_extrair_sentimento_score.sh')

arquivo = open('./Arquivo_36_sentimento_score', 'r')
conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = conteudo.split(":")[-1]
conteudo = conteudo.split(",")[0]
print(conteudo)

arquivo = open('Arquivo_36_sentimento_score','w')
arquivo.writelines(conteudo)
arquivo.close()


conteudo = float(conteudo)


if conteudo >= 0:
        print("Dia Feliz")
        controle = "a"
        ser.write(str.encode(controle))
        conteudo = str(conteudo)
        conteudo = " Fique mais tempo com "
        arquivo = open('Arquivo_37_parte_pessoa_resposta_dia','w')
        arquivo.writelines(conteudo)
        arquivo.close()
        
        conteudo = " ,esteja mais vezes em "
        arquivo = open('Arquivo_38_parte_local_resposta_dia','w')
        arquivo.writelines(conteudo)
        arquivo.close()
        
        conteudo = " ,consuma mais "
        arquivo = open('Arquivo_39_parte_produto_resposta_dia','w')
        arquivo.writelines(conteudo)
        arquivo.close()
        arquivo = open('./Arquivo_40_inicio_dia_feliz', 'r')
    
else:
        print("Dia triste")
        controle = "b"
        ser.write(str.encode(controle))
        conteudo = str(conteudo)
        conteudo = " Fique menos tempo com "
        arquivo = open('Arquivo_37_parte_pessoa_resposta_dia','w')
        arquivo.writelines(conteudo)
        arquivo.close()
        
        conteudo = " ,esteja menos vezes em "
        arquivo = open('Arquivo_38_parte_local_resposta_dia','w')
        arquivo.writelines(conteudo)
        arquivo.close()
        
        conteudo = " ,consuma menos "
        arquivo = open('Arquivo_39_parte_produto_resposta_dia','w')
        arquivo.writelines(conteudo)
        arquivo.close()
        
        arquivo = open('./Arquivo_41_inicio_dia_triste', 'r')
        

conteudo = arquivo.readlines()
conteudo = conteudo[0]
conteudo = str(conteudo)
arquivo = open('Arquivo_42_inicio_resposta_sentimento','w')
arquivo.writelines(conteudo)
arquivo.close()




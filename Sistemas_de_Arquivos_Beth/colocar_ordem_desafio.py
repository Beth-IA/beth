contador_0=0
contador_1=0
contador_2=0


arquivo = open('./Arquivo_113_posicao_x_objeto_0', 'r')
posicao_objeto_0 = arquivo.readlines()
posicao_objeto_0 = posicao_objeto_0[0]
print(posicao_objeto_0)

arquivo = open('./Arquivo_114_posicao_x_objeto_1', 'r')
posicao_objeto_1 = arquivo.readlines()
posicao_objeto_1 = posicao_objeto_1[0]
print(posicao_objeto_1)

arquivo = open('./Arquivo_115_posicao_x_objeto_2', 'r')
posicao_objeto_2 = arquivo.readlines()
posicao_objeto_2 = posicao_objeto_2[0]
print(posicao_objeto_2)

#Contagem objeto 0
if(posicao_objeto_0>posicao_objeto_1):
        contador_0 = contador_0 + 1
if(posicao_objeto_0>posicao_objeto_2):
        contador_0 = contador_0 + 1

#Contagem objeto 1
if(posicao_objeto_1>posicao_objeto_0):
        contador_1 = contador_1 + 1
if(posicao_objeto_1>posicao_objeto_2):
        contador_1 = contador_1 + 1

#Contagem objeto 2
if(posicao_objeto_2>posicao_objeto_1):
        contador_2 = contador_2 + 1
if(posicao_objeto_2>posicao_objeto_0):
        contador_2 = contador_2 + 1

print("Contador 0:")
print(contador_0)

print("Contador 1:")
print(contador_1)

print("Contador 2:")
print(contador_2)




#contador 0, 01 e 02.

#TESTE OBJETO 0
if(contador_0==0):
    arquivo = open('./Arquivo_102_nome_objeto_0', 'r')
    conteudo = arquivo.readlines()
    arquivo = open('./objeto_posicao_01', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
if(contador_0==1):
    arquivo = open('./Arquivo_102_nome_objeto_0', 'r')
    conteudo = arquivo.readlines()
    arquivo = open('./objeto_posicao_02', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
if(contador_0==2):
    arquivo = open('./Arquivo_102_nome_objeto_0', 'r')
    conteudo = arquivo.readlines()
    arquivo = open('./objeto_posicao_03', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

#TESTE OBJETO 1
if(contador_1==0):
    arquivo = open('./Arquivo_103_nome_objeto_01', 'r')
    conteudo = arquivo.readlines()
    arquivo = open('./objeto_posicao_01', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
if(contador_1==1):
    arquivo = open('./Arquivo_103_nome_objeto_01', 'r')
    conteudo = arquivo.readlines()
    arquivo = open('./objeto_posicao_02', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
if(contador_1==2):
    arquivo = open('./Arquivo_103_nome_objeto_01', 'r')
    conteudo = arquivo.readlines()
    arquivo = open('./objeto_posicao_03', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

#TESTE OBJETO 2
if(contador_2==0):
    arquivo = open('./Arquivo_104_nome_objeto_02', 'r')
    conteudo = arquivo.readlines()
    arquivo = open('./objeto_posicao_01', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
if(contador_2==1):
    arquivo = open('./Arquivo_104_nome_objeto_02', 'r')
    conteudo = arquivo.readlines()
    arquivo = open('./objeto_posicao_02', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
if(contador_2==2):
    arquivo = open('./Arquivo_104_nome_objeto_02', 'r')
    conteudo = arquivo.readlines()
    arquivo = open('./objeto_posicao_03', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

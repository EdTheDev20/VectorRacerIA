
from fileinput import close
from pickle import TRUE
"""Leitura do ficheiro para definirmos o tamanho da matriz"""
f = open("track0.txt","r") # abrimos o ficheiro
nlinhas = 0
ncolunas = 0

while TRUE: #Condição para "rolar" até o break
    linha = f.readline() #leitura linha por linha
    if("\n"==linha): #Se tiver espaço na linha, fazemos a leitura de outra linha
        linha=f.readline()
    if(""==linha): #condição de paragem do ciclo, se for o fim do arquivo saímos do while
        break
    ncolunas= len(linha)
    nlinhas+=1
"""Leitura do ficheiro para definirmos o tamanho da matriz"""
matriz = []
f = close()
f = open("track0.txt","r")
while TRUE:
    linha = f.readline()
    matrizLinha = []
    if(""==linha):
        break
    for x in linha:
        if("\n"==x or ""==x):
            pass
        else:  
             matrizLinha.append(x)
        print(matrizLinha,end="")
        print()
    matriz.append(matrizLinha)


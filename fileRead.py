
from fileinput import close
from pickle import TRUE

f = open("track0.txt","r")
nlinhas = 0
ncolunas = 0
matriz = []
while TRUE: #Condição para "rolar" até o break
    linha = f.readline() #leitura linha por linha
    if("\n"==linha):
        linha=f.readline()
    if(""==linha): #condição de paragem do ciclo
        break
    ncolunas= len(linha)
    nlinhas+=1
    print(linha,end="") #print da linha
    
print(ncolunas) #ncolunas
print(nlinhas) #nlinhas
f = close()
f = open("track0.txt","r")
while TRUE:
    linha = f.readline()
    if(""==linha): #condição de paragem do ciclo
        break
    for i in range(nlinhas):
        mlinha = []
        for j in range(ncolunas):
            for x in linha:
                if(x!="\n"):
                    mlinha.append(x)
        matriz.append(mlinha)

print(len(matriz[0]))
print(len(matriz))
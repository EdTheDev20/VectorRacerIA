from pickle import TRUE
class Track:
    def __init__(self):
        self.size = [] #Tamanho da pista, contem uma lista com dois elementos. Ou seja, o número das linhas e o número das colunas da matriz.
        self.env #Uma lista de listas em que os obstáculos são representados por "NIL" e o espaço que pode ser percorrido é representado por "T"
        self.startpos = [] #Uma lista que representa a posição inicial. Ex: [linha-5,coluna-5]
        self.endpositions = []
        #Representada por uma lista de posições, ou seja, pode ser uma lista de listas com as respectivas posições da meta ou a finish line.
    
    def orderlistofcoordinates(): #Função que serve para comprarar estruturas do tipo track.
        pass 

    def readTrack(): #Função que serve para ler o ficheiro .txt e transformar em "env" ou "track".
        arqname= input("Caro usuário, insira o nome do arquivo:")
        f = open(arqname,"r")
        matriz = []
        while TRUE:
            linha = f.readline()
            if(""==linha):
                break
            mlinha = []
            for x in linha:
               if(x!="\n"):
                    mlinha.append(x)
            matriz.append(mlinha)
        return matriz

    def setSize(self,value): 
        self.size.append(value)

    def setStartPos(self,value):
        self.startpos.append(value)

    def setEndPositions(self,value):
        self.endpositions.append(value)
    
    def setEnv(self):
        self.env = Track.readTrack()
    
    
    

class State: #Estado do Carro
    def __init__(self):
        self.pos = [] #lista de dois elementos, ou seja: demonstra em que lugar está o carro
        self.vel = [] #lista de dois elementos que representa a velocidade atual do carro.
        self.action = [] #lista de dois elementos, é a ação que dá origem ao estado. Ou seja, é a nossa aceleração. Ex: se a velocidade for [5,2] e a aceleração for [1,1], na posição iremos usar o valor da linha atual e acrescentar [5+1] e na coluna vamos acrescentar [2+1],vamos deslocar [7,2]
        self.cost #Incógnita ainda, representa o custo da acção(ou aceleração) que originou a mudança de estado. ATT: custo da ação apenas e não o acúmulo dos custos
        self.track = [] #Uma lista de listas em que os obstáculos são representados por "NIL" e o espaço que pode ser percorrido é representado por "T"
        self.other #variável reserva.

class Problem:
    def __init__(self):
        self.initialState #estado inicial
        
    def nextStates(): #Uma função que aplicada a um estadogera uma lista com todos os estados que podem ser atingidos à partir desse
         pass

    def isGoal(): #Uma função que permite identificar um estado objectivo em que o jogo terminou
        pass

    def h(): #Uma função heurística que aplicada a um estado estima a distância desse estado ao objectivo mais próximo
        pass

def isObstaclep(pos,track): #Uma função que dada a uma posição e uma psta devolve o valor lógico T se existir um obstáculo na posição e NIL no caso contrário
    pass

def isGoalp(state): #Uma função que dado um estado devolve o valor lógico T se o estado for objectivo e NIL se não for
    pass

def nextState(state,action): #Uma função que dado um estado e uma ação devolve o estado que resulta de aplicar a ação ao estado fornecido, ou seja: vai apresentar a nossa próxima posição de acordo à nossa aceleração
    pass
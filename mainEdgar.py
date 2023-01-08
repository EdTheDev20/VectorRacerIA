# Grupo 3, membros: Edgar, Cleusia e Elber
from pickle import TRUE
import math
class Track:
    def __init__(self):
        self.size = []
        # Tamanho da pista, contem uma lista com dois elementos. Ou seja, o número das linhas e o número das colunas da matriz.
        self.env = []
        # Uma lista de listas em que os obstáculos são representados por "NIL" e o espaço que pode ser percorrido é representado por "T"
        self.startpos = []
        # Uma lista que representa a posição inicial. Ex: [linha-5,coluna-5]
        self.endpositions = []
        # Representada por uma lista de posições, ou seja, pode ser uma lista de listas com as respectivas posições da meta ou a finish line.

    def orderlistofcoordinates(self):  # Função que serve para comprarar estruturas do tipo track.
        pass

    def setEndPositions(self, matriz):
        self.endpositions.append(matriz)

    def setStartPos(self, *valores):
        for x in valores:
            self.size.append(x)

    def setSize(self, *valores):
        for x in valores:
            self.size.append(x)

    def startPista(self, file):

        Track.setEnv(self, file)
        "Damos o tamanho da pista"
        Track.setSize(self, len(self.env))
        Track.setSize(self, len(self.env[0]))
        "Damos o tamanho da pista"
        for i in range(len(self.env)):
            for j in range(len(self.env[0])):
                linha = []
                if (self.env[i][j] == "E"):
                    linha.append(i)
                    linha.append(j)
                    self.setEndPositions(linha)
                if (self.env[i][j] == "S"):
                    self.setStartPos(i)
                    self.setStartPos(j)

    def readTrack(self, file):
        # Função que serve para ler o ficheiro .txt e transformar em "env" ou "track".
        f = open(file, "r")
        matriz = []
        while TRUE:
            linha = f.readline()
            if "" == linha:
                break
            mlinha = []
            for x in linha:
                if x != "\n":
                    mlinha.append(x)
            matriz.append(mlinha)

        return matriz

    def setSize(self, value):
        self.size.append(value)

    def setStartPos(self, value):
        self.startpos.append(value)

    def setEndPositions(self, value):
        self.endpositions.append(value)

    def setEnv(self, file):
        self.env = Track.readTrack(self, file)

    def printEnv(self):
        for i in range(len(self.env)):
            for j in range(len(self.env[0])):
                print(self.env[i][j], end="")
            print()


class State:  # Estado do Carro
    def __init__(self):
        self.pos = []  # lista de dois elementos, ou seja: demonstra em que lugar está o carro
        self.vel = []  # lista de dois elementos que representa a velocidade atual do carro.
        self.action = []  # lista de dois elementos, é a ação que dá origem ao novo estado. Ou seja, é a nossa aceleração
        self.cost = 0  # Incógnita ainda, representa o custo da acção(ou aceleração) que originou a mudança de estado. ATT: custo da ação apenas e não o acúmulo dos custos
        self.track = []  # Uma lista de listas em que os obstáculos são representados por "X" e o espaço que pode ser percorrido é representado por "O"
        self.heuristic = None
        self.f = 0
        self.g = 0


def make_state(pos, vel, action, cost,
               track):  # função que cria um estado, a função apenas recebe os parâmetros do estado, cria o objecto e atribui as propriedades
    state = State()
    state.pos = pos
    state.vel = vel
    state.action = action
    state.cost = cost
    state.track = track

    return state


class Problem:
    def __init__(self):
        self.initialState  # estado inicial

    def h(self):  # Uma função heurística que aplicada a um estado estima a distância desse estado ao objectivo mais próximo
        pass


def isObstaclep(pos,
                track):  # Uma função que dada a uma posição e uma pista devolve o valor lógico T se existir um obstáculo na posição e NIL no caso contrário

    for i in range(len(track.env)):
        for j in range(len(track.env[0])):

            aux = [i, j]  # auxiliar para comparação entre a posição dada e as posições da pista

            if pos[0] == aux[0] and pos[1] == aux[1]:  # se a posição dada for igual a posição da pista
                if track.env[i][j] == 'X':  # se na posição tiver um 'X' então é um obstáculo, retorna 'T'
                    return True

    return False


def isGoalp(state :State):  # Uma função que dado um estado devolve o valor lógico T se o estado for objectivo e NIL se não for

    for i in state.track.endpositions:  # procura na lista de posições finais o estado em que o carro está nesse momento

        if state.pos[0] == i[0] and state.pos[1] == i[1]:  ##se uma das posições estiver na lista, retorna T
            return True

    return False


def nextState(state,
              action):  # Uma função que dado um estado e uma ação devolve o estado que resulta de aplicar a ação ao estado fornecido, ou seja: vai apresentar a nossa próxima posição de acordo à nossa aceleração

    contingency = [state.pos[0], state.pos[1]]  # contingência para o caso de bater num obstáculo
    state.action = action  # o estado recebe a nova ação

    # conversão de tupla para listas para calcular as novas posições
    vel = list(state.vel)
    pos = list(state.pos)

    vel[0] = vel[0] + action[0]
    vel[1] = vel[1] + action[1]

    pos[0] = pos[0] + vel[0]
    pos[1] = pos[1] + vel[1]

    # conversão de volta para listas
    state.vel = tuple(vel)
    state.pos = tuple(pos)

    if isObstaclep(state.pos, state.track) == True:  # se a nova posição for um obstáculo
        # volta para a posição anterior ou contingência
        state.pos = contingency
        state.vel = [0, 0]  # a velocidade é 0
        state.cost = 20  # o custo é 20

    elif isGoalp(state) == True:  # se a nova posição for um objectivo
        state.cost = -100  # o custo é -100
    else:
        state.cost = 1  # senão, é um estado normal, e o custo é 1

    return state


def loadTrack(file):
    t = Track()
    t.startPista(file)
    return t


def state_to_str(state):  # Função que transforma um estado em string
    print("Pos: " + str(state.pos) + " Vel: " + str(state.vel) + " Action: " + str(state.action) + " Cost: " + str(
        state.cost))

def nextStates(state):  # Uma função que dado um estado, devolve uma lista dos estados seguintes possíveis

    actions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    copy = state
    estados = []


    for j in range(len(actions)):
        state = copy
        action = actions[j]

        # conversão de tupla para listas para calcular as novas posições
        vel = list(state.vel)
        pos = list(state.pos)

        vel[0] = vel[0] + action[0]
        vel[1] = vel[1] + action[1]

        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]


        if isObstaclep(tuple(pos), state.track) == False:
            estados.append(tuple(pos))


    return estados

def abs(value):
    if (value < 0):
        value *= -1

    return value
def Busca(estadoInicial:State,maxDepth:int):
    def DFS(estadoInicial:State,maxDepth:int):
        print("Verificando um destino:",estadoInicial)
        if(isGoalp(estadoInicial)):
            return True
        if(maxDepth<=0):
            return False
        estadosFilhos = nextStates(estadoInicial)
        for filho in estadosFilhos:
            if DFS(filho,(maxDepth-1)):
                return True
        return False   

    def DDFS(estadoInicial:State,maxDepth:int):
        for i in (maxDepth):
            if DFS(estadoInicial,i):
                return True
        return False
    
    if not DDFS(estadoInicial,maxDepth):
        print("um caminho existe")
    else:
        print("um caminho n existe")

def compute_heuristic(state):
    copyH = 900

    if (state.track.env[state.pos[0]][state.pos[1]] == "X"):
        h = '<M>'
    elif (state.track.env[state.pos[0]][state.pos[1]] == "E"):
        h = 0
    else:
        # para vários pontos de chegada, calcular e depois ir verificando a medida que se calcula qual é o menor
        for x in range(len(state.track.endpositions)):
            h = abs(state.pos[0] - state.track.endpositions[x][0]) + abs(state.pos[1] - state.track.endpositions[x][1])
            h = math.sqrt(
                math.pow(state.pos[0] - state.track.endpositions[x][0], 2) + math.pow(
                    state.pos[1] - state.track.endpositions[x][1],
                    2))
            if (h < copyH):
                copyH = h
            else:
                h = copyH

            h = int(h)

    return h


#---------------------------------------------------------------------------------------------#

track = loadTrack("track0.txt")
StateInicial = make_state(track.startpos, (0,1), 'nil', 0, track)
action = (1, -1)
# pos, vel, action, cost, track
prev_goal_state = make_state((2,13), (0,4), (1,1), 1, track)


goal_state = make_state((3,16), (1,3), (1,-1), -100, track)
goal_state1 = make_state((4,16), (1,3), (1,-1), -100, track)

non_goal_state = make_state((3,6), (-1,2), (-1,0), 1, track)
non_goal_state1 = make_state((5,7), (-1,2), (-1,0), 1, track)

obstacle = (2,2)
obstacle1 = (1,2)
obstacle2 = (6,16)

non_obstacle = (2,8)
non_obstacle1 = (3,3)
non_obstacle2 = (2,10)

#===================================================================================================
print("Exercise 1.1 - isObstaclep")
isObstaclep(obstacle, track)
isObstaclep(obstacle1, track)
isObstaclep(obstacle2, track)

isObstaclep(non_obstacle, track)
isObstaclep(non_obstacle1, track)
isObstaclep(non_obstacle2, track)
#===================================================================================================

print("Exercise 1.2 - isGoalp")
print(isGoalp(goal_state))
isGoalp(goal_state1)

print(isGoalp(non_goal_state))
isGoalp(non_goal_state1)

#===============================================================================
print("Exercise 1.3 - nextState")
state_to_str(nextState(prev_goal_state, action))
state_to_str(nextState(StateInicial, action))

#NOTA: state_to_str(st) e o returno "Pos: Vel: Action: Cost:"


#================================================================================
print("----------------------------TESTING--------------------")
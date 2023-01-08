
def Busca(estadoInicial:State,maxDepth): 
    def DFS(estadoInicial:State,maxDepth):
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

    def DDFS(estadoInicial:State,maxDepth):
        for i in range(maxDepth):
            if DFS(estadoInicial,i):
                return True
        return False
    
    if not DDFS(estadoInicial,maxDepth):
        print("um caminho existe")
    else:
        print("um caminho n existe")


#Rules

tab = [] #tabuleiro
possibleMove = [] # tabuleiro que só deve conter as bolinhas cinzas dos movimentos (orientacao pra view)

def createTab(): #cria um tabuleiro 8x8 
    global tab
    global possibleMove
    j = 0

    while j < 8:
        tab.append([])
        i = 0
        while i < 8:
            tab[j].append('')
            i+=1
        j+=1
    
    possibleMove = tab
    initTab(tab)
    return tab

def initTab(tab): #Posições iniciais

    backline = ['R','C','B','Q','K','B','C','R']
    #White
        #White Pawn
    for el in tab[1]:
        el = 'WP2'

        #White backline

    i = 0
    while i < len(tab[0]):
        tab[0][i] = 'W' + backline[i]
        i+=1

    #Black
        #Black Pawn
    for el in tab[6]:
        el = 'BP2'


        #Black backline
    i = 0
    while i < len(tab[0]):
        tab[7][i] = 'B' + backline[i]
        i+=1

    return tab

def createCMD(): #dicionário para futura command line
    diccio = {}
    letters = ['A','B','C','D','E','F','G','H']
    i = 0

    while i < 8:
        j = 0
        while j < 8:
            diccio[letters[i] + str(j+1)] = [i,j]
            j+=1
        i+=1
    return diccio

def validTile(pos): #ve oq tem naquele tile e valida seu movimento
    global tab
    if(pos[0] < 8):
        if(pos[1] < 8):
            if(tab[pos[0]][pos[1]] != ''):
                return 3 #nenhuma peça nessa posição
            elif('B' in tab[pos[0]][pos[1]]):
                return 2 #peça preta nesta posição
            elif('W' in tab[pos[0]][pos[1]]):
                return 1 #peça branca nesta posição
    else:
        return 0 #movimento invalido

def clearTracing(): #limpa a lista de tracing para a próxima peça
    global possibleMove
    for sublist in possibleMove:
        for el in sublist:
            el = ''
    return

def pawnTracing(initPos): #calcula o tracing do peao
    global tab
    global possibleMove
    i = 1
    initPos = [initPos[0] + i,initPos[1] + i] # offset para os movimentos do peao, ja que ele nao deve ter a opcao de se mover para a própria initPos

    while i <= 2:
        if(validTile(initPos) == 3):
            possibleMove[initPos[0]][initPos[1]] = 'x'  #isso tb
        else:
            break
        i+=1


def columnTracing(initPos): #tracing do movimento da torre
    global tab
    global possibleMove
    #preciso fazer o tracing das 4 direções de forma independente, se não tem o risco de quando limitar 1 limitar todos
    
    i = 1 #step

    north = [initPos[0] ,initPos[1] + i]
    west = [initPos[0] - i,initPos[1]] 
    east = [initPos[0] + i ,initPos[1]]
    south = [initPos[0] ,initPos[1] - i]

    #North tracing
    while north[1] < 8:
        possibleMove[north[0]][north[1]] = 'x'
        north = [north[0],north[1] + i]

    #South tracing
    while south[1] > -1:
        possibleMove[south[0]][south[1]] = 'x'
        south = [south[0],south[1] - i]
    
    #East tracing
    while east[0] < 8:
        possibleMove[east[0]][east[1]] = 'x'
        east = [east[0] + i][east[1]]
    
    #West tracing
    while west > -1:
        possibleMove[west[0]][west[1]] = 'x'
        west = [west[0]-i][west[1]]

    

def diagonalTracing(initPos): #tracing do movimento do bispo
    global tab
    global possibleMove

    i = 1 #step

    NW = [initPos[0] - i, initPos[1] + i]
    NE = [initPos[0] + i, initPos[1] + i]
    SW = [initPos[0] - i, initPos[1] - i]
    SE = [initPos[0] + i, initPos[1] - i]

    #NE tracing
    while NE[0] < 8 and NE[1] < 8:
        possibleMove[NE[0]][NE[1]] = 'x'
        NE = [NE[0] +i, NE[1] +i]

    #SW tracing
    while SW[0] > -1 and SW[1] > -1:
        possibleMove[SW[0]][SW[1]] = 'x'
        SW = [SW[0] -i, SW[1] -i]

    #NW tracing
    while NW[0] > -1 and NW[1] < 8:
        possibleMove[NW[0]][NW[1]] = 'x'
        NW = [NW[0] -i, NW[1] +i]
    #SE tracing
    while SE[0] < 8 and SE[1] > -1 :
        possibleMove[SE[0]][SE[1]] = 'x'
        SE = [SE[0] +i, SE[1] -i]
    return

def kingTracing(initPos):

    return
#Rules

def createTab(): #cria um tabuleiro 8x8 
    tab = []
    j = 0

    while j < 8:
        tab.append([])
        i = 0
        while i < 8:
            tab[j].append('')
            i+=1
        j+=1
    
    initTab(tab)
    return tab

def initTab(tab): #Posições iniciais

    backline = ['R','C','B','Q','K','B','C','R']
    #White
        #White Pawn
    for el in tab[1]:
        el = 'WP'

        #White backline

    i = 0
    while i < len(tab[0]):
        tab[0][i] = 'W' + backline[i]
        i+=1

    #Black
        #Black Pawn
    for el in tab[6]:
        el = 'BP'


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


import math 
import copy

def gameWinning(state,playerX):
    horizontal=False
    vertical=False
    previous1=0
    previous2=0
    for i in range(3):#check for horizontal and vertical winning states
      
            previous1=state[i][0]#first element for horizontal
            previous2=state[0][i]#first element for vertical
            horizontal=True
            vertical=True

            for f in range(3):
                if state[i][f]!=previous1:#check horizontal tiles if all are the same
                    horizontal=False
                if state[f][i]!=previous2:#check vertical tiles if all are the same
                    vertical=False

                previous=state[i][f]
                previous2=state[f][i]  
 
            if horizontal==True and previous1!=' ':#check if blank
                break
            if vertical==True and previous2!=' ':
                break
    
    diagonal=False #check diagonal
    if state[1][1]==state[0][0] and state[1][1]==state[2][2]:
        diagonal=True
    if state[1][1]==state[0][2] and state[1][1]==state[2][0]:
        diagonal=True

    if diagonal==True:# RETURN VALUES
        if state[1][1]=='X':
            return 1

        elif state[1][1]=='O':
            return (-1)


    if(horizontal==True):
        if previous1=='X':
            return 1

        elif previous1=='O':
            return (-1)



    if(vertical==True):
        if previous2=='X':
            return 1


        elif previous2=='O':
            return (-1)

    over=True
    for row in state:
        if row.count(' ')!=0:
            over=False
            break
    if(over==True):
        return 0 #Draw


def successorStates(state, playerX):
    successorList=[]

    for i in range(3):
        for j in range(3):
            if state[i][j]==' ':
      
                newState = copy.deepcopy(state)

                if(playerX==1):
                    newState[i][j]='O'#CPU is 0
                else:
                    newState[i][j]='X'
                successorList.append(newState)
               
    return successorList

def max(a,b):
    if(a>b):
        return a
    return b
def min(a,b):
    if(a<b):
        return a
    return b

    
def minMax(state, playerX, alpha, beta, depth):

    print("--State--   alpha: "+str(alpha)+", beta: "+str(beta)+" Depth: "+str(depth))
    for row in state:
        print(row)

    u = gameWinning(state,playerX)
    if u==1 or u==0 or u==(-1):#1 means X wins, -1 means O, 0 for draw
        if u==1:
            return 1,state
        elif u==(-1):
            return -1,state
        else: 
            return 0,state

    childState=successorStates(state, playerX)


    if playerX==0:#CPU is X, maximizing
        m = -math.inf 
        bestState = state
        # print("Max")
        for i in range(len(childState)):
            val, currentState=minMax(childState[i],1,alpha,beta,depth+1)
            if(val>m):
                bestState = childState[i]
            m = max(val, m)
            alpha = max(m, alpha)           

            if alpha>=beta:
                print("Break")
                break
            
        return m, bestState

    else:#CPU is O
        m = math.inf 
        bestState = state
        # print("Min")
        for i in range(len(childState)):
            val, currentState=minMax(childState[i],0,alpha,beta,depth+1)
            if(val<m):
                bestState = childState[i]
            m= min(val, m)  
            beta = min(m, beta)     
  
            if beta<=alpha:
                print("Break")
                break
            
                


        return m, bestState

alpha = -math.inf 
beta = math.inf 



# puzzleArr=[
# [' ','O',' '],
# [' ',' ','X'],
# ['X',' ',' ']]

# playerX=1
# ideal=minMax(puzzleArr,playerX,alpha,beta, 0)
# print("-----IDEAL STATE-----")
# for row in ideal[1]:
#     print(row)

squareIndex=0

puzzleArr=[
['O','O',' '],
[' ','X',' '],
['X',' ',' ']]
newState=[
3,    
[
    ['O','O','X'],
    [' ','X',' '],
    ['X',' ',' ']
]

]

squareindex=0
for f in range(3):
    for j in range(3):
        if puzzleArr[f][j]!=newState[1][f][j]:
            break
        squareindex+=1

print(f)
print(j)

# board = [
# [' ',' ',' '],
# [' ',' ',' '],
# [' ',' ',' ']]
# playerFirst=0
# playerX=1
# while True:
#     print("---BOARD---")
#     for row in board:
#         print(row)
#     win = gameWinning(board, playerX)
#     if(win==1 or win==-1 or win==0):
#         if (win==1 and playerX==0):
#             print("CPU wins")
#         elif (win==-1 and playerX==0):
#             print("CPU wins")
#         print("Game over")
#         break
#     if(playerFirst==1):
#         playerFirst=0
#         indexA=int(input("X: "))
#         indexB=int(input("Y: "))
#         if playerX==0:
#             board[indexA][indexB]='O'
#         else:
#             board[indexA][indexB]='X'

#     else:
#         playerFirst=1
#         ideal=minMax(board,playerX,alpha,beta, 0)
#         board = ideal[1]




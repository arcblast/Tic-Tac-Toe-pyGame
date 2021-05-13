import pygame
import random
import math 
import copy


from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    QUIT
)

puzzleArr=[]

for i in range(3):
    puzzleArr.append([' ',' ',' '])

for row in puzzleArr:
    print(row)


class Square(pygame.sprite.Sprite): 
    def __init__(self, content, indexA, indexB):
        super(Square, self).__init__()

        self.image = pygame.image.load("black.png")

        self.surf = pygame.transform.scale(self.image,(75,75))
        pygame.transform.scale(self.surf, (75,75))
        self.indexA=indexA
        self.indexB=indexB
        self.rect = self.surf.get_rect()
        self.rect.x = indexB*80+130 #SET SPAWN POINT
        self.rect.y = indexA*80+80 #
        self.content = content

    def reset(self):#for game reset
        self.image = pygame.image.load("black.png")
        self.surf = pygame.transform.scale(self.image,(75,75))
        pygame.transform.scale(self.surf, (75,75))
        self.content = ' '

    def clicked(self, playerX,listSquare,puzzleArr):


        if playerX:#FILL EMPTY SQUARE
            self.content='X'
            self.image = pygame.image.load("X.png")
            self.surf = pygame.transform.scale(self.image,(75,75))
            puzzleArr[self.indexA][self.indexB]='X'
            pygame.transform.scale(self.surf, (75,75))

        else:
            self.content='O'
            self.image = pygame.image.load("O.png")
            self.surf = pygame.transform.scale(self.image,(75,75))
            pygame.transform.scale(self.surf, (75,75))
            puzzleArr[self.indexA][self.indexB]='O'

        u=gameWinning(puzzleArr, playerX)

        if(u==1):
            print("X wins")
            return u
        elif(u==-1):
            print("O wins")
            return u
        elif(u==0):
            print("Draw")
            return u



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

    if diagonal==True:# RETURN VALUES,1 if X wins, -1 if O wins, 0 if draw
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
        return 0 #Draw#Returns 1 if X wins, -1 if O wins, 0 if draw


def successorStates(state, playerX):#returns list of possible moves for X or O
    successorList=[]

    for i in range(3):
        for j in range(3):
            if state[i][j]==' ':
                newState = copy.deepcopy(state)
                if(playerX==1):
                    newState[i][j]='O'
                else:
                    newState[i][j]='X'
                successorList.append(newState)

    return successorList


def minMax(state, playerX, alpha, beta, depth):


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

            if beta<=alpha:
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
                break


        return m, bestState

  
# Defining a negative infinite integer 


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


pygame.init()
pygame.font.init()
squares = pygame.sprite.Group()

for i in range( len(puzzleArr) ):
    for j in range(len(puzzleArr[i])):
        squares.add(Square(puzzleArr[i][j], i, j)) #add box with array index and value

pygame.display.set_caption('TIC TAC TOE')
font = pygame.font.SysFont('Comic Sans MS',30)



listSquare = squares.sprites()  #for accessing


#TEXT BOXES
text=font.render("Click on an empty tile", False, (0,126,0),(126,126,125))  #TEXT BUTTONS
textRect = text.get_rect()  
textRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2+100) 

font1 = pygame.font.SysFont('Comic Sans MS',55)
text1=font1.render("Choose a side", False, (0,126,0)) 
textRect1 = text1.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2-75))  

font2 = pygame.font.SysFont('Comic Sans MS',50)
text2=font2.render(" O ", False, (126,126,0)) 
textRect2 = text2.get_rect(center=(SCREEN_WIDTH//2+30, SCREEN_HEIGHT//2-20))  

text3=font2.render(" X ", False, (126,126,0), (0,0,128))
textRect3 = text3.get_rect(center=(SCREEN_WIDTH//2-30, SCREEN_HEIGHT//2-20))  

text4=font1.render("Go first?", False, (0,126,0)) 
textRect4 = text4.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+40))  
font3 = pygame.font.SysFont('Comic Sans MS',45)

text5=font3.render("YES", False, (126,126,0), (0,0,128) ) 
textRect5 = text2.get_rect(center=(SCREEN_WIDTH//2-40, SCREEN_HEIGHT//2+95))  

text6=font3.render("NO", False, (126,126,0) ) 
textRect6 = text3.get_rect(center=(SCREEN_WIDTH//2+40, SCREEN_HEIGHT//2+95))  
 
text7=font2.render("START", False, (126,0,126),(0,128,128) ) 
textRect7 = text7.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+150))  


running = True  
start = True
playerFirst=1
playerX=1

gameOver=False
def gameIntro():   
    screen.blit(text1,textRect1)
    screen.blit(text2,textRect2)   
    screen.blit(text3,textRect3)
    screen.blit(text4,textRect4)
    screen.blit(text5,textRect5)
    screen.blit(text6,textRect6)
    screen.blit(text7,textRect7)


while running:#PYGAME LOOP

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            if textRect2.collidepoint(event.pos) and start and not gameOver:#LOG IN SCREEN
                print("PLAYER CHOSE O")
                playerX=0
                text2=font2.render(" O ", False, (126,126,0),(0,0,128)) 
                text3=font2.render(" X ", False, (126,126,0))  
            if textRect.collidepoint(event.pos) and gameOver:#LOG IN SCREEN
                print("NEW GAME")
                puzzleArr=[#RESET TILES
                [' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']
                ]
                pygame.time.wait(100)
                for square in listSquare:#RESET TILE SPRITE
                    square.reset()
                start=True
                gameOver=False


            elif textRect3.collidepoint(event.pos) and start and not gameOver:
                print("PLAYER CHOSE X")
                playerX=1
                text2=font2.render(" O ", False, (126,126,0)) 
                text3=font2.render(" X ", False, (126,126,0), (0,0,128)) 
            elif textRect5.collidepoint(event.pos) and start and not gameOver:
                print("PLAYER GOES FIRST")
                playerFirst=1
                text5=font3.render("YES", False, (126,126,0),(0,0,128) ) 
                text6=font3.render("NO", False, (126,126,0), ) 
            elif textRect6.collidepoint(event.pos) and start and not gameOver:
                print("PLAYER GOES LAST")
                playerFirst=0
                text5=font3.render("YES", False, (126,126,0), ) 
                text6=font3.render("NO", False, (126,126,0), (0,0,128)) 
            elif textRect7.collidepoint(event.pos) and start and not gameOver:
                start=False
                print("START")

            for i in range(len(listSquare)):
                if listSquare[i].rect.collidepoint(event.pos) and playerFirst==1 and not start and not gameOver:
                    if listSquare[i].content!=' ':
                        print("Square is occupied!")

                    else:
                        u=listSquare[i].clicked(playerX,listSquare,puzzleArr)
                        
                        if u==1 or u==-1 or u==0:#check if board full
                            gameOver=True

                        playerFirst=0#CPU turn
                        break


    if playerFirst==0 and not start and not gameOver:#CPU turn
        print("CPU turn")

        newState=minMax(puzzleArr, playerX,-math.inf,math.inf,0)#Get ideal position state


        indexA=0
        indexB=0
        for f in range(3):#check which box need to be updated between current state and ideal state
            for j in range(3):
                if puzzleArr[f][j]!=newState[1][f][j]:
                    indexA=f
                    indexB=j
                    break

            
        for box in listSquare:#Find the box in the sprite list
            if(box.indexA==indexA and box.indexB==indexB):
                if(playerX==1):#Update sprite
                    u=box.clicked(0,listSquare,puzzleArr)

                    break
                else:
                    u=box.clicked(1,listSquare,puzzleArr)

                    break
        if u==1 or u==-1 or u==0:#check if board full
            gameOver=True

        playerFirst=1#Player turn
    


    screen.fill((0, 0, 0))#BG Color BLACK


    if start:
        gameIntro() #ASK USER FOR OPTIONS
    elif not start: 

        for square in squares:  #Draw squares
            screen.blit(square.surf,square.rect) 
            text=font.render("Click on an empty square", False, (0,126,0))  #TEXT BUTTONS


        if gameOver==True:
            text=font.render("TRY AGAIN?", False, (0,126,0), (126,0,0))


        screen.blit(text,textRect)#instructions




    pygame.display.flip()


pygame.quit()
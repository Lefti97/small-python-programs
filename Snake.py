# snakeDir is not assigned in main

import pygame
import random

FPS = 10

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

xSize = 20
ySize = 20

dispMult = 20
xDisplay = xSize * dispMult
yDisplay = ySize * dispMult

gameDisplay = pygame.display.set_mode((xDisplay,yDisplay + dispMult*2))

snakeList = [[random.randrange(5, ySize - 6), random.randrange(5, xSize - 6)]]

snakeDir = [random.choice("udlr")]  # 1 = up, 2 = down, 3 = left, 4 = right
score = [0]
gameExit = [False]
gameOver = [False]

map = []

def randItem():
    empty = False
    while(empty == False):
        tmp = [random.randrange(5, ySize - 6), random.randrange(5, xSize - 6)]
        if map[tmp[0]][tmp[1]] == ' ':
            empty = True
            map[tmp[0]][tmp[1]] = 'I'


def initMap():
    map.clear()
    for y in range(ySize):
        tmp = []
        if (y != 0) and (y != ySize-1):
            tmp = list("".ljust(xSize, ' '))
            tmp[0] = '*'
            tmp[len(tmp)-1] = '*'
        else:
            tmp = list("".ljust(xSize, '*'))
        map.append(tmp)
    
    map[snakeList[0][0]][snakeList[0][1]] = 'X'
    

    if snakeDir[0] == 'u': # UP
        for i in range(1,5):
            map[snakeList[0][0]+i][snakeList[0][1]] = 'O'
            snakeList.append([snakeList[0][0]+i, snakeList[0][1]])
    elif snakeDir[0] == 'd': # DOWN
        for i in range(1,5):
            map[snakeList[0][0]-i][snakeList[0][1]] = 'O'
            snakeList.append([snakeList[0][0]-i, snakeList[0][1]])
    elif snakeDir[0] == 'l': # LEFT
        for i in range(1,5):
            map[snakeList[0][0]][snakeList[0][1]+i] = 'O'
            snakeList.append([snakeList[0][0], snakeList[0][1]+i])
    elif snakeDir[0] == 'r': # RIGHT
        for i in range(1,5):
            map[snakeList[0][0]][snakeList[0][1]-i] = 'O'
            snakeList.append([snakeList[0][0], snakeList[0][1]-i])

    randItem()


def drawMap():
    for y in range(ySize):
        for x in range(xSize):
            if   map[y][x] == '*':
                pygame.draw.rect(gameDisplay, BLUE, [x * dispMult , y * dispMult, dispMult, dispMult])
            elif map[y][x] == ' ':
                pygame.draw.rect(gameDisplay, BLACK, [x * dispMult , y * dispMult, dispMult, dispMult])
            elif map[y][x] == 'X':
                pygame.draw.rect(gameDisplay, RED, [x * dispMult , y * dispMult, dispMult, dispMult])
            elif map[y][x] == 'O':
                pygame.draw.rect(gameDisplay, GREEN, [x * dispMult , y * dispMult, dispMult, dispMult])
            elif map[y][x] == 'I':
                pygame.draw.rect(gameDisplay, YELLOW, [x * dispMult , y * dispMult, dispMult, dispMult])
            elif map[y][x] == 'x':
                pygame.draw.rect(gameDisplay, WHITE, [x * dispMult , y * dispMult, dispMult, dispMult])
            pygame.draw.rect(gameDisplay, GRAY, [x * dispMult , y * dispMult, dispMult, dispMult], 1)  


def gameUpdate():
    oldTail = list(snakeList[-1])

    map[snakeList[-1][0]][snakeList[-1][1]] = ' '
    snakeList[-1] = list(snakeList[0])
    snakeList.insert(1,snakeList.pop())
    map[snakeList[1][0]][snakeList[1][1]] = 'O'

    if snakeDir[0] == 'u':
        snakeList[0][0] -= 1
    elif snakeDir[0] == 'd':
        snakeList[0][0] += 1
    elif snakeDir[0] == 'l':
        snakeList[0][1] -= 1
    elif snakeDir[0] == 'r':
        snakeList[0][1] += 1


    if map[snakeList[0][0]][snakeList[0][1]] == 'I':
        snakeList.append(oldTail)
        map[snakeList[-1][0]][snakeList[-1][1]] = 'O'
        map[snakeList[0][0]][snakeList[0][1]] = 'X'
        randItem()
        score[0] += 10
    elif map[snakeList[0][0]][snakeList[0][1]] == ' ':
        map[snakeList[0][0]][snakeList[0][1]] = 'X'
    else:
        map[snakeList[0][0]][snakeList[0][1]] = 'x'
        gameOver[0] = True


def main(): 
    initMap()

    pygame.init()

    font = pygame.font.SysFont(None, 40)
    font2 = pygame.font.SysFont(None, 80)

    while not gameExit[0]:
        
        if gameOver[0] == False:
            gameUpdate()

        keyPress = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if keyPress == False:
                    if (event.key == pygame.K_UP) and (snakeDir[0] != 'd'):
                        snakeDir[0] = 'u'
                        keyPress = True
                    elif (event.key == pygame.K_DOWN) and (snakeDir[0] != 'u'):
                        snakeDir[0] = 'd'
                        keyPress = True
                    elif (event.key == pygame.K_LEFT) and (snakeDir[0] != 'r'):
                        snakeDir[0] = 'l'
                        keyPress = True
                    elif (event.key == pygame.K_RIGHT) and (snakeDir[0] != 'l'):
                        snakeDir[0] = 'r'
                        keyPress = True
        
        
        
        gameDisplay.fill(BLACK)
        drawMap()

        text = font.render('Score: ' + str(score[0]), True, WHITE)
        gameDisplay.blit(text, (dispMult , yDisplay+5))

        if gameOver[0]:
            text2 = font2.render('GAME OVER', True, WHITE)
            gameDisplay.blit(text2, (dispMult , yDisplay/3))

        pygame.display.update()
        clock.tick(FPS)
        



if __name__ == "__main__":
    main()

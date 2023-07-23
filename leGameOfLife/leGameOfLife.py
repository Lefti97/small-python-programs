import pygame

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
GRAY2 = (90, 90, 90)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

pygame.display.set_caption('leGameOfLife')
clock = pygame.time.Clock()

pausedFPS = 60
unpausedFPS = 4

# Grid Size
xSize = 100
ySize = 60

dispMult = 15 # Cell display size
xDisplay = xSize * dispMult
yDisplay = ySize * dispMult
gameDisplay = pygame.display.set_mode((xDisplay,yDisplay + 25))

LIVE = True
DEAD = False

map = []

def initMap():
    map.clear()
    for y in range(ySize):
        tmp = []
        for x in range(xSize):
            tmp.append(DEAD)
        map.append(tmp)

def drawMap():
    for y in range(ySize):
        for x in range(xSize):
            if   map[y][x] == LIVE:
                pygame.draw.rect(gameDisplay, YELLOW, [x * dispMult , y * dispMult, dispMult, dispMult])
            elif map[y][x] == DEAD:
                pygame.draw.rect(gameDisplay, GRAY2, [x * dispMult , y * dispMult, dispMult, dispMult])
            pygame.draw.rect(gameDisplay, GRAY, [x * dispMult , y * dispMult, dispMult, dispMult], 1)  

def getNeighbours(y, x):
    neighbours = 0

    if(y != 0)         and                      (map[y-1][x] == LIVE): # TOP
        neighbours += 1
    if(y != 0)         and (x != (xSize-1)) and (map[y-1][x+1] == LIVE): # TOP RIGHT
        neighbours += 1
    if(x != (xSize-1)) and                      (map[y][x+1] == LIVE): # RIGHT
        neighbours += 1
    if(y != (ySize-1)) and (x != (xSize-1)) and (map[y+1][x+1] == LIVE): # BOTTOM RIGHT
        neighbours += 1
    if(y != (ySize-1)) and                      (map[y+1][x] == LIVE): # BOTTOM
        neighbours += 1     
    if(y != (ySize-1)) and (x != 0)         and (map[y+1][x-1] == LIVE): # BOTTOM LEFT
        neighbours += 1     
    if(x != 0)         and                      (map[y][x-1] == LIVE): # LEFT
        neighbours += 1             
    if(y != 0)         and (x != 0)         and (map[y-1][x-1] == LIVE): # TOP LEFT
        neighbours += 1     
    
    return neighbours

def gameUpdate():
    neighboursMap = []

    for y in range(ySize):
        neighboursMap.append([])
        for x in range(xSize):
            neighboursMap[y].append(getNeighbours(y, x))
    
    for y in range(ySize):
        for x in range(xSize):
            if   (map[y][x] == LIVE) and (neighboursMap[y][x] != 2) and (neighboursMap[y][x] != 3):
                map[y][x] = DEAD
            elif (map[y][x] == DEAD) and (neighboursMap[y][x] == 3):
                map[y][x] = LIVE

def changeCell(mouseY, mouseX):
    curY = mouseY // dispMult
    curX = mouseX // dispMult
    map[curY][curX] = not map[curY][curX]

def main(): 
    pygame.init()
    initMap()
    PAUSE = True
    font = pygame.font.SysFont(None, 25)
    text = font.render('Left Click: Flip Cell , R: Reset Grid , N: Next State , SPACE: Un/Pause , ESC: Exit , PAUSED', True, WHITE)
    PLAYING = True

    while PLAYING == True:
        gameDisplay.fill(BLACK)
        drawMap()
        gameDisplay.blit(text, (10 , yDisplay + dispMult/2))
        buttonPress = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if buttonPress == False:
                    if (event.key == pygame.K_SPACE):
                        PAUSE = not PAUSE
                        buttonPress = True
                        if PAUSE == True:
                            text = font.render('Left Click: Flip Cell , R: Reset Grid , N: Next State , SPACE: Un/Pause , ESC: Exit , PAUSED', True, WHITE)
                        else:
                            text = font.render('Left Click: Flip Cell , R: Reset Grid , N: Next State , SPACE: Un/Pause , ESC: Exit , UNPAUSED', True, WHITE)
                    elif (event.key == pygame.K_r):
                        text = font.render('Left Click: Flip Cell , R: Reset Grid , N: Next State , SPACE: Un/Pause , ESC: Exit , PAUSED', True, WHITE)
                        initMap()
                        PAUSE = True
                        buttonPress = True
                    elif (event.key == pygame.K_n) and (PAUSE == True):
                        gameUpdate()
                        buttonPress = True
                    elif (event.key == pygame.K_ESCAPE):
                        PLAYING = False
            if event.type == pygame.MOUSEBUTTONUP:
                if buttonPress == False:
                    if (event.button == 1):
                        buttonPress = True
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if (mouseY // dispMult) < ySize:
                            changeCell(mouseY, mouseX)

        if PAUSE == True:
            clock.tick(pausedFPS)
        else:
            gameUpdate()
            clock.tick(unpausedFPS)
        pygame.display.update()

if __name__ == "__main__":
    main()
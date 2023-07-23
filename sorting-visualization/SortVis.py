import pygame
import random

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.display.set_caption('Algorithm Visualization')
clock = pygame.time.Clock()

FPS = 100

arrSize = 100

xSize = arrSize
ySize = xSize

dispMult = 7
xDisplay = xSize * dispMult
yDisplay = ySize * dispMult + 100
display = pygame.display.set_mode((xDisplay,yDisplay))

pygame.init()

font = pygame.font.SysFont(None, 25)
botText = font.render('SPACE: Pause, 1: Shuffle, 2: Asc Sort, 3: Desc Sort, Check README for more', True, WHITE)
topText = [font.render('Choose Algorithm', True, WHITE)]

STOP = [True]



def initArr(arr, size):
    arr.clear()
    for i in range(size):
        arr.append(size - i)
    random.shuffle(arr)



def draw(arr, x = None, y = None):
    #if STOP[0] == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    STOP[0] = True
    display.fill(BLACK)
    for i in range(len(arr)):
        if i == x or i == y:
            pygame.draw.rect(display, RED, [i * dispMult , (arrSize - arr[i]) * dispMult + 50, dispMult, arr[i] * dispMult])
        else:
            pygame.draw.rect(display, YELLOW, [i * dispMult , (arrSize - arr[i]) * dispMult + 50, dispMult, arr[i] * dispMult]) 
    display.blit(botText, (10 , yDisplay - 50))
    display.blit(topText[0], (50, 10)) 
    clock.tick(FPS) 
    pygame.display.update()



def insertionSort(arr):
    comps = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and STOP[0] == False:
            comps += 1
            topText[0] = font.render('Insertion Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
            draw(arr, i, j)

            if key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
                swaps += 1
            else:
                break

        arr[j+1] = key
        if STOP[0] == True:
            break
    
    topText[0] = font.render('Insertion Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
    draw(arr)



def bubbleSort(arr):
    comps = 0
    swaps = 0

    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            comps += 1
            topText[0] = font.render('Bubble Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
            draw(arr, j, j+1)
            
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if STOP[0] == True:
                break
        if (STOP[0] == True) or (swaps == 0):
            break
    
    topText[0] = font.render('Bubble Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
    draw(arr)



def partition(arr, low, high, comps, swaps):
    arr[high],arr[(low+high)//2] = arr[(low+high)//2],arr[high]
    swaps[0] += 1
    pivot = arr[high]
    i = (low-1)
  
    for j in range(low, high):
        comps[0] += 1
        topText[0] = font.render('Quick Sort    Comparisons: '+ str(comps[0]) +'    Swaps: ' + str(swaps[0]), True, WHITE)
        draw(arr, high, j)

        if arr[j] < pivot:
            swaps[0] += 1
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        if STOP[0] == True:
            break
    
    if STOP[0] == False:
        swaps[0] += 1
        arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return (i+1)
  
def quickSort(arr, low, high, comps, swaps):
    if STOP[0] == True:
        return
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high, comps, swaps)
        quickSort(arr, low, pi-1, comps, swaps)
        quickSort(arr, pi+1, high, comps, swaps)
    
    topText[0] = font.render('Quick Sort    Comparisons: '+ str(comps[0]) +'    Swaps: ' + str(swaps[0]), True, WHITE)
    draw(arr)



def selectionSort(arr):
    comps = 0
    swaps = 0

    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            comps += 1
            topText[0] = font.render('Selection Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
            draw(arr, min_ind, j)

            if arr[min_ind] > arr[j]:
                min_ind = j
            if STOP[0] == True:
                break
        if (STOP[0] == True) or (min_ind == 0):
            break
        swaps += 1
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

    topText[0] = font.render('Selection Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
    draw(arr)



def merge(arr, l, m, r, comps, swaps):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0 
    j = 0  
    k = l  
 
    while i < n1 and j < n2:
        comps[0] += 1
        topText[0] = font.render('Merge Sort    Comparisons: '+ str(comps[0]) +'    Swaps: ' + str(swaps[0]) + '    No Pause', True, WHITE)
        draw(arr, l+i, m+1+j)
        
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
        swaps[0] += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
        swaps[0] += 1
        topText[0] = font.render('Merge Sort    Comparisons: '+ str(comps[0]) +'    Swaps: ' + str(swaps[0]) + '    No Pause', True, WHITE)
        draw(arr, l+i)

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        
        swaps[0] += 1
        topText[0] = font.render('Merge Sort    Comparisons: '+ str(comps[0]) +'    Swaps: ' + str(swaps[0]) + '    No Pause', True, WHITE)
        draw(arr, m+1+j)
 
def mergeSort(arr, l, r, comps, swaps):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m, comps, swaps)
        mergeSort(arr, m+1, r, comps, swaps)
        merge(arr, l, m, r, comps, swaps)
    
    topText[0] = font.render('Merge Sort    Comparisons: '+ str(comps[0]) +'    Swaps: ' + str(swaps[0]) + '    No Pause', True, WHITE)
    draw(arr)



def oddEvenSort(arr, n):
    comps = 0
    swaps = 0

    isSorted = 0
    while isSorted == 0 and STOP[0] == False:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if STOP[0] == True:
                break
            comps += 1
            topText[0] = font.render('OddEven Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
            draw(arr, i, i+1)

            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
                swaps += 1

        for i in range(0, n-1, 2):
            if STOP[0] == True:
                break
            comps += 1
            topText[0] = font.render('OddEven Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
            draw(arr, i, i+1)

            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
                swaps += 1

    topText[0] = font.render('OddEven Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
    draw(arr)



def shellSort(arr):
    comps = 0
    swaps = 0

    gap = len(arr) // 2
 
    while gap > 0 and STOP[0] == False:
        i = 0
        j = gap

        while j < len(arr) and STOP[0] == False:
            comps += 1
            topText[0] = font.render('Shell Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
            draw(arr, i, j)

            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                swaps += 1
             
            i += 1
            j += 1

            k = i
            while k - gap > -1 and STOP[0] == False:
                comps += 1
                topText[0] = font.render('Shell Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
                draw(arr, k - gap, k)

                if arr[k - gap] > arr[k]:
                    arr[k-gap],arr[k] = arr[k],arr[k-gap]
                    swaps += 1
                k -= 1
 
        gap //= 2

    topText[0] = font.render('Shell Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
    draw(arr)



def main():

    numList = []
    initArr(numList, arrSize)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                STOP[0] = False

                if (event.key == pygame.K_q):
                    insertionSort(numList)
                elif (event.key == pygame.K_w):
                    bubbleSort(numList)
                elif (event.key == pygame.K_e):
                    quickSort(numList, 0, arrSize-1, [0], [0])
                elif (event.key == pygame.K_r):
                    selectionSort(numList)
                elif (event.key == pygame.K_t):
                    mergeSort(numList, 0, len(numList)-1, [0], [0])
                elif (event.key == pygame.K_y):
                    oddEvenSort(numList, len(numList))
                elif (event.key == pygame.K_u):
                    shellSort(numList)
                elif (event.key == pygame.K_1):
                    random.shuffle(numList)
                elif (event.key == pygame.K_2):
                    numList.sort()
                elif (event.key == pygame.K_3):
                    numList.sort(reverse=True)

                STOP[0] = True

        draw(numList)
        
if __name__ == "__main__":
    main()

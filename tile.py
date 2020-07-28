# (i,j) is the coordinate of the missing square (all the other squares will be filled)
# every tile is L shaped and consists of three squares with the same number
# n should be power of 2
# the board is n * n

n, i, j = map(int,input().split())

counter = 0

arr = [[0 for x in range(n)] for y in range(n)]

def lastL(i1, j1,i2, j2, i3, j3):
    global counter
    counter += 1
    arr[j1][i1] = counter
    arr[j2][i2] = counter
    arr[j3][i3] = counter

def printArray(arr, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = "  ")
        print()

#tile(n//2, (xStart + xEnd)//2, (yStart + yEnd)//2, xStart, (xStart + xEnd)//2, yStart, (yStart + yEnd)//2)
#tile(n//2, (xStart + xEnd)//2 + 1, (yStart + yEnd)//2, (xStart + xEnd)//2 + 1, xEnd, yStart, (yStart + yEnd)//2)
#tile(n//2, (xStart + xEnd)//2, (yStart + yEnd)//2 + 1, xStart, (xStart + xEnd)//2, (yStart + yEnd)//2 + 1, yEnd)
#tile(n//2, (xStart + xEnd)//2 + 1, (yStart + yEnd)//2 + 1, (xStart + xEnd)//2 + 1, xEnd, (yStart + yEnd)//2 + 1, yEnd)

def tile(n, i, j, xStart, xEnd, yStart, yEnd):
    global counter
    global arr
    if(n == 2):
        for y in range(yStart, yEnd + 1):
            for x in range(xStart, xEnd + 1):
                if(x != i or y != j):
                    arr[y][x] = counter + 1
                if(x == i and y == j):
                    arr[y][x] = counter
        counter += 2
    else:
        if(xStart <= i <= (xStart + xEnd)//2):

            if(yStart <= j <= (yStart + yEnd)//2):
                tile(n//2, i, j, xStart, (xStart + xEnd)//2, yStart, (yStart + yEnd)//2)
                tile(n//2, (xStart + xEnd)//2 + 1, (yStart + yEnd)//2, (xStart + xEnd)//2 + 1, xEnd, yStart, (yStart + yEnd)//2)
                tile(n//2, (xStart + xEnd)//2, (yStart + yEnd)//2 + 1, xStart, (xStart + xEnd)//2, (yStart + yEnd)//2 + 1, yEnd)
                tile(n//2, (xStart + xEnd)//2 + 1, (yStart + yEnd)//2 + 1, (xStart + xEnd)//2 + 1, xEnd, (yStart + yEnd)//2 + 1, yEnd)
                lastL((xStart + xEnd)//2 + 1,(yStart + yEnd)//2,(xStart + xEnd)//2,(yStart + yEnd)//2 + 1,(xStart + xEnd)//2 + 1,(yStart + yEnd)//2 + 1)

            if(j > (yStart + yEnd)//2):
                tile(n//2, (xStart + xEnd)//2, (yStart + yEnd)//2, xStart, (xStart + xEnd)//2, yStart, (yStart + yEnd)//2)
                tile(n//2, (xStart + xEnd)//2 + 1, (yStart + yEnd)//2, (xStart + xEnd)//2 + 1, xEnd, yStart, (yStart + yEnd)//2)
                tile(n//2, i, j, xStart, (xStart + xEnd)//2, (yStart + yEnd)//2 + 1, yEnd)
                tile(n//2, (xStart + xEnd)//2 + 1, (yStart + yEnd)//2 + 1, (xStart + xEnd)//2 + 1, xEnd, (yStart + yEnd)//2 + 1, yEnd)
                lastL((xStart + xEnd)//2,(yStart + yEnd)//2,(xStart + xEnd)//2 + 1,(yStart + yEnd)//2,(xStart + xEnd)//2 + 1,(yStart + yEnd)//2 + 1,)

        if(i > (xStart + xEnd)//2):

            if(yStart <= j <= (yStart + yEnd)//2):
                tile(n//2, (xStart + xEnd)//2, (yStart + yEnd)//2, xStart, (xStart + xEnd)//2, yStart, (yStart + yEnd)//2)
                tile(n//2, i, j, (xStart + xEnd)//2 + 1, xEnd, yStart, (yStart + yEnd)//2)
                tile(n//2, (xStart + xEnd)//2, (yStart + yEnd)//2 + 1, xStart, (xStart + xEnd)//2, (yStart + yEnd)//2 + 1, yEnd)
                tile(n//2, (xStart + xEnd)//2 + 1, (yStart + yEnd)//2 + 1, (xStart + xEnd)//2 + 1, xEnd, (yStart + yEnd)//2 + 1, yEnd)
                lastL((xStart + xEnd)//2, (yStart + yEnd)//2,(xStart + xEnd)//2 ,(yStart + yEnd)//2 + 1,(xStart + xEnd)//2 + 1,(yStart + yEnd)//2 + 1)

            if(j > (yStart + yEnd)//2):
                tile(n//2, (xStart + xEnd)//2, (yStart + yEnd)//2, xStart, (xStart + xEnd)//2, yStart, (yStart + yEnd)//2)
                tile(n//2, (xStart + xEnd)//2 + 1, (yStart + yEnd)//2, (xStart + xEnd)//2 + 1, xEnd, yStart, (yStart + yEnd)//2)
                tile(n//2, (xStart + xEnd)//2, (yStart + yEnd)//2 + 1, xStart, (xStart + xEnd)//2, (yStart + yEnd)//2 + 1, yEnd)
                tile(n//2, i, j, (xStart + xEnd)//2 + 1, xEnd, (yStart + yEnd)//2 + 1, yEnd)
                lastL((xStart + xEnd)//2,(yStart + yEnd)//2,(xStart + xEnd)//2 + 1,(yStart + yEnd)//2,(xStart + xEnd)//2,(yStart + yEnd)//2 + 1)

tile(n, i, j, 0, n-1, 0, n-1)
arr[j][i] = "*"
printArray(arr, n)

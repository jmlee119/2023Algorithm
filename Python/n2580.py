import sys 
answer = []
blank =[] 
input = sys.stdin.readline

def checkRow(x,a):
    for i in range(9):
        if a == answer[x][i]:
            return False
    return True

def checkCol(y,a):
    for i in range(9):
        if a== answer[i][y]:
            return False
    return True

def checkRect(x,y,a):
    nx = x//3 *3
    ny = y//3 *3
    for i in range(3):
        for j in range(3):
            if a == answer[nx+i][ny+j]:
                return False
    return True


def find(n):
    # print("n : ",n)
    if n==len(blank):
        for i in range(9):
            print(*answer[i])
        exit(0)
    
    for i in range(1,10):
        x = blank[n][0]
        y = blank[n][1]

        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i) :
            answer[x][y] = i
            find(n+1)
            answer[x][y] =0

for i in range(9):
    row_elements = list(map(int, input().rstrip().split()))
    answer.append(row_elements)
    for j in range(9):
        if answer[i][j]==0:
            blank.append([i,j])

find(0)


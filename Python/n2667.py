import sys

input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


result = 0
array = []
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            array.append(count)
            result += 1
            count = 0
print(result)
array.sort()
for i in array:
    print(i)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(input()) for _ in range(N)]

visited = [[False for i in range(N)] for i in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([])
    visited[x][y] = True
    q.append([x, y])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False and graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = True
                    q.append([nx, ny])


count1, count2 = 0, 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            count1 += 1

visited = [[False for i in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == "G":
            graph[i][j] = "R"

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            # color = graph[i][j]
            bfs(i, j)
            count2 += 1
print(count1, count2)

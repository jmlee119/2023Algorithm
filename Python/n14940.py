import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = [[0] * m for i in range(n)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    graph[x][y] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    continue
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == False:
            # visited[i][j] = True
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            graph[i][j] = -1

for i in graph:
    print(*i)

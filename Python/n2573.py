import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
check = False


def melting_bfs(x, y):
    q.append((x, y))

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                if graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1


day = 0
while True:
    visited = [[False] * M for _ in range(N)]
    count = [[0] * M for i in range(N)]
    result = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(melting_bfs(i, j))

    for i in range(N):
        for j in range(M):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(result) == 0:
        break
    if len(result) >= 2:
        check = True
        break
    day += 1

if check == True:
    print(day)

else:
    print(0)

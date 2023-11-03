import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == -1:
                    continue
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = 1 + graph[x][y]


result = 0


def check(graph):
    global result
    for i in graph:
        for j in i:
            if j == 0:
                return False
        result = max(max(i), result)
    return True


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
bfs()

if check(graph):
    print(result - 1)
else:
    print(-1)

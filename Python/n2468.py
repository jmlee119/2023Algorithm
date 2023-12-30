import sys
from collections import deque


input = sys.stdin.readline

N = int(input())
graph = []
max_value = 0
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] > max_value:
            max_value = graph[i][j]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, value, graph):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


count = 0
result = []
for k in range(max_value + 1):
    visited = [[0] * N for i in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == 0:
                bfs(i, j, k, graph)
                count += 1
    result.append(count)

print(max(result))

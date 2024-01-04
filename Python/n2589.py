import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for i in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 0
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == "L" and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx, ny))
    return cnt - 1


result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            visited = [[0] * M for i in range(N)]
            result = max(result, bfs(i, j))

print(result)

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if graph[nx][ny][nz] == -1:
                    continue

                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    queue.append([nx, ny, nz])


queue = deque()
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))
result = 0


def check(graph):
    global result
    for i in graph:
        for j in i:
            for k in j:
                if k == 0:
                    return False
            result = max(max(j), result)
    return True


bfs()

if check(graph):
    print(result - 1)

else:
    print(-1)

import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())

graph = [[0 for i in range(M)] for j in range(N)]
visited = [[False for i in range(M)] for j in range(N)]
count = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    cnt = 0
    # print("함수실행")
    q = deque([])
    graph[x][y] = 1
    q.append([x, y])

    while q:
        cnt += 1
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append([nx, ny])
    return cnt


for _ in range(K):
    p1, p2, p3, p4 = map(int, input().split())
    for i in range(p2, p4):
        for j in range(p1, p3):
            graph[i][j] = 1

answer = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            a = bfs(i, j)
            answer.append(a)
            count += 1
answer.sort()
print(count)
print(*answer)

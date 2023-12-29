import sys

input = sys.stdin.readline

move = [1, -1]


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))

visited = [[False] * M for i in range(N)]


def dfs(x, y):
    visited[x][y] = True
    if board[x][y] == "|":
        for i in range(2):
            nx = x + move[i]
            if 0 <= nx < N and board[nx][y] == "|" and visited[nx][y] == False:
                dfs(nx, y)
    if board[x][y] == "-":
        for i in range(2):
            ny = y + move[i]
            if 0 <= ny < M and board[x][ny] == "-" and visited[x][ny] == False:
                dfs(x, ny)


count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)

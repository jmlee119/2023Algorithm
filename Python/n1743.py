import sys
from collections import deque

input = sys.stdin.readline

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    global cnt
    q.append((x, y))

    while q:
        x, y = q.popleft()
        board[x][y] = 1
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == "#":
                board[dx][dy] = board[x][y] + 1
                cnt += 1
                q.append((dx, dy))


n, m, k = map(int, input().split())
board = [["." for _ in range(m)] for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = "#"

big = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "#":
            cnt = 1
            bfs(i, j)
            big = max(big, cnt)


print(big)

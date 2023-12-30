import sys

input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(str, input().rstrip())))

f = [[0] * (N + 1) for i in range(N + 1)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if board[i][j] == "Y" or (board[i][k] == "Y" and board[k][j] == "Y"):
                f[i][j] = 1

res = 0
for i in f:
    res = max(res, sum(i))

print(res)

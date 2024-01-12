import sys

input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))

for i in range(1, N - 1):
    for j in range(1, N - 1):
        if (
            board[i - 1][j] == "*"
            and board[i + 1][j] == "*"
            and board[i][j - 1] == "*"
            and board[i][j + 1] == "*"
        ):
            a, b = i, j
print(a + 1, b + 1)

left_arm, right_arm, waist, left_leg, right_leg = 0, 0, 0, 0, 0

for i in range(b - 1, -1, -1):
    if board[a][i] == "*":
        left_arm += 1

for i in range(b + 1, N):
    if board[a][i] == "*":
        right_arm += 1

last_a, last_b = 0, b
for i in range(a + 1, N):
    if board[i][b] == "*":
        waist += 1
        last_a = i

for i in range(a + 1, N):
    if board[i][last_b - 1] == "*":
        left_leg += 1

for i in range(a + 1, N):
    if board[i][last_b + 1] == "*":
        right_leg += 1
print(left_arm, right_arm, waist, left_leg, right_leg)

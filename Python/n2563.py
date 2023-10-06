import sys

input = sys.stdin.readline

n = int(input())

white_board = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            white_board[i][j] = 1

result = 0
for i in white_board:
    for j in i:
        result += j
print(result)

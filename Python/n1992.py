import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))


def trees(board, row, col, end):
    all_sum = 0
    for i in range(col, col + end):
        for j in range(row, row + end):
            all_sum += board[i][j]

    if all_sum == 0:
        print(0, end="")
    elif all_sum == end * end:
        print(1, end="")

    else:
        print("(", end="")
        mid = end // 2
        trees(board, row, col, mid)
        trees(board, row + mid, col, mid)
        trees(board, row, col + mid, mid)
        trees(board, row + mid, col + mid, mid)
        print(")", end="")


trees(board, 0, 0, N)

import sys

input = sys.stdin.readline


def Z(row, col, n):
    global count
    if row > r or row + n <= r or col > c or col + n <= c:
        count += n**2
        return
    if n > 2:
        n = n // 2
        Z(row, col, n)
        Z(row, col + n, n)
        Z(row + n, col, n)
        Z(row + n, col + n, n)
    else:
        if row == r and col == c:
            print(count)
        elif row == r and col + 1 == c:
            print(count + 1)
        elif row + 1 == r and col == c:
            print(count + 2)
        elif row + 1 == r and col + 1 == c:
            print(count + 3)


n, r, c = map(int, input().split())
count = 0

Z(0, 0, 2**n)

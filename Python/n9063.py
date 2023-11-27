import sys

input = sys.stdin.readline

n = int(input())
row = []
col = []
for _ in range(n):
    a, b = map(int, input().split())
    row.append(a)
    col.append(b)


if n <= 1:
    answer = 0
else:
    answer = (max(row) - min(row)) * (max(col) - min(col))

print(answer)

import sys

input = sys.stdin.readline
N, B = map(str, input().split())
B = int(B)

N = N[::-1]
JIN = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0

for i in range(len(N) - 1, -1, -1):
    result += (B**i) * JIN.index(N[i])

print(result)

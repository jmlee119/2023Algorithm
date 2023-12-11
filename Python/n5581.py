import sys

input = sys.stdin.readline

coins = [500, 100, 50, 10, 5, 1]
N = int(input())
i, count = 0, 0
ans = 1000 - N

while ans > 0:
    if ans >= coins[i]:
        count += 1
        ans -= coins[i]
    else:
        i += 1

print(count)

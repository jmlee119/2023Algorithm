import sys

input = sys.stdin.readline

n = int(input())

list = list(map(int, input().rstrip().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if list[i] > list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

import sys

input = sys.stdin.readline

n = int(input())
boxs = list(map(int, input().split()))
dp = [1] * 1001

for i in range(n):
    for j in range(i):
        if boxs[i] > boxs[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

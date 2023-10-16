import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 103

dp[1] = 1
dp[2] = 1
dp[3] = 1
for _ in range(n):
    m = int(input())
    for i in range(4, m + 1):
        dp[i] = dp[i - 3] + dp[i - 2]
    print(dp[m])

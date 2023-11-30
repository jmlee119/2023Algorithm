import sys

input = sys.stdin.readline
N = int(input())

dp = [[0]]
for i in range(N):
    dp.append(list(map(int, input().split())))


for i in range(1, N + 1):
    for j in range(i):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j]
        elif j == i - 1:
            dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + dp[i][j], dp[i - 1][j] + dp[i][j])


print(max(dp[N]))

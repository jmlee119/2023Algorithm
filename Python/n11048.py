import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [[0 for i in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            dp[i][j] = arr[i][j]
        elif i == 0:
            dp[i][j] = arr[i][j] + dp[i][j - 1]
        elif j == 0:
            dp[i][j] = arr[i][j] + dp[i - 1][j]
        else:
            dp[i][j] = arr[i][j] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
# print(dp)
print(max(max(dp)))

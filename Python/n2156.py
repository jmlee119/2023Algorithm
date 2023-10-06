import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 100000
array = [0] * 100000
for i in range(n):
    array[i] = int(input())

dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[2] + array[1], array[2] + array[0], dp[1])

for i in range(3, n + 1):
    dp[i] = max(array[i] + array[i - 1] + dp[i - 3], array[i] + dp[i - 2], dp[i - 1])

print(max(dp))

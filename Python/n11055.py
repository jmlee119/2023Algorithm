import sys

input = sys.stdin.readline

# dp = [1] * 1001

N = int(input())

arr = list(map(int, input().split()))
dp = [i for i in arr]
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))

import sys

input = sys.stdin.readline

N = int(input())
dp = [1] * N

edges = []
for i in range(N):
    a, b = map(int, input().split())
    edges.append([a, b])

edges.sort()

for i in range(N):
    for j in range(i):
        if edges[i][1] > edges[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))

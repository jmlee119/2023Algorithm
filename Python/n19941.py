import sys

input = sys.stdin.readline
N, K = map(int, input().split())
Ham = list(input())
count = 0

for i in range(N):
    if Ham[i] == "P":
        for j in range(max(i - K, 0), min(N, i + K + 1)):
            if Ham[j] == "H":
                Ham[j] = "0"
                count += 1
                break

print(count)

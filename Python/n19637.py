import sys

input = sys.stdin.readline

N, M = map(int, input().split())
rank = []

for _ in range(N):
    name, power = map(str, input().split())
    power = int(power)
    rank.append([name, power])


def bs(rank, m):
    start = 0
    end = len(rank) - 1
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if int(rank[mid][1]) >= m:
            end = mid - 1
            res = mid
        else:
            start = mid + 1
    return res


for _ in range(M):
    m = int(input())
    print(rank[bs(rank, m)][0])

import sys

input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


def cal(alist, blist):
    asm, bsm = 0, 0
    for i in range(M):
        for j in range(M):
            asm += graph[alist[i]][alist[j]]
            bsm += graph[blist[i]][blist[j]]
    return abs(asm - bsm)


def dfs(n, alist, blist):
    global ans
    if n == N:
        if len(alist) == len(blist):
            ans = min(ans, cal(alist, blist))
        return

    dfs(n + 1, alist + [n], blist)
    dfs(n + 1, alist, blist + [n])


M = N // 2
ans = sys.maxsize

dfs(0, [], [])

print(ans)

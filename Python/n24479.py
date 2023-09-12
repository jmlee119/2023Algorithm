import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(a):
    global cnt
    visited[a] = cnt
    line[a].sort()
    for i in line[a]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


n, m, r = map(int, input().split())
line = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    line[a].append(b)
    line[b].append(a)
dfs(r)
# print(visited)
for i in range(1, n + 1):
    print(visited[i])

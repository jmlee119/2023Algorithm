import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
visited = [0] * (n + 1)
count = 1
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    global count
    q = deque([k])
    visited[k] = 1
    while q:
        v = q.popleft()
        graph[v].sort(reverse=True)
        for g in graph[v]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                q.append(g)


bfs(k)

for v in visited[1:]:
    print(v)

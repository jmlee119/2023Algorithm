import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, i, visited):
    visited[i] = True
    dfs_answer.append(i)
    graph[i].sort()
    for i in graph[i]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        graph[v].sort()
        bfs_answer.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs_answer = []
bfs_answer = []

visited = [False] * (n + 1)
dfs(graph, v, visited)

visited = [False] * (n + 1)
bfs(graph, v, visited)

print(*dfs_answer)

print(*bfs_answer)

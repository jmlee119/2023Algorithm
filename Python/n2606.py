import sys
from collections import deque

input = sys.stdin.readline

computer = int(input())
line = int(input())

graph = [[] for _ in range(computer + 1)]
for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computer + 1)


def bfs(graph, start, visited):
    count = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                count += 1
                queue.append(i)
                visited[i] = True

    return count


result = bfs(graph, 1, visited)

print(result)

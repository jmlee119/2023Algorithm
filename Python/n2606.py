import sys

input = sys.stdin.readline

computer = int(input())
line = int(input())
graph = [[] for i in range(computer + 1)]

visited = [False] * (computer + 1)

for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0


def dfs(start, visited, graph):
    visited[start] = True

    global cnt

    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            visited[i] = True
            dfs(i, visited, graph)


dfs(1, visited, graph)

print(cnt)

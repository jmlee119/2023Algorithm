import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for i in range(V + 1)]
indegree = [0] * (V + 1)

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topolog_sort():
    result = []
    q = []

    for i in range(1, V + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

    for i in result:
        print(i, end=" ")


topolog_sort()

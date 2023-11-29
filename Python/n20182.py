import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, A, B, C = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]

distance = [INF] * N + 1

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(A)

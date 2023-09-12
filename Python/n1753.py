import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] * (V + 1) for _ in range(V + 1)]
distance = [INF] * (V + 1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

print("graph : ", graph)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    print("q : ", q)
    print("distance : ", distance)

    while q:
        dist, now = heapq.heappop(q)
        print("dist, now :", dist, now)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

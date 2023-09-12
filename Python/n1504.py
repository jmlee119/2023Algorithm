import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
INF = int(1e9)
graph = [[] * (V + 1) for _ in range(V + 1)]
# graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
v1, v2 = map(int, input().split())
# print("graph : ", graph)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (V + 1)
    distance[start] = 0
    # print("q : ", q)
    # print("distance : ", distance)

    while q:
        dist, now = heapq.heappop(q)
        # print("dist, now :", dist, now)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


first = dijkstra(1)
v1_d = dijkstra(v1)
v2_d = dijkstra(v2)
# print(first, v1_d, v2_d)
result = min(first[v1] + v1_d[v2] + v2_d[V], first[v2] + v2_d[v1] + v1_d[V])
if result < INF:
    print(result)
else:
    print(-1)

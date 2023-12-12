import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N, E = map(int, input().split())

graph = [[] for i in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        distance[start] = 0
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[0] + dist
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return distance


original = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)


path1 = original[v1] + v1_distance[v2] + v2_distance[N]
path2 = original[v2] + v2_distance[v1] + v1_distance[N]

result = min(path1, path2)

if result < INF:
    print(result)
else:
    print(-1)

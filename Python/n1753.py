import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [[] for i in range(V + 1)]

distance = [INF] * (V + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

    # heapq 쓰려면 앞이 가중치고 뒤가 ㅑndex여야 함.


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[0] + dist
            if cost < distance[i[1]]:  # distance [now ] 가 아니였음
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


dijkstra(start)
# print(distance)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

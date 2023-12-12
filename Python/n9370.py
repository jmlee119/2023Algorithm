import sys
import heapq

input = sys.stdin.readline
Testcase = int(input())
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return distance


for _ in range(Testcase):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for i in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))

    arrive = []
    for _ in range(t):
        arrive.append(int(input()))

    original = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)

    ans = []
    for i in arrive:
        if (original[g] + g_dijk[h] + h_dijk[i] == original[i]) or (
            original[h] + h_dijk[g] + g_dijk[i] == original[i]
        ):
            ans.append(i)

    ans.sort()

    print(ans)

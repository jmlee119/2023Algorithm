import sys

input = sys.stdin.readline
INF = sys.maxsize

Testcase = int(input())


def bellman_ford():
    global ispossible
    for repeat in range(n):
        for now in range(1, n + 1):
            for next, weight in graph[now]:
                if distance[now] != INF and distance[next] > distance[now] + weight:
                    distance[next] = distance[now] + weight
                    if repeat == n - 1:
                        ispossible = False


for _ in range(Testcase):
    n, m, w = map(int, input().split())
    ispossible = True
    graph = [[] for _ in range(n + 1)]
    distance = [10001] * (n + 1)

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    bellman_ford()
    if not ispossible:
        print("YES")
    else:
        print("NO")
    # print(graph)

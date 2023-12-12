import sys


input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)
distance[1] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

ispossible = True


def bellman_ford():
    global ispossible
    for repeat in range(N):
        for now in range(1, N + 1):
            for next, weight in graph[now]:
                if distance[now] != INF and distance[next] > distance[now] + weight:
                    distance[next] = distance[now] + weight
                    if repeat == N - 1:
                        ispossible = False


bellman_ford()

if not ispossible:
    print(-1)
else:
    for i in distance[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)

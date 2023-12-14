import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
parent = [i for i in range(N + 1)]
total = 0

for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    total += cost
edges.sort()


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]


def union(a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


result = 0

for i in edges:
    cost, a, b = i
    if find(parent, a) != find(parent, b):
        union(a, b)
        result += cost
        end = cost
print(result - end)

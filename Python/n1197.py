import sys

input = sys.stdin.readline

V, E = map(int, input().split())

edges = []
answer = 0
parent = [i for i in range(V + 1)]
for _ in range(V):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for (
    a,
    b,
    c,
) in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)

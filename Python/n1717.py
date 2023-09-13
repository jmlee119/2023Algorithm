import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())

parent = []
for i in range(n + 1):
    parent.append(i)


def find(n):
    if parent[n] == n:
        return n
    p = find(parent[n])
    parent[n] = p
    return parent[n]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    elif a > b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        union(a, b)
    elif check == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

# print(parent)

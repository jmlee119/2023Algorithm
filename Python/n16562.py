import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M, K = map(int, input().split())
money = [0] + list(map(int, input().split()))

parent = [i for i in range(N + 1)]

ans = []


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])

    return parent[x]


def union(a, b, parent):
    a = find(parent, a)
    b = find(parent, b)
    if money[a] > money[b]:
        money[a] = 0
        parent[a] = b
    else:
        money[b] = 0
        parent[b] = a


for _ in range(M):
    a, b = map(int, input().split())
    union(a, b, parent)

friend = set()
print(money)
result = 0
for i in range(1, N + 1):
    if parent[i] not in friend:
        result += money[parent[i]]
        friend.add(parent[i])
# print(parent)
# print(ans)


if result > K:
    print("Oh no")
else:
    print(result)

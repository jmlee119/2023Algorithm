import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N)]
way = []


def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
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


for i in range(N):
    way = list(map(int, input().split()))
    for j in range(M):
        if way[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
# print(parent)
ans = "YES"
for i in range(1, M):
    if parent[plan[i] - 1] != parent[plan[0] - 1]:
        ans = "NO"

print(ans)

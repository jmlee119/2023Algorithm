import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
count = [0] * (N + 1)
parent = [i for i in range(N + 1)]
# print(parent)


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]


def union(a, b, parent):
    a = find(parent, a)
    b = find(parent, b)

    if count[a] >= count[b]:
        parent[b] = a
    else:
        parent[a] = b


input_ans = []

for _ in range(M):
    a, b = map(int, input().split())
    count[a] += 1
    count[b] += 1
    input_ans.append([a, b])

for a, b in input_ans:
    union(a, b, parent)

ans = set(parent[1:])
print(len(ans))
for i in list(ans):
    print(i)

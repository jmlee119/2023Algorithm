import sys

input = sys.stdin.readline

Gate = int(input())
Airplane = int(input())
parent = [i for i in range(Gate + 1)]
count = 0


def find(g):
    if parent[g] == g:
        return g
    parent[g] = find(parent[g])
    return parent[g]


plane_list = []
for _ in range(Airplane):
    g = int(input())
    plane_list.append(g)

for plane in plane_list:
    temp = find(plane)
    if temp == 0:
        break
    parent[temp] = parent[temp - 1]
    count += 1

print(count)

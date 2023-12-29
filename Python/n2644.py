import sys

input = sys.stdin.readline

num = int(input())
N, M = map(int, input().split())
line = int(input())

family = [[] for i in range(num + 1)]

visited = [False] * (num + 1)

for _ in range(line):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)


def dfs(num, depth):
    depth += 1
    # print(depth)
    visited[num] = True
    if num == M:
        answer.append(depth)

    for i in family[num]:
        if not visited[i]:
            dfs(i, depth)


# answer = dfs(N, 0)
answer = []
dfs(N, 0)
if not answer:
    print(-1)
else:
    print(answer[0] - 1)

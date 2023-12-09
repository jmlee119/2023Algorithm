import sys
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
myCnt = [[] for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    myCnt[b] = 1


def bfs(start, visited, graph):
    cnt = 1
    visited[start] = True
    q = deque([start])

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                q.append(i)
    # print(cnt)
    return cnt


answer = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    if myCnt[i] == 0:
        answer.append(0)
    else:
        cnt = bfs(i, visited, graph)
        answer.append(cnt)

max_answer = max(answer)

for idx, i in enumerate(answer):
    if max_answer == i:
        print(idx + 1, end=" ")
# print(answer)
# #

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x + 1, x - 1, 2 * x):
            if 0 <= nx <= len(dist) - 1 and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)


n, k = map(int, input().split())
dist = [0] * 100001
bfs()

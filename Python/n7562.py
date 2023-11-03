import sys
from collections import deque

input = sys.stdin.readline

dx = [2, -2, 2, -2, 1, 1, -1, -1]
dy = [1, 1, -1, -1, 2, -2, 2, -2]


def bfs():
    queue = deque([])
    queue.append((start1, start2))

    while queue:
        # print("dfkaop")
        x, y = queue.popleft()
        if x == end1 and y == end2:
            return graph[end1][end2] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < line and 0 <= ny < line and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


TestCase = int(input())

for _ in range(TestCase):
    line = int(input())

    graph = [[0 for i in range(line)] for j in range(line)]

    start1, start2 = map(int, input().split())
    end1, end2 = map(int, input().split())
    graph[start1][start2] = 1
    result = bfs()

    print(result)

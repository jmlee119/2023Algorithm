# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M = map(int, input().split())

# graph = []

# for _ in range(N):
#     graph.append(list(map(int, input().rstrip())))
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))

#     while queue:
#         print(queue)
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M:
#                 if graph[nx][ny] == 1:
#                     continue
#                 if graph[nx][ny] == 0:
#                     graph[nx][ny] = 1
#                     queue.append((nx, ny))

#     return


# result = 0

# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 0:
#             graph[i][j] = 1
#             bfs(i, j)
#             result += 1


# print(result)

import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

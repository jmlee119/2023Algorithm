import sys
import heapq

input = sys.stdin.readline

n = int(input())
max_heapq = []
for _ in range(n):
    x = int(input()) * -1
    if x != 0:
        heapq.heappush(max_heapq, x)
    else:
        try:
            print(-1 * heapq.heappop(max_heapq))
        except:
            print(0)

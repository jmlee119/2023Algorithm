import sys
import heapq

input = sys.stdin.readline

n = int(input())
max_heapq = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(max_heapq, x)
    else:
        try:
            print(heapq.heappop(max_heapq))
        except:
            print(0)

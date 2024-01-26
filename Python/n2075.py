import sys
import heapq

q = []

N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    if not q:
        for i in arr:
            heapq.heappush(q, i)
    else:
        for i in arr:
            if q[0] <= i:
                heapq.heappush(q, i)
                heapq.heappop(q)


print(q[0])

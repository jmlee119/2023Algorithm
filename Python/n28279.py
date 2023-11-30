import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque([])
for _ in range(N):
    num = list(map(int, input().split()))
    if len(num) == 2:
        if num[0] == 1:
            queue.appendleft(num[1])
        if num[0] == 2:
            queue.append(num[1])
    else:
        enum = num[0]
        if enum == 3:
            if len(queue) == 0:
                print(-1)
            else:
                e = queue.popleft()
                print(e)

        elif enum == 4:
            if len(queue) == 0:
                print(-1)
            else:
                e = queue.pop()
                print(e)

        elif enum == 5:
            print(len(queue))

        elif enum == 6:
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif enum == 7:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif enum == 8:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])

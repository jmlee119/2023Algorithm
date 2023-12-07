import sys
import math

input = sys.stdin.readline

Testcase = int(input())

for _ in range(Testcase):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if (dist == r1 + r2) or abs(r2 - r1) == dist:
            print(1)
        elif (dist < r1 + r2) and abs(r2 - r1) < dist:
            print(2)
        else:
            print(0)

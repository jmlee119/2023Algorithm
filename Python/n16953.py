import sys

input = sys.stdin.readline

A, B = map(int, input().split())

count = 1
while B != A:
    count += 1
    temp = B
    if B % 10 == 1:
        B = B // 10
    elif B % 2 == 0:
        B = B // 2

    if temp == B:
        print(-1)
        break
else:
    print(count)

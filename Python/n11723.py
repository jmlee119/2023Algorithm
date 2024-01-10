import sys

input = sys.stdin.readline

N = int(input())
s = set()
for _ in range(N):
    temp = input().strip().split()
    if len(temp) == 1:
        if temp[0] == "all":
            for i in range(1, 21):
                s.add(i)
        elif temp[0] == "empty":
            s = set()
    else:
        cen, num = temp[0], temp[1]
        num = int(num)
        if cen == "add":
            s.add(num)
        elif cen == "remove":
            s.discard(num)
        elif cen == "check":
            if num in s:
                print(1)
            else:
                print(0)
        elif cen == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)

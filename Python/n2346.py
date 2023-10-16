import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
qq = deque(enumerate(map(int, input().split())))
ans = []


while qq:
    idx, bo = qq.popleft()
    ans.append(idx + 1)

    if bo > 0:
        qq.rotate(-(bo - 1))
    else:
        qq.rotate(-bo)

print(" ".join(map(str, ans)))

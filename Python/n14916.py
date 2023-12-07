import sys

input = sys.stdin.readline

n = int(input())
count = 0
coin = [5, 2]

for i in coin:
    count = n // i

    n = n - (i % count)

if count == 0 and n != 0:
    print(-1)
else:
    print(count)

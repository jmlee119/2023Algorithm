import sys

input = sys.stdin.readline

n = int(input())
count = 0
coin = [5, 2]

while n > 0:
    if n % 5 == 0:
        count += n // 5
        break
    else:
        n -= 2
        count += 1

if count == 0 or n < 0:
    print(-1)
else:
    print(count)

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
bag = sorted(list(map(int, input().split())))

start, end = 0, 0
sum = bag[start]
count = 1

while end < len(bag) - 1:
    if sum == C:
        count += 1
        sum -= bag[start]
        start += 1
        end += 1
        sum += bag[end]
    elif sum <= C:
        count += 1
    else:
        end += 1
        sum += bag[end]

print(count)

import sys

input = sys.stdin.readline
N, S = map(int, input().split())
list = list(map(int, input().split()))

min_value = sys.maxsize
left, right = 0, 0
sum = 0
while True:
    if sum >= S:
        min_value = min(min_value, right - left)
        sum -= list[left]
        left += 1
    elif right == N:
        break
    else:
        sum += list[right]
        right += 1

if min_value == sys.maxsize:
    print(0)
else:
    print(min_value)

import sys

input = sys.stdin.readline
N = int(input())
list = sorted(list(map(int, input().rstrip().split())))
start, end = 0, N - 1
answer = [list[0], list[N - 1]]
min_value = abs(list[start] + list[end])
while start < end:
    temp = list[start] + list[end]
    if abs(temp) < min_value:
        min_value = abs(temp)
        answer = [list[start], list[end]]
        if min_value == 0:
            break
    if temp < 0:
        start += 1
    else:
        end -= 1
print(answer[0], answer[1])

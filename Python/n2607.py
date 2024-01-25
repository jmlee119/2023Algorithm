import sys

input = sys.stdin.readline

N = int(input())
target = list(input().rstrip())

count = 0

for _ in range(N - 1):
    compare = target[:]
    word = input().rstrip()
    cnt = 0

    for i in word:
        if i in compare:
            compare.remove(i)
        else:
            cnt += 1
    if cnt < 2 and len(compare) < 2:
        count += 1
print(count)

import sys

input = sys.stdin.readline

N = int(input())
km = list(map(int, input().split()))
money = list(map(int, input().split()))

total = 0
m = money[0]
for i in range(N - 1):
    if m > money[i]:
        m = money[i]
    total += m * km[i]


print(total)

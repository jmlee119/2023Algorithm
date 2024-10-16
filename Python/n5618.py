import sys
import math

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

gcd = math.gcd(*numbers)

for i in range(1, (gcd // 2) + 1):
    if gcd % i == 0:
        print(i)
print(gcd)

import sys
import math

input = sys.stdin.readline
n = int(input())

tress = []

for _ in range(n):
    tree = int(input())
    tress.append(tree)

cm = []

for i in range(1, n):
    s = tress[i] - tress[i - 1]
    cm.append(s)

cm_gcd = math.gcd(*cm)

answer = 0
for i in cm:
    answer += i // cm_gcd - 1

print(answer)

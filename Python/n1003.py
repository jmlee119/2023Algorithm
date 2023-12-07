import sys

input = sys.stdin.readline

dp = [0] * 40

testcase = int(input())

for _ in range(testcase):
    n = int(input())
    a, b = 1, 0
    for _ in range(n):
        a, b = b, b + a
    print(a, b)

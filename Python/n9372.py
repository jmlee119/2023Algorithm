import sys

input = sys.stdin.readline

Test = int(input())
for _ in range(Test):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    print(N - 1)

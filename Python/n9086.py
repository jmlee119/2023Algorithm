import sys

input = sys.stdin.readline
n = int(input())


for _ in range(n):
    answer = []
    s = input().split()
    answer.append(s[0][0])
    answer.append(s[0][-1])
    print(s)
    print(answer)
    print("".join(answer))

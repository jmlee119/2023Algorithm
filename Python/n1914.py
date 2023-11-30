import sys

input = sys.stdin.readline
N = int(input())


def hanoi(top, from_, by, to):
    if top == 1:
        print(from_, to)
        return
    else:
        hanoi(top - 1, from_, to, by)
        print(from_, to)
        hanoi(top - 1, by, from_, to)


print(2**N - 1)

if N < 20:
    hanoi(N, 1, 2, 3)

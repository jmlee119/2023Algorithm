import sys

input = sys.stdin.readline

N = int(input())


def hanoi(n, from_n, by_n, to_n):
    if n == 1:
        print(from_n, to_n)
        return

    else:
        hanoi(n - 1, from_n, to_n, by_n)
        print(from_n, to_n)
        hanoi(n - 1, by_n, from_n, to_n)


print(2**N - 1)
hanoi(N, 1, 2, 3)

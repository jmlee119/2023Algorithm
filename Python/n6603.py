import sys

input = sys.stdin.readline


def choice(depth, idx):
    if depth == 6:
        print(*new_array)
    else:
        for i in range(idx, k):
            new_array.append(lotto[i])
            choice(depth + 1, i + 1)
            new_array.pop()


while True:
    array = list(map(int, input().split()))
    k = array[0]
    lotto = array[1:]

    if k == 0:
        break

    new_array = []

    choice(0, 0)
    print()

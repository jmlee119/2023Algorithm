import sys

# sys.setrecursionlimit(10)
input = sys.stdin.readline

N = int(input())
money = list(map(int, input().split()))
max_money = int(input())
total = 0


def HAP(n):
    total = 0
    for m in money:
        if m > n:
            total += n
        else:
            total += m
    return total


def binary(start, last):
    global total
    if start > last:
        return last

    mid = (start + last) // 2
    hap = HAP(mid)

    # print("합", hap)
    if hap > max_money:
        total = mid
        return binary(start, mid - 1)
    else:
        return binary(mid + 1, last)


result = binary(1, max(money))
print(result)

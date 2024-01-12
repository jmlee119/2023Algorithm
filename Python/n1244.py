import sys

input = sys.stdin.readline
n = int(input())

switch = [0] + list(map(int, input().split()))
student = int(input())


def change(i):
    if switch[i] == 0:
        switch[i] = 1
    else:
        switch[i] = 0
    return


for _ in range(student):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, n + 1, num):
            change(i)

    else:
        change(num)
        for x in range(n // 2):
            # print(x + num, x - num, switch[num + x], switch[num - x])
            if x + num > n or num - x < 1:
                break
            if switch[num + x] == switch[num - x]:
                # print()
                change(num + x)
                change(num - x)
            else:
                break

for i in range(1, n + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()

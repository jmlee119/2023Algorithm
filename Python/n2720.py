import sys

input = sys.stdin.readline

Testcase = int(input())

moneys = [25, 10, 5, 1]

for _ in range(Testcase):
    nows = int(input())
    i = 0
    answer = [0, 0, 0, 0]
    while True:
        if nows == 0 or i > 4:
            break
        else:
            count = nows // moneys[i]
            nows = nows % moneys[i]
            answer[i] = count
            i += 1
    print(" ".join(map(str, answer)))

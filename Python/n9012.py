import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    stack = input()
    answer = []
    for i in stack:
        # print("answer: ", answer)
        if i == "(":
            answer.append(i)
        elif i == ")":
            if answer:
                answer.pop()
            else:
                print("NO")
                break
    # print("answer: ", answer)
    else:
        if not answer:
            print("YES")
        else:
            print("NO")

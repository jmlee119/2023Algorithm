import sys

input = sys.stdin.readline
stack = []
# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
N = int(input())
for _ in range(N):
    case = input().split()
    if case[0] == "1":
        stack.append(case[1])
    elif case[0] == "2":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif case[0] == "3":
        print(len(stack))
    elif case[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif case[0] == "5":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

# 9
# 4
# 1 3
# 1 5
# 3
# 2
# 5
# 2
# 2
# 5

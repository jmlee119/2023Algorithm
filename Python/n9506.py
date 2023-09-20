import sys

input = sys.stdin.readline


def su(n):
    answer = []
    for i in range(1, n):
        if n % i == 0:
            answer.append(i)
    # str_ans = ""
    # str_ans = n + str_ans + " = "
    if sum(answer) == n:
        print(n, " = ", " + ".join(str(i) for i in answer), sep="")
    else:
        print(n, "is NOT perfect.")


while True:
    n = int(input())
    if n == -1:
        break
    else:
        su(n)

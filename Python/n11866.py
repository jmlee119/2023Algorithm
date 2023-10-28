import sys

input = sys.stdin.readline
n, k = map(int, input().split())

index = 0
answer = []

array = [i for i in range(1, n + 1)]
while array:
    index += k - 1
    index = index % len(array)
    answer.append(array.pop(index))


print("<", end="")
for i in range(len(answer) - 1):
    print(answer[i], end=", ")
print(answer[-1], end="")
print(">")

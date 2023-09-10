import sys

input = sys.stdin.readline


def Binary(a, start, end, target):
    find = False
    global answer
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return a[start : end + 1].count(target)
        elif a[mid] > target:
            end = mid - 1
        elif a[mid] < target:
            start = mid + 1

    if find == False:
        return 0


n = int(input())
list1 = list(map(int, input().rstrip().split()))
m = int(input())
list2 = list(map(int, input().rstrip().split()))
list1.sort()

answer = []
for i in list2:
    target = i
    answer.append(Binary(list1, 0, len(list1) - 1, target))
print(*answer)

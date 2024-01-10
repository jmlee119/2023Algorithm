import sys

input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    arr.sort()
    a = arr[0]
    b = arr[1]
    c = arr[2]
    if a == 0 and b == 0 and c == 0:
        break

    if c >= a + b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

import sys

input = sys.stdin.readline

n, b = map(int, input().split())


def hap_function(n, matrix1, matrix2):
    result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000

    return result


def devide(n, b, matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return hap_function(n, matrix, matrix)
    else:
        temp = devide(n, b // 2, matrix)
        if b % 2 == 0:
            return hap_function(n, temp, temp)
        else:
            return hap_function(n, hap_function(n, temp, temp), matrix)


matrix = [0 for i in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))

answer = devide(n, b, matrix)

for i in answer:
    for j in i:
        print(j % 1000, end=" ")
    print()

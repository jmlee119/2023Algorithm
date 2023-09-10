# import sys
# sys.setrecursionlimit(10**6)

# def check(board, row, col, end):
#     global minus_count, zero_count, one_count
#     all_sum = 0

#     for i in range(row, row + end):
#         for j in range(col, col + end):
#             all_sum += board[i][j]
    
#     if all_sum == 0:
#         zero_count += 1
#     elif all_sum == end * end:
#         one_count += 1
#     elif all_sum == -(end * end):
#         minus_count += 1
#     else:
#         mid = end // 3
#         for i in range(3):
#             for j in range(3):
#                 check(board, row + i * mid, col + j * mid, mid)

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# minus_count, zero_count, one_count = 0, 0, 0
# check(board, 0, 0, n)

# print(minus_count)
# print(zero_count)
# print(one_count)


def divide_paper(matrix, n, row, col):
    global minus_count, zero_count, one_count

    check = matrix[row][col]
    same = True

    for i in range(row, row + n):
        for j in range(col, col + n):
            if matrix[i][j] != check:
                same = False
                break
        if not same:
            break

    if same:
        if check == -1:
            minus_count += 1
        elif check == 0:
            zero_count += 1
        else:
            one_count += 1
        return

    new_n = n // 3

    for i in range(3):
        for j in range(3):
            divide_paper(matrix, new_n, row + i * new_n, col + j * new_n)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

minus_count, zero_count, one_count = 0, 0, 0
divide_paper(matrix, n, 0, 0)

print(minus_count)
print(zero_count)
print(one_count)

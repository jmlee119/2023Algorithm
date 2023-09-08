import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def cut(board, row,col,end):
    global zero_count, one_count
    all_sum=0
    for i in range(row, row + end):
        for j in range(col, col + end):
            all_sum += board[i][j]
    if all_sum ==0:
        zero_count +=1
    elif all_sum == end*end:
        one_count +=1
    else:
        mid = end//2

        cut(board, row, col , mid)
        cut(board, row, col +mid , mid)
        cut(board, row+ mid , col , mid)
        cut(board,row+mid, col+mid, mid)


n = int(input())
board = [list(map(int , input().rstrip().split())) for _ in range(n)]
zero_count=0
one_count=0
cut(board,0,0,n)
print(zero_count)
print(one_count)
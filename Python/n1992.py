import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def cut(board, row,col,end):
    global answer
    all_sum=0
    for i in range(row, row + end):
        for j in range(col, col + end):
            all_sum += board[i][j]
    if all_sum ==0:
        print(0,end="")
    elif all_sum== end*end:
        print(1,end="")
    else:
        print("(" ,end="")
        mid = end//2
        cut(board, row, col , mid)
        cut(board, row, col +mid , mid)
        cut(board, row+ mid , col , mid)
        cut(board,row+mid, col+mid, mid)
        print(")",end="")

n = int(input())
board = [list(map(int , input().strip())) for _ in range(n)]
cut(board,0,0,n)
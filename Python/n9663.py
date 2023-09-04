import sys

n = int(sys.stdin.readline())

answer =0
board =[0] * n


def n_queen(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False
    return True
    

def main (x):
    global answer
    if x ==n:
        answer += 1
        return 
    else:
        for i in range(n):
            board[x] =i
            if n_queen(x)== True:
                main(x+1)

main(0)
print(answer)
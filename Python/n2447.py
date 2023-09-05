import sys


def Kan(list,first,col, last):

    answer = last //3    
    if answer ==0 or answer >last:
        return
    for i in range(first + answer, first +answer*2):
        for j in range(col + answer, col + answer * 2):
            list[i][j]=" "
        
    
    Kan(list,first,col,answer)
    Kan(list ,first ,col +answer ,answer)
    Kan(list ,first , col +answer *2,answer)

    Kan(list,first+answer ,col,answer)
    Kan(list,first+answer ,col +answer*2,answer)
    
    Kan(list,first+answer *2,col,answer)
    Kan(list,first+answer *2,col +answer ,answer)
    Kan(list,first+answer *2,col+answer*2,answer)


n = int(sys.stdin.readline())
list = [["*" for _ in range(n)] for _ in range(n)]
Kan(list , 0,0, n)
# print("".join(list))

for row in list:
    print("".join(row))

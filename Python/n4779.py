import sys

def Kan(list,first, last):
    answer = last //3
    if answer ==0:
        return
    for i in range(first + answer, first +answer*2):
        list[i]=" "
    
    Kan(list,first,answer)
    Kan(list,first + answer*2, answer)


while True:
    try:
        n = int(sys.stdin.readline())
        list= ["-" for i in range(3**n)]
        Kan(list,0,len(list))
        print("".join(list))
    except:
        break
# n = int(sys.stdin.readline())
# list= ["-" for i in range(3**n)]
# Kan(list,0,len(list))
# print("".join(list))

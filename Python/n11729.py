import sys

def hanoi(top, fr , to,by):
    if top ==1:
        print(fr, to)
        return
    else :
        hanoi (top-1,fr,by,to)
        print(fr, to)
        hanoi(top-1,by,to,fr)


n = int(sys.stdin.readline())
print(2**n -1)
a = hanoi(n, 1,3,2)

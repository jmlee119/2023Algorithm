num = int(input())

count=1
if(num==1):
    print(666)
else:
    while True:
        if('666' in str(i)):
            count = count+1
            if(count ==num):
                print(i)
                break


# import sys
# input = sys.stdin.readline

# lst = list(map(int, input().rstrip().split())) => 가로 줄 입력 "1 2 3 4" => ["1", "2", "3", "4"]
# 1234
# lst = list(map(int, input().rstrip())) "1234" => ['1', '2', '3', '4']
# tuple => priority queue heap
# a = [10 ,20 ,3, 5,10, 4]
# sum(a.filter(lambda x : x > 5))

# a = [(0,2, 3), (2,4, 1), (4,1, 2)]
# sorted(a, key= lambda x: x[1])

# sum([i for i in range(0, 101, 2)])

# def f(x):
#     return int(x)
# def g(x, y):
#     return x + y
# g_lambda = lambda x, y : x + y
# g_lambda(3, 5)
# g(3, 5)

# lst = list(map(int, input().rstrip().split()))
# lst = list(map(lambda x : int(x), input().rstrip().split()))
# lst = list(map(f, input().rstrip().split()))


# # 2 - for list
# a = [0] * 100  # [0, 0, 0 ... ,0]
# a = [[0] * 2] * 2
# a = [[0, 0], [0, 0]] # 쓰면 안됨
# visited = [[False *w] for _ in range(h)]  

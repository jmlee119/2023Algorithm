import sys

input = sys.stdin.readline
N = int(input())
# count1 = 1
count2 = 0

# def fibo(n):
#     global count1
#     if n == 1 or n == 2:
#         return 1
#     else:
#         count1 += 1
#         return fibo(n - 1) + fibo(n - 2)


def dpfibo(n):
    global count2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        count2 += 1
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(dpfibo(N), count2)

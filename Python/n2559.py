import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
part_sum = sum(array[:m])
result = [part_sum]
for i in range(n - m):
    part_sum = part_sum - array[i] + array[i + m]
    result.append(part_sum)

print(max(result))

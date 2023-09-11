import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

trees = list(map(int, input().rstrip().split()))
max_tree = max(trees)


def tree_count(n):
    count = 0
    for tree in trees:
        if tree > n:
            count += tree - n
    return count


def binary(start, end, m):
    if start > end:
        return end
    mid = (start + end) // 2
    cnt = tree_count(mid)
    if cnt >= m:
        return binary(mid + 1, end, m)
    else:
        return binary(start, mid - 1, m)


print(binary(1, max_tree, m))

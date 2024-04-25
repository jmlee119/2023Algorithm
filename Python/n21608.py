import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

students = []
N = int(input())

new_borad = [[0] * N for _ in range(N)]

for _ in range(N * N):
    arr = list(map(int, input().split()))
    students.append(arr)


def board(like, st):
    tmp = []
    for i in range(N):
        for j in range(N):
            likes = 0
            blanks = 0
            if new_borad[i][j] == 0:
                for x in range(4):
                    nx = i + dx[x]
                    ny = j + dy[x]

                    if 0 <= nx < N and 0 <= ny < N:
                        if new_borad[nx][ny] in like:
                            likes += 1
                        if new_borad[nx][ny] == 0:
                            blanks += 1
                        tmp.append([likes, blanks, i, j])
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    new_borad[tmp[0][2]][tmp[0][3]] = st[0]


for i in students:
    like = i[1:]
    board(like, i)


score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
# 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
total = 0
for st in students:
    member = st[0]
    like = st[1:]
    count = 0
    for i in range(N):
        for j in range(N):
            if new_borad[i][j] == member:
                for x in range(4):
                    nx = i + dx[x]
                    ny = j + dy[x]
                    if 0 <= nx < N and 0 <= ny < N:
                        if new_borad[nx][ny] in like:
                            count += 1
                total += score[count]


print(total)

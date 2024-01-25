import sys

input = sys.stdin.readline
Testcase = int(input())
for _ in range(Testcase):
    N, K, ID, M = map(int, input().split())
    Team = [[0 for _ in range(K)] for _ in range(N)]  # 문제 번호와 점수
    submit = [0] * N
    time = [0] * N

    for i in range(M):
        Team_id, num, score = map(int, input().split())
        Team[Team_id - 1][num - 1] = max(Team[Team_id - 1][num - 1], score)
        time[Team_id - 1] = i
        submit[Team_id - 1] += 1

    new = []
    for i in range(N):
        new.append([sum(Team[i]), submit[i], time[i], i])
    new.sort(key=lambda x: (-x[0], x[1], x[2]))

    for idx in range(N):
        if new[idx][3] == ID - 1:
            print(idx + 1)
            break

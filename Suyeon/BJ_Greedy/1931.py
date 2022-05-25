import sys

N = int(sys.stdin.readline())
meetings = []
answer = 0

for i in range(N):
    meetings.append(list(map(int,sys.stdin.readline().split())))

meetings.sort()

# start = 0
finish = 0
for meeting in meetings:
    if meeting[0] >= finish: # 안겹치는 경
        answer += 1
        finish = meeting[1]

    elif meeting[1] <= finish: # 포함되면
        finish = meeting[1]


print(answer)


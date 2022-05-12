import sys

N = int(input())
lines = []
last = []


# 전기줄 저장
for _ in range(N) :
    lines.append(list(map(int, sys.stdin.readline().split())))

lines = sorted(lines, key= lambda x : x[0])

# 끝점들 다 저장
for line in lines:
    last.append(line[1])

LIS = [1] * N

for i in range(1,N):
    j = 0
    while j < i:
        if last[j] < last[i]:
            LIS[i] = max(LIS[i], LIS[j] + 1)
        j += 1

print(N-max(LIS))











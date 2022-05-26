import sys

N, cnt = map(int, sys.stdin.readline().split())
numbers = map(int, sys.stdin.readline().split())
subSum = [0] # 누적합 구해두기
sumNumber = 0
answer = []

# 누적합 구하기
for num in numbers:
    sumNumber += num
    subSum.append(sumNumber)

for _ in range(cnt):
    i, j = map(int, sys.stdin.readline().split())
    answer.append(subSum[j] - subSum[i - 1])

for ans in answer:
    print(ans)

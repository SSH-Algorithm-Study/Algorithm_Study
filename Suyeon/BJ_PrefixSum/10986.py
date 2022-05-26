import sys

N, M = map(int,sys.stdin.readline().split())
numbers = map(int, sys.stdin.readline().split())

sumNumber = 0
count = [0] * M

# 누적합의 나머지 저장
for num in numbers:
    sumNumber = (num + sumNumber) % M
    count[sumNumber] += 1

# 누적합끼리 나머지가 같은 것들이 나누어떨어지는 구간 -> Combination으로 구하기
answer = count[0]
for c in count:
    answer += c * (c - 1) / 2



# 타임아웃이 나는 구간 O(N^2)
# for i in range(1, N+1):
#     for j in range(i, N+1):
#         if subRemain[j] == subRemain[i-1]:
#             answer += 1

print(int(answer))



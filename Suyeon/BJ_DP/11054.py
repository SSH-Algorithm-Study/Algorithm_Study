N = int(input())
nums = list(map(int,input().split()))

LIS = [1] * N
LDS = [1] * N

for i in range(1,N):
    j = 0
    while j < i:
        if nums[i] > nums[j]:
            LIS[i] = max(LIS[i], LIS[j] + 1)
        j += 1

for i in range(N-2,-1,-1):
    j = N-1
    while j > i:
        if nums[i] > nums[j]:
            LDS[i] = max(LDS[i], LDS[j] + 1)
        j -= 1


answer = 0

for i in range(0,N):
    answer = max(LIS[i] + LDS[i] - 1, answer)

print(answer)


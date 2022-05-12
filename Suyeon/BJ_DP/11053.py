N = int(input())
nums = list(map(int,input().split()))

LIS = [1] * N

for i in range(1,N):
    j=0
    while j < i:
        if nums[j] < nums[i]:
            LIS[i] = max(LIS[i], LIS[j]+1)
        j += 1
print(max(LIS))

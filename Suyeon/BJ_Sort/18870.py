N = int(input())
nums = list(map(int,input().split()))

##### 다른것 세기
pairs = {}

s_nums = sorted(nums)
pairs[s_nums[0]] = 0

cnt = 0
for i in range(1, N):
    if s_nums[i-1] != s_nums[i]:
        cnt += 1
    pairs[s_nums[i]] = cnt


for num in nums:
    print(pairs[num], end=" ")

#### set

s_nums2 = list(sorted(set(nums)))
pairs2 = { s_nums2[i]:i for i in range(len(s_nums2))}
print(*[pairs2[num] for num in nums])
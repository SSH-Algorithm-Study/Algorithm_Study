answer = input().split()
nums = input().split()

N = int(answer[0])
M = int(answer[1])
numbers = []

def answer(N,M):
    for i in range(N-2):
        max_value = 0
        j = i+1
        k = len(nums)-1
        sum = nums[i] + nums[j] + nums[k]
        while j < k:
            if sum < M:
                max_value = max(sum,max_value) # 갱신
                sum = nums[i] + nums[++j] + nums[k]
            elif sum > M:
                sum = nums[i] + nums[j] + nums[++k]
            else:
                return M

        if sum > M :
            sum = nums[i]







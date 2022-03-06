import itertools

answer = input().split()
nums = input().split()

N = int(answer[0])
M = int(answer[1])
nums = list(map(int, nums))
nums.sort() # 정렬

max_value = 0
def answer(N,M):
    global max_value
    for i in range(N-2):
        j = i+1
        k = len(nums)-1

        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum < M:
                max_value = max(sum,max_value) # 갱신
                j += 1
            elif sum > M:
                k -= 1
            else:
                return M

    return max_value

print(answer(N,M))



def answer(N,M):
    global max_value

    for combi in itertools.permutations(N,3):
        if sum(combi) <= M:
            max_value = max(max_value,sum(combi))






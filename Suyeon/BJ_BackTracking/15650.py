import itertools

N, M = input().split()

for num in itertools.combinations(range(1,int(N)+1), int(M)):
    print(*num)


#################################백트레킹

numbers = range(1,int(N)+1)
result = []



def combination(nums,M):
    if M == 0:
        print(*result)
        return

    for i in range(len(nums)):
        result.append(nums[i])
        combination(nums[i+1:], M-1)
        result.pop()

combination(numbers,int(M))
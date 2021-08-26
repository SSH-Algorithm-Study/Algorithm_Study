def combinationSum(candidates, target):
    result = []
    pre_list = []



    def dfs(start):
        if sum(pre_list) > target:
            return
        if sum(pre_list) == target:
            result.append(pre_list[:])
            return
        for i in range(start,len(candidates)):
            pre_list.append(candidates[i])
            dfs(i)
            pre_list.pop()

    dfs(0)


    return result




combinationSum(candidates = [2,3,6,7], target = 7)

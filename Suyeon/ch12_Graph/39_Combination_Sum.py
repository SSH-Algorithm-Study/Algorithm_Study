def combinationSum(candidates, target):
    result = []
    pre_list = []
    back = 0


    def dfs(start):
        global back
        if sum(pre_list) > target:
            back = 1
            return
        if sum(pre_list) == target:
            result.append(pre_list[:])
            back = 1
            return
        for num in candidates[start:]:
            pre_list.append(num)
            dfs(start)
            if pre_list:
                pre_list.pop()
            if back:
                back = 0
                break

    for i in range(len(candidates)):
        pre_list.clear()
        pre_list.append(candidates[i])
        dfs(i)

    return result



combinationSum(candidates = [2,3,6,7], target = 7)

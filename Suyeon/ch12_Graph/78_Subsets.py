import collections

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(list, start):
            if list:
                result.append(list)
            for i in range(start,len(nums)):
                dfs(list+[nums[i]], i+1)


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = list(range(1, n + 1))

        def dfs(list, start):
            if len(list) == k:
                result.append(list)
                return
            for num in nums[start:]:
                dfs(list + [num], num) #자신의 다음인덱스 요소를 start로

        dfs(list=[], start=0)

        return result




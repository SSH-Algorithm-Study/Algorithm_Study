class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(list, nums):
            if not nums:  # 탈출조건 
                result.append(list)
                return
            for num in nums:
                new_nums = nums.copy() # 참조가 일어나지 않도록
                new_nums.remove(num)
                dfs(list + [num], new_nums)  # list가 아예 변형되지 않도록 + 사용
        # 빈 숫자열 예외처리
        if nums:
            dfs(list=[], nums=nums)

        return result

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:   # 예외처리
            return max(nums)

        dp = []
        dp.append(nums[0])
        dp.append(max(nums[:2]))

        for i in range(2, len(nums)):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1])) # 오른쪽으로 늘려가면서 넣었을 때와 안넣었을 때중 큰거 선택

        return dp[len(nums) - 1]


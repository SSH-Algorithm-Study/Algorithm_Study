class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        dp = []
        dp.append(nums[0])
        dp.append(max(nums[:2]))

        for i in range(2, len(nums)):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))

        return dp[len(nums) - 1]



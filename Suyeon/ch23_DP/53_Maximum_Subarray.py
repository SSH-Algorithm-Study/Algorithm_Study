class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0   # 새로운것에서 그전 까지의 합이 음수이면 첫지점 새로운것으로 다시 맞추기
        return max(nums)



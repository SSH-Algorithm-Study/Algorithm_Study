class Solution:
    def maxSlidingWindow(self, nums, k):

        if len(nums) == 1:
            return nums

        max_val = nums[0]
        max_idx = 0
        result = []

        def findMax(start):
            max_val = nums[start]
            global max_idx
            for i in range(start, k + start):
                if nums[i] >= max_val:
                    max_idx = i
                    max_val = nums[i]

            return max_val

        # 초기값 잡기
        result.append(findMax(0))

        for i in range(1, len(nums)-k+1):
            if max_idx < i:
                max_val = findMax(i)
            else:
                if nums[i] <= nums[i+k-1]:
                    max_idx = i+k-1
                    max_val = nums[i+k-1]
            result.append(max_val)

        return result



sol = Solution()
print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))


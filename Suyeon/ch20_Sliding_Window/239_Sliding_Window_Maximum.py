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

        for i in range(1, len(nums) - k + 1):
            if max_idx < i:
                if max_val > nums[i + k - 1]:
                    max_val = findMax(i)
                else:
                    max_idx = i + k - 1
                    max_val = nums[i + k - 1]
            else:
                if max_val <= nums[i + k - 1]:
                    max_idx = i + k - 1
                    max_val = nums[i + k - 1]

            result.append(max_val)

        return result


class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []

        for i in range(1, len(nums) - k + 1):
            result.append(max(nums[i:i+3]))



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque() # stores *indices*
        res = []
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)
            # remove first element if it's outside the window
            if q[0] == i - k:
                q.popleft()
            # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

sol = Solution()
print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))


import functools

class Solution:
    def cmp(self, x, y):
        if x + y < y + x:
            return 1
        else:
            return -1

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        result = ""

        nums = sorted(nums, key=functools.cmp_to_key(self.cmp))
        if nums[0] == "0":
            return "0"

        for num in nums:
            result = result + num

        return result
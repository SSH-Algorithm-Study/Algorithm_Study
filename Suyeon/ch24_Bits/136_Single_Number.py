import collections

class Solution:
    def singleNumber(self, nums) -> int:
        pair = collections.defaultdict(int)

        for num in nums:
            pair[num] += 1

        for num in nums:
            if pair[num] == 1:
                return num

class Solution:
    def singleNumber(self, nums) -> int:
        for i in range(1,len(nums)):
            nums[0] ^= nums[i] # a xor a = 0 , 0 xor a = a

        return nums[0]

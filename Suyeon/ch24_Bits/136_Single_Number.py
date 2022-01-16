import collections

class Solution:
    def singleNumber(self, nums) -> int:
        pair = collections.defaultdict(int)

        for num in nums:
            pair[num] += 1

        for num in nums:
            if pair[num] == 1:
                return num

import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = collections.Counter(nums)

        return freqs.most_common(1)[0]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = collections.defaultdict(int)

        for num in nums:
            freqs[num] += 1

        for key in freqs:
            if freqs[key] > len(nums)//2:
                return key


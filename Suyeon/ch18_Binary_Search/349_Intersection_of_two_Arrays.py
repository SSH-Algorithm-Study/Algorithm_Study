class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        result = [ num  for num in nums1 if num in nums2 ]

        return result


import collections

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = collections.defaultdict(int)

        for num in nums1:
            dict1[num] += 1

        result = []

        for num in nums2:
            if dict1[num] != 0:
                result.append(num)

        return result

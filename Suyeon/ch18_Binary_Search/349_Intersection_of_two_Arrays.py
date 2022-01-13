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

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()

        nums2.sort()

        for num in nums1:
            first, last = 0, len(nums2)-1

            while first <= last:
                mid = first+(last-first)//2

                if nums2[mid] == num:
                    result.add(num)
                elif nums2[mid] > num:
                    last = mid - 1
                else:
                    first = mid + 1

        return result


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()

        nums1.sort()
        nums2.sort()

        i=j=0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result
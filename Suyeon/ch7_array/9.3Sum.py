class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            first = i + 1
            last = len(nums) - 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            while first < last:
                sum = nums[i] + nums[first] + nums[last]
                if sum == 0:
                    result.append([nums[i], nums[first], nums[last]])
                    while first < last and nums[first] == nums[first + 1]:
                        first += 1
                    while first < last and nums[last] == nums[last - 1]:
                        last -= 1
                    first += 1
                    last -= 1

                elif sum > 0:
                    last -= 1

                else:
                    first += 1
        return result


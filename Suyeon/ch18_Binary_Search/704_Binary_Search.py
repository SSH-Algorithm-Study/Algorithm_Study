class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def BS(left, right):
            if left > right:
                return -1

            mid = left + (right - left) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                return BS(left, mid-1)
            else:
                return BS(mid+1, right)

        return BS(0, len(nums)-1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                right = mid -1
            else:
                left = mid + 1

        return -1

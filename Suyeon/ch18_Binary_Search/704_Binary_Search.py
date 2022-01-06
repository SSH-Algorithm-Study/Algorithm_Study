class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def BS(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                return BS(left, mid-1)
            else:
                return BS(mid+1, right)

        return BS(0, len(nums)-1)
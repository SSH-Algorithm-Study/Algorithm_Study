class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = -1

        # pivot 값 찾기
        while pivot > -len(nums):
            if nums[pivot] < nums[pivot - 1]:
                break

            pivot -= 1

        # 이진탐색진행
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid + pivot] == target:
                if mid + pivot < 0: # index 음수면 양수로 변환
                    return len(nums) + (mid + pivot)
                else:
                    return mid + pivot
            elif nums[mid + pivot] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

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

# 이진탐색 새로운 기준
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums)-1


        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[right]: # pivot이 왼쪽에 존재할 경우
                if nums[mid] <= target and target <= nums[right]: # target이 mid와 right의 사이값이면 그 사이에 존재
                    left = mid + 1
                else: # 아니라면 왼쪽편에 target 존재
                    right = mid - 1

            if nums[mid] >= nums[left]: # pivot이 오른쪽에 존재할 경우
                if nums[mid] >= target and nums[left] <= target: # target이 mid와 left의 사이값이면 그 사이에 존재
                    right = mid - 1
                else: # 아니라면 오른편에 target 존재
                    left = mid + 1

        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        # 최소값 인덱스 찾기
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # target 찾기
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            mid_pivot = (mid+pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1

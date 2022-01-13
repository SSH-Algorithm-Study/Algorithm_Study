class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while i < j:
            if numbers[i] + numbers[j] > target:
                j = j - 1

            elif numbers[i] + numbers[j] < target:
                i = i + 1

            else:
                return [i+1,j+1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k+1, len(numbers)-1 # k보다 오른쪽에서 탐색 앞쪽은 이미 탐색했으므로
            target = target - v

            while left <= right:
                mid = left + (right-left)//2

                if numbers[mid] < target :
                    left = mid + 1
                elif numbers[mid] > target:
                    right = mid -1
                else:
                    return k+1, mid+1
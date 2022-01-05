class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = 0
        tail = len(nums)-1
        i = 0

        while i <= tail:
            if nums[i] == 0:
                if head == i: # 자리 교환이 필요 없는 경우 다음 것으로 가기
                    i = i+1
                else:
                    nums[head], nums[i] = nums[i], nums[head]
                head = head + 1
            elif nums[i] == 2:
                nums[tail], nums[i] = nums[i], nums[tail]
                tail = tail - 1
            else: # 1일때는 한칸 나아가기 
                i = i + 1

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):  # 음수로 만들어서 최대힙구할수있게
            nums[i] = -1 * nums[i]

        heapq.heapify(nums)  # heap으로 만들어주기

        for _ in range(k-1):
            heapq.heappop(nums) # k-1번 pop하기

        return -1 * heapq.heappop(nums)    # 반환할때 음수처리 다시 해주기




class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        return heapq.nlargest(k,nums)[-1]

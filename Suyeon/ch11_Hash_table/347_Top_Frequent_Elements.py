import collections
import heapq

# most_common()이용
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        result = []

        for pair in freqs.most_common(k):
            print(pair)
            result.append(pair[0])

        return result

# heap이용
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        heap = []
        result = []

        for key in freqs:
            heapq.heappush(heap, (-freqs[key],key) )   # 키와 값을 바꾸고 값은 음수로
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])  # 값을 넣기

        return result


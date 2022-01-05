class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key= lambda x : x[0]**2 + x[1]**2)

        return points[:k]


import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        result = []
        for i,point in enumerate(points):
            heapq.heappush(pq, (point[0]**2 + point[1]**2, i))

        for i in range(k):
            result.append(points[heapq.heappop(pq)[1]])

        return result
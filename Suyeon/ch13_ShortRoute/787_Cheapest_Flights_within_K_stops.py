import heapq
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        pairs = [(0, src, -1)]  # 최소 우선순위 큐
        info = collections.defaultdict(list)  # 초기연결정보

        for flight in flights:
            info[flight[0]].append((flight[1], flight[2]))

        while pairs:
            price, node, middle = heapq.heappop(pairs)
            if node == dst:
                return price
            if middle < k:  # 지금까지 경유지가 K 미만일때만 이웃고려
                for n, p in info[node]:  # 이웃경로정보넣어주기
                    heapq.heappush(pairs, (p + price, n, middle + 1))

        return -1


def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    pairs = [(0, src, k)]  # 최소 우선순위 큐
    info = collections.defaultdict(list)  # 초기연결정보

    for flight in flights:
        info[flight[0]].append((flight[1], flight[2]))

    while pairs:
        price, node, middle = heapq.heappop(pairs)
        if node == dst:
            return price
        if middle < k:  # 지금까지 경유지가 K 미만일때만 이웃고려
            for n, p in info[node]:  # 이웃경로정보넣어주기
                heapq.heappush(pairs, (p + price, n, middle + 1))

    return -1
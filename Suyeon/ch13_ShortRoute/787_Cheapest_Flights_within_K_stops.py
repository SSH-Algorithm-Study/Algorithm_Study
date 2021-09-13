import heapq
import collections

def findCheapestPrice( n: int, flights, src: int, dst: int, k: int) -> int:
    result = collections.defaultdict()  # 시작점부터 노드까지의 최단거리
    pairs = [(0, src, -1)]  # 최소 우선순위 큐
    info = collections.defaultdict(list) # 초기연결정보

    for flight in flights:
        info[flight[0]].append((flight[1], flight[2]))


    while pairs:
        price, node, middle = heapq.heappop(pairs)
        if middle > k:  # 경유지가 k가 넘으면 더 이상 필요없는 경로
            continue
        if not result[node]:  # 이제까지 k이내의 최소 경로가 없었다면 넣어주기
            result[node] = price
        for n, p in info[node]: # 이웃경로정보넣어주기
            heapq.heappush(pairs, (p+price, n, middle+1))

    if result[dst]:
        return result[dst]
    else:
        return -1

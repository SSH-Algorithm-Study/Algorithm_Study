import heapq
import collections

def findCheapestPrice( n: int, flights, src: int, dst: int, k: int) -> int:
    dist = collections.defaultdict(tuple)  # 시작점부터 노드까지의 최단거리
    pairs = [(0, src, -1)]  # 최소 우선순위 큐
    info = collections.defaultdict(list) # 초기연결정보

    for flight in flights:
        info[flight[0]].append((flight[1], flight[2]))

    while pairs:
        print(dist)
        print(pairs)
        cost, node, mid = heapq.heappop(pairs)
        if mid < k and dist
        if node not in dist or (node in dist and dist[node][1]) > k:  # 없다면 넣어주기
            dist[node] = (cost, mid)
            for n, c in info[node]: # 이웃노드들 정보가져오기
                heapq.heappush(pairs, (c+cost, n, mid+1 ))


    if dist[dst] and dist[dst][1] <= k :
        return dist[dst][0]
    else:
        return -1


print(findCheapestPrice(4,
[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
0,
3,
1))
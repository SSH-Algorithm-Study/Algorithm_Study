import collections

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         result = 0
#         d = collections.defaultdict(list)
#         queue = collections.deque()
#
#         for time in times: # 주어진 거리정보 저장
#              d[time[0]].append((time[1], time[2]))
#
#         for pair in d[k]: # 시작점 바로다음 지점들 스택에 저장
#             queue.append(pair)
#
#         while queue:
#             cur = queue.popleft()
#             if not d[cur[0]]:
#                 result = max(result, cur[1])
#
#             for pair in d[cur[0]]:
#                 next = (pair[0], cur[1] + pair[1])
#                 queue.append(next)
#
#         return result
#
# def networkDelayTime( times, n: int, k: int) -> int:
#     INF = 1000000
#     inf = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         inf[i][i] = 0
#
#     for time in times:  # 거리정보 채우기
#         inf[time[0]][time[1]] = time[2]
#
#     d = inf[k].copy()  # 시작점에서 각 노드까지 최단거리
#     v = [0] * (n + 1)  # 각 노드들 방문 여부
#     v[k] = 1  # 시작점은 방문한 것으로 취급
#
#     queue = collections.deque()
#
#     for i, val in enumerate(d):
#         if val != INF and i != k:
#             queue.append(i)
#
#     while queue:
#         print(queue)
#         cur = queue.popleft()
#         v[cur] = 1
#         print(inf[cur])
#         for i, val in enumerate(inf[cur]):
#             if val != INF and v[i] == 0:
#                 if d[i] > val + d[cur]:  # i까지의 최단거리가 더 짧으면 갱신
#                     d[i] = val + d[cur]
#                 queue.append(i)  # 아직 방문하지 않은 다음 노드 추가
#
#     print(v)
#     if sum(v) < n:
#         return -1
#     else:
#         return max(d[1:])
#
# print(networkDelayTime([[1,2,1],[2,3,2],[1,3,1]],3,2))





def networkDelayTime( times, n: int, k: int) -> int:
    INF = 1000000
    inf = [[INF for _ in range(n)] for _ in range(n)]

    for i in range(n):
        inf[i][i] = 0

    for time in times:  # 거리정보 채우기
        inf[time[0]-1][time[1]-1] = time[2]

    d = inf[k-1] # 시작점에서 각 노드까지 최단거리
    v = [0] * n  # 각 노드들 방문 여부
    v[k-1] = 1  # 시작점은 방문한 것으로 취급

    stack = []

    for i, val in enumerate(d):
        if val != INF and i != k-1:
            stack.append(i)


    while stack:
        print(stack)
        cur = stack.pop()
        v[cur] = 1
        for i, val in enumerate(inf[cur]):
            if val != INF and v[i] == 0: # 방문하지 않은 이웃노드
                if d[i] > val + d[cur]:  # i까지의 최단거리가 더 짧으면 갱신
                    d[i] = val + d[cur]
                stack.append(i)  # 아직 방문하지 않은 다음 노드 추가


    if sum(v) < n:
        return -1
    else:
        return max(d[1:])


import heapq

def networkDelayTime( times, n: int, k: int) -> int:
    inf = collections.defaultdict(list)

    for time in times: # 정보저장
        inf[time[0]].append((time[1], time[2]))

    pairs = [(0, k)]
    dist = {}

    while pairs:
        time, node = heapq.heappop(pairs)
        if node not in dist: # 없을 때만 추가
            dist[node] = time
            for v, w in inf[node]:
                heapq.heappush(pairs, (w+time,v))  # node를 바로지나게하는 이웃노드까지의 시간


    if len(dist) == n:
        return max(dist.values())

    else:
        return -1

# tuple 받을 때  a,b 분리해서 


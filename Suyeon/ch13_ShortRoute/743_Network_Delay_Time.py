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

def networkDelayTime( times, n: int, k: int) -> int:
    INF = 1000000
    inf = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        inf[i][i] = 0

    for time in times:  # 거리정보 채우기
        inf[time[0]][time[1]] = time[2]

    d = inf[k].copy()  # 시작점에서 각 노드까지 최단거리
    v = [0] * (n + 1)  # 각 노드들 방문 여부
    v[k] = 1  # 시작점은 방문한 것으로 취급

    queue = collections.deque()

    for i, val in enumerate(d):
        if val != INF and i != k:
            queue.append(i)

    while queue:
        print(queue)
        cur = queue.popleft()
        v[cur] = 1
        print(inf[cur])
        for i, val in enumerate(inf[cur]):
            if val != INF and v[i] == 0:
                if d[i] > val + d[cur]:  # i까지의 최단거리가 더 짧으면 갱신
                    d[i] = val + d[cur]
                queue.append(i)  # 아직 방문하지 않은 다음 노드 추가

    print(v)
    if sum(v) < n:
        return -1
    else:
        return max(d[1:])

print(networkDelayTime([[1,2,1],[2,3,2],[1,3,1]],3,2))














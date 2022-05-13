import collections
import heapq


def solution(n, edge):
    linked = collections.defaultdict(list)
    distance = [float('inf')] * (n + 1)

    # 경로저장
    for e in edge:
        linked[e[0]].append(e[1])

    pq = []

    heapq.heappush(pq, (0, 1))

    while pq:
        dis, mid = heapq.heappop(pq)

        if distance[mid] > dis:
            distance[mid] = dis
            for child in linked[mid]:
                heapq.heappush(pq, (dis + 1, child))

    answer = 0

    for d in distance:
        if d != float('inf'):
            answer = max(answer, d)

    return answer + 1

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	 ))
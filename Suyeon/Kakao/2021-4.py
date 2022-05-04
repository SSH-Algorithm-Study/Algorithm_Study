import collections
import heapq


def solution(n, s, a, b, fares):
    graph = collections.defaultdict(list)

    for fare in fares:
        graph[fare[0]].append(fare[1:])
        graph[fare[1]].append([fare[0],fare[2]])

    distance = [ [float('inf')] * (n+1) for _ in range(n+1) ]

    # 초기화
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                distance[i][j] = 0


    for start in range(1,n+1):
        queue = []
        heapq.heappush(queue, (0, start))

        while queue:
            dis, mid = heapq.heappop(queue)
            for node, d in graph[mid]:
                if dis + d < distance[start][node]:
                    distance[start][node] = dis + d
                    heapq.heappush(queue, (dis+d, node))

    mid = list(range(1,n+1))

    print(distance)

    result = []
    for m in mid:
        result.append(distance[s][m] + distance[m][a] + distance[m][b])

    return min(result)


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
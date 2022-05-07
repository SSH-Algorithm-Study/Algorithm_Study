import collections
import heapq


def solution(n, paths, gates, summits):
    routes = collections.defaultdict(list)
    for path in paths:
        routes[path[0]].append([path[1], path[2]])
        routes[path[1]].append([path[0], path[2]])

    answer = [-1 , float('inf')]
    for gate in gates:
        costs = [float('inf')] * (n+1)
        sum_costs = [flo]
        children = []
        heapq.heappush(children, (0, gate, gate))

        while children:
            intensity, mid, parent = heapq.heappop(children)
            if costs[mid] > intensity:
                costs[mid] = intensity
            if mid not in summits:
                for node, inten in routes[mid]:
                    if node != parent and node not in gates:
                        if intensity < inten:
                            heapq.heappush(children, (inten, node, mid))
                        else:
                            heapq.heappush(children, (intensity, node, mid))



        for summit in summits:
            if costs[summit] < answer[1]:
                answer[0] = summit
                answer[1] = costs[summit]


    return answer

print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3],[5]))

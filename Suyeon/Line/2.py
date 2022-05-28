# 줄 N개로 딱 맞게 잘라야함
import heapq


def solution(n, times):
    cost = [float('inf')] * (n + 1)
    works = [(0, 1)]

    while works:
        time, lines = heapq.heappop(works)
        if cost[lines] > time:  # 최소값 갱신
            cost[lines] = time
        for i in range(1, lines + 1):
            if lines + i <= n: # n 넘는 것은 작업하지 않도록
                heapq.heappush(works, (time + times[i-1], lines + i))

    return cost[n]


print(solution(5,[2, 4, 5]))

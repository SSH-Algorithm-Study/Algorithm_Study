import heapq
import copy


def solution(alp, cop, problems):
    def is_valid(a, c):
        if 0 <= a <= 150 and 0 <= c <= 150:
            return True
        return False

    answer = float("inf")

    costs = [[float('inf')] * (151) for _ in range(151)]
    children = []

    heapq.heappush(children, [0, alp, cop, set()])

    while children:
        time, ap, cp, solve = heapq.heappop(children)
        if len(solve) == len(problems):
            answer = min(answer, time)
            continue
        if is_valid(ap, cp):
            if costs[ap][cp] > time:
                costs[ap][cp] = time
                # 문제를 풀거나
                for i, problem in enumerate(problems):
                    if ap >= problem[0] and cp >= problem[1]:
                        solve2 = copy.deepcopy(solve)
                        solve2.add(i)
                        heapq.heappush(children, [time + problem[4], ap + problem[2], cp + problem[3], solve2])
                # 기술연마
                heapq.heappush(children, [time + 1, ap + 1, cp, copy.deepcopy(solve)])
                heapq.heappush(children, [time + 1, ap, cp+1, copy.deepcopy(solve)])

    return answer


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))

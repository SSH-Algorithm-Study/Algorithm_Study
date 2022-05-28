# N개의 우주선 , 각자 다른 목적지
# 연료 적절 배분(양수)
# p인 우주선에 m채우면 p씩 속도 늘어나는 등가속운동 m초동안 -> 이후 등속
# 넓이 : m * mp + mpk
# 나눠갖는 모든 경우 수 = (fuel - 1) C (우주선수 - 1)
import itertools

# 비행시간 계산
def flight(min,pow,dis):
    # print(min, pow, dis)
    total = pow / 2
    time = 1
    pre = total

    for _ in range(min-1):
        if total >= dis:
            return time
        time += 1
        total += pow + pre
        pre += pow

    v = min * pow
    while total < dis:
        total += v
        time += 1

    return time


def solution(fuel, powers, distances):
    answer = float('inf')
    if len(powers) == 1:
        return flight(fuel,powers[0],distances[0])
    for pair in itertools.combinations(range(1,fuel), len(powers)-1):
        sub = []
        sub.append(flight(pair[0], powers[0], distances[0]))
        for i in range(len(powers)-2):
            sub.append(flight(pair[i+1]-pair[i], powers[i+1], distances[i+1]))
        sub.append(flight(fuel-pair[-1], powers[-1], distances[-1]))

        answer = min(answer, max(sub))
    return answer

print(solution(10,[5],[200]	))

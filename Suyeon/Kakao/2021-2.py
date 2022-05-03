import itertools
import collections

def solution(orders, course):
    answer = []

    for c in course:
        count = collections.defaultdict(int)
        for order in orders:
            if len(order) >= c:
                for combi in itertools.combinations(sorted(order),c):
                    count["".join(combi)] += 1

        if count:
            count = sorted(count.items(), key=lambda x : -x[1])
            i = 0
            maximum = count[0][1]
            if maximum > 1:
                while i < len(count) and count[i][1] == maximum:
                    answer.append(count[i][0])
                    i += 1


    return sorted(answer)


print(solution(["XYZ", "XWY", "WXA"],[2, 3, 4]))
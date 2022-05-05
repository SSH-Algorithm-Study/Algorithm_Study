import sys
import collections


def solution(gems):
    kind = len(set(gems))

    min_length = sys.maxsize
    answer = []
    have = collections.defaultdict(int)

    i, j = 0, 0
    have[gems[0]] += 1

    while j < len(gems):
        print(have)
        if len(have.keys()) == kind:
            if j - i + 1 < min_length:
                answer = [i+1,j+1]
                min_length = j-i+1
            if have[gems[i]] == 1:
                del have[gems[i]]
            else:
                have[gems[i]] -= 1
            i += 1

        else:
            j += 1
            if j < len(gems):
                have[gems[j]] += 1



    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
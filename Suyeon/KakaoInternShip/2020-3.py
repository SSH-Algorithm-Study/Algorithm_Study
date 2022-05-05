import sys


def solution(gems):
    kind = len(set(gems))
    if kind == 1:
        return [1,1]

    min_length = sys.maxsize
    answer = []

    i, j = 0, 1
    # and로 묶으면 다른 것들도 같이 걸러질 수 있음.. 풀어서!!
    while j < len(gems):
        if len(set(gems[i:j+1])) == kind:
            if j - i + 1 < min_length:
                answer = [i+1,j+1]
                min_length = j-i+1
            i += 1

        else:
            j += 1


    return answer
print(solution(["a","a","a","a","a","a","a","b","c"]))
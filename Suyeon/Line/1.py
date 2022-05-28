# 이름 중복 없음
# 사전 순 정렬
# 공백으로 구분
import collections


def solution(logs):
    answer = []
    solve_user = set()
    solve_prob = collections.defaultdict(int)

    for log in set(logs):  # 문제 중복 제거
        user, prob = log.split()
        solve_user.add(user)
        solve_prob[prob] += 1

    solve_prob = sorted(solve_prob.items(), key=lambda x: (-x[1], x[0]))

    half = len(solve_user) / 2
    print(half)
    print(solve_prob)
    for prob in solve_prob:
        if prob[1] < half:
            break
        answer.append(prob[0])

    return answer


print(solution(["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"]))

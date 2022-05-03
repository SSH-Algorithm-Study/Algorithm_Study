import collections
import bisect

def solution(info, query):
    queries = collections.defaultdict(list)
    answer = []

    def dfs(condition, q, n):
        if n == 4:
            queries[q].append(int(condition[n]))
            return

        dfs(condition, q+condition[n], n+1)
        dfs(condition, q+"-", n+1)


    for i in info:
        dfs(i.split(), "", 0)

    for key in queries.keys():
        queries[key].sort()

    for q in query:
        score = int(q.split()[-1])
        scores = queries["".join(q.split()[:-1]).replace("and","")]
        start = bisect.bisect_left(scores, score)
        answer.append(len(scores)-start)



    return answer



print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))












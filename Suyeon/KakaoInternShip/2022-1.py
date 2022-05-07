def solution(survey, choices):
    type = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    matching = {1:[0,3], 2:[0,2], 3:[0,1], 5:[1,1], 6:[1,2], 7:[1,3]}
    answer = ""

    for i,v in enumerate(survey):
        c = choices[i]
        if c == 4:
            continue
        type[v[matching[c][0]]] += matching[c][1]

    print(type)

    if type["R"] >= type["T"]:
        answer += "R"
    else:
        answer += "T"

    if type["C"] >= type["F"]:
        answer += "C"
    else:
        answer += "F"

    if type["J"] >= type["M"]:
        answer += "J"
    else:
        answer += "M"

    if type["A"] >= type["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))

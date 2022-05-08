def solution(line):
    L = ["1","2","3","4","5", "Q", "W", "E", "R", "T"]
    R = ["6", "7", "8", "9", "0", "Y", "U", "I", "O", "P"]

    pos = {
        "1": [0,0], "2":[0,1], "3": [0,2], "4": [0,3], "5": [0,4], "6":[0,5], "7":[0,6], "8":[0,7], "9":[0,8], "0":[0,9],
        "Q": [1,0], "W":[1,1], "E":[1,2], "R":[1,3], "T":[1,4], "Y":[1,5], "U":[1,6], "I":[1,7], "O":[1,8], "P":[1,9],
    }
    l_cur = "Q"
    r_cur = "P"

    def distance(a,b):
        return (abs(pos[a][0] - pos[b][0]) , abs(pos[a][1] - pos[b][1])) # 수직, 수평

    def whichHand(input):
        l_v, l_h = distance(l_cur, input)
        r_v, r_h = distance(r_cur, input)
        if l_v+l_h == r_v + r_h:
            if l_h < r_h:
                return 0
            elif l_h > r_h:
                return 1
            else:
                if input in L:
                    return 0
                else:
                    return 1
        elif l_v+l_h > r_v + r_h:
            return 1
        else:
            return 0

    answer = []
    for i in line:
        hand = whichHand(i)
        answer.append(hand)
        if hand:
            r_cur = i
        else:
            l_cur = i

    return answer

print(solution("Q4OYPI"))
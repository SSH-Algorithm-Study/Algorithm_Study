def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solution(numbers, hand):
    L = [1, 4, 7]
    R = [3, 6, 9]

    # 해당 숫자의 위치좌표
    position = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1],
    }
    # 처음위치
    l_pos = [3,0]
    r_pos = [3,2]

    answer = ''

    for num in numbers:
        if num in L: # 좌측번호
            answer += "L"
            l_pos = position[num]
        elif num in R: # 우측번호
            answer += "R"
            r_pos = position[num]
        else: # 가운데 번호
            if distance(l_pos,position[num]) > distance(r_pos, position[num]): # 오른쪽손이 더 가까움
                answer += "R"
                r_pos = position[num]
            elif distance(l_pos,position[num]) < distance(r_pos, position[num]): # 왼쪽손이 더 가까움
                answer += "L"
                l_pos = position[num]
            else:  # 같은 거리
                if hand == "left": # 왼손잡이
                    answer += "L"
                    l_pos = position[num]
                else: # 오른손잡이
                    answer += "R"
                    r_pos = position[num]


    return answer

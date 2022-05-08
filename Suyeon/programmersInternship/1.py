def mise(number):
    if number <= 30:
        return 0
    elif 31 <= number <= 80:
        return 1
    elif 81 <= number <= 150:
        return 2
    else:
        return 3

def chomise(number):
    if number <= 15:
        return 0
    elif 16 <= number <= 35:
        return 1
    elif 36 <= number <= 75:
        return 2
    else:
        return 3



def solution(atmos):
    mask = False # 개봉여부
    day = 0 #사용기간
    count = 0 # 총사용 마스크
    for m,c in atmos:
        if mask: # 마스크 개봉중
            day += 1
        if mise(m) >= 2 or chomise(c) >= 2:
            if not mask:
                mask = True
                count += 1
            if mise(m) == 3 and chomise(c) == 3:
                day = 0
                mask = False
        if day == 2:
            day = 0
            mask = False


    return count

print(solution(
[[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]))
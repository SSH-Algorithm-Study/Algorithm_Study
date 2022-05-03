def solution(new_id):
    notAllow = list("~!@#$%^&*()=+[{]}:?,<>/")


    #1단계
    new_id = new_id.lower()

    #2단계
    for ch in new_id:
        if ch in notAllow:
            new_id = new_id.replace(ch,"")

    #3단계
    dot = False
    length = len(new_id)
    i = 0
    while i < length:
        if new_id[i] == ".":
            if dot:
                new_id = new_id[:i] + new_id[i+1:]
                length -= 1
            else:
                i += 1
            dot = True
        else:
            dot = False
            i +=  1


    #4단계
    if new_id and new_id[0] == ".":
        if len(new_id) == 1:
            new_id = "a"
        else:
            new_id = new_id[1:]

    if new_id and new_id[-1] == ".":
        if len(new_id) == 1:
            new_id = "a"
        else:
            new_id = new_id[:-1]

    if not new_id:
        new_id = "a"

    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    elif len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]


    return new_id


print(solution("z-+.^."))
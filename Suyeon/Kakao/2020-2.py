def opposite(p):
    answer = ""
    for i in p:
        if i == "(":
            answer + ")"
        else:
            answer + "("

    return answer


def partition(p):
    stack = []

    for i in range(len(p)):
        if(len(stack) != 0 and stack[-1] != p[i]):
            stack.pop()
            if not stack:
                return (p[:i+1], p[i+1:])
        else:
            stack.append(p[i])


def isPerfect(p):
    stack = []

    for i in p:
        if(len(stack) != 0 and stack[-1] == "(" and i ==")"):
            stack.pop()
        else:
            stack.append(i)

    return not stack

def solution(p):
    if not p or isPerfect(p):
        return p

    u, v = partition(p)

    if isPerfect(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + opposite(u[1:-1])




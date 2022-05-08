import itertools

def partition(expression):
    expression = expression.replace("-", " - ")
    expression = expression.replace("*", " * ")
    expression = expression.replace("+", " + ")

    return expression.split()


def make_post_expression(expression, order):
    order_dict = {v : i for i,v in enumerate(order)}
    result = []
    operator = []
    expression = partition(expression)

    for i,v in enumerate(expression):
        if i%2 == 0: # 숫자
            result.append(v)
        else:
            while len(operator) != 0 and order_dict[operator[-1]] >= order_dict[v]:
                result.append(operator.pop())
            operator.append(v)

    while len(operator) != 0:
        result.append(operator.pop())


    return result

def basic(a,b,opt):
    if opt == "+":
        return a+b
    elif opt == "-":
        return a-b
    else:
        return a*b

def calculator(expression):
    stack = []

    for e in expression:
        if e.isdigit():
            stack.append(int(e))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(basic(a,b,e))

    return abs(stack.pop())



def solution(expression):
    answer = 0
    operator = []
    if "+" in expression:
        operator.append("+")
    if "-" in expression:
        operator.append("-")
    if "*" in expression:
        operator.append("*")


    orders = itertools.permutations(operator, len(operator))

    for order in orders:
        answer = max(answer,calculator(make_post_expression(expression,order)))



    return answer

print(solution("100-200*300-500+20"	))
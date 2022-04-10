N = int(input())
nums = list(map(int, input().split()))
operator = { i : v for i,v in enumerate(list(map(int, input().split()))) }
result = set()

def calculate(a,b,opt):
    if opt == 0: # 덧셈
        return a+b
    elif opt == 1:  # 뺄셈
        return a-b
    elif opt == 2: # 곱셈
        return a*b
    else:
        if a < 0 :
            return ((-1 * a) // b ) * -1
        else:
            return a//b


def dfs(a,n):
    if n == N:
        result.add(a)
        return

    for opt in operator.keys():
        if operator[opt] == 0:
            continue

        operator[opt] -= 1
        dfs(calculate(a,nums[n],opt), n+1)
        operator[opt] += 1


dfs(nums[0],1)
print(max(result))
print(min(result))



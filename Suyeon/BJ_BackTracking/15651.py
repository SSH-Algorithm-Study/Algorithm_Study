N, M = input().split()
result = []
list = range(1,int(N)+1)

def permu(M):
    if M == 0:
        print(*result)
        return

    for num in list:
        result.append(num)
        permu(M-1)
        result.pop()


permu(int(M))
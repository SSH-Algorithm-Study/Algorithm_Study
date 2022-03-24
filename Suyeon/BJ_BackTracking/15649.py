###### 순열함수
import itertools

N, M =input().split()

for nums in list(itertools.permutations(range(1,int(N)+1),int(M))):
    print(*nums)


###### 백트레킹

N, M =input().split()
result = []

def dfs(list, M):
    if M == 0:
        print(*result)
        return

    for num in list:
        result.append(num)
        temp = list[:]
        temp.remove(num)
        dfs(temp,M-1)
        result.remove(num)

dfs(list(range(1,int(N)+1)), int(M))







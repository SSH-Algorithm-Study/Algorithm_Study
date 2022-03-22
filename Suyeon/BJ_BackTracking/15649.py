###### 순열함수
import itertools

N, M =input().split()

for nums in list(itertools.permutations(range(1,int(N)+1),int(M))):
    print(*nums)


###### 백테킹

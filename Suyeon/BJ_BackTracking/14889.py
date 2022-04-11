import sys
import itertools
input = sys.stdin.readline
result = sys.maxsize

N = int(input())
synergy = []
for i in range(N):
    synergy.append(list(map(int, input().split())))

print(synergy)

for memberA in itertools.combinations(range(0,N), N//2):
    memberB = [ mem for mem in range(0,N) if mem not in memberA ]
    synergyA = 0
    synergyB = 0
    print(memberA, memberB)

    for pair in itertools.combinations(memberA, 2):
        synergyA += synergy[pair[0]][pair[1]]
        synergyA += synergy[pair[1]][pair[0]]

    for pair in itertools.combinations(memberB, 2):
        synergyB += synergy[pair[0]][pair[1]]
        synergyB += synergy[pair[1]][pair[0]]

    result = min(result,abs(synergyA - synergyB))


print(result)








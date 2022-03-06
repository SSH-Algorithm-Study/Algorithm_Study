N = int(input())
students= []
bigger = {}
answer = [0] * N
# answer = [0 for _ in range(N)]

for _ in range(N):
    students.append(list(map(int,input().split())))

for i in range(N): #리스트 내포로 가능
    bigger[i] = 0


for i in range(N-1):
    for j in range(i+1,N):
        if students[i][1] > students[j][1] and students[i][0] > students[j][0] :
            bigger[j] += 1
        elif students[i][1] < students[j][1] and students[i][0] < students[j][0] :
            bigger[i] += 1


for i in range(N):
    answer[i] = bigger[i]+1

print(*answer)
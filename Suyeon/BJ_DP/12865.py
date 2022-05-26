import sys

N, limitWeight = map(int,sys.stdin.readline().split())
items = []
dp = [[-1] * (limitWeight + 1) for i in range(N)]

def board():
    for d in dp:
        print(d)
    print("-----------------------")

### 데이터 넣기 ###
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    items.append([w,v])

def knapsack(i,j):
    if i < 0 or j < 0:
        return 0

    weight, value = items[i]
    if dp[i][j] == -1: # 값 업다면
        if j-weight < 0: # i추가 불가능
            dp[i][j] = knapsack(i-1,j)
        else:  # i추가 가능
            dp[i][j] = max(knapsack(i-1, j-weight) + value, knapsack(i-1,j))


    return dp[i][j]


knapsack(N-1,limitWeight)

print(dp[N-1][limitWeight])



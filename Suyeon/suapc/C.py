import sys
input = sys.stdin.readline

N, M = list((map(int, input().split())))
chess = []

for _ in range(N):  # 체스판채우기
    chess.append(input().split())

dp = [[[0 for _ in range(N)] for _ in range(M)] for _ in range(3000)]

def chess():
    size = 2

    for i in range(N):
        for j in range(M):
            dp[i][j][1] = 1

    while True:
        i = 0
        j = 0
        while i+size <= N:
            while j+size <=N:
                if dp[i][j][size-1] and dp[i+1][i][size-1] and dp[i]
            dp[i][j][size] = 1








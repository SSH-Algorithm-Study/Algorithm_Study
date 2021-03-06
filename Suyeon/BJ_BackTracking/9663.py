# N = int(input())
# chess = [ [0 for i in range(N+1)] for j in range(N+1) ]
# count = 0
# queens = []
#
# def showChess():
#     for i in range(N+1):
#         print(chess[i])
#
# def sero0(i,j):
#     for a in range(i+1,N+1):
#         chess[a][j] = 0
#
# def sero1(i,j):
#     for a in range(i+1,N+1):
#         chess[a][j] = 1
#
# def diagonal0(i,j):
#     k = 1
#     while j-k > 0 and i+k < N+1:
#         chess[i+k][j-k] = 0
#         k += 1
#
#     k = 1
#     while j+k < N+1 and i+k < N+1:
#         chess[i+k][j+k] = 0
#         k += 1
#
# def diagonal1(i, j):
#     k = 1
#     while j - k > 0 and i + k < N + 1:
#         chess[i + k][j - k] = 1
#         k += 1
#
#     k = 1
#     while j + k < N + 1 and i + k < N + 1:
#         chess[i + k][j + k] = 1
#         k += 1
#
#
# def NQuuen(i):
#     global count
#     if i == N+1:
#         count += 1
#         return
#
#     for j in range(1,N+1):
#         for queen in queens:
#             sero1(queen[0],queen[1])
#             diagonal1(queen[0],queen[1])
#         if chess[i][j] == 0:
#             queens.append((i,j))
#             NQuuen(i+1) # 재귀
#             for queen in queens:
#                 sero0(queen[0], queen[1])
#                 diagonal0(queen[0], queen[1])
#             queens.pop()
#
# NQuuen(1)
# print(count)




################ 더 간단하게 규칙확인

N = int(input())
queens = [0] * (N+1)
count = 0

def isOk(i,j):
    for k in range(1, i):
        if queens[k] == j: # 세로
            return False
        if abs(k - i) == abs(queens[k] -j): # 대각선
            return False

    return True


def NQueen(i) :
    global count
    if i == N+1:
        count += 1
        return

    for j in range(1,N+1):
        if(isOk(i,j)): # pruning
            queens[i] = j
            NQueen(i+1)
            queens[i] = 0 # back


NQueen(1)
print(count)


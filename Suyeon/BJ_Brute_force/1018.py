import sys

first = input().split()
row = int(first[0])
col = int(first[1])

board = []
result = sys.maxsize

for _ in range(row):
    board.append(list(input()))

def isChess(x,y):
    std = ['W','B']
    change = [0,0]

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0: # 변화량이 짝수
                if board[x+i][y+j] == std[0]:
                    change[1] += 1
                else:
                    change[0] += 1
            else: # 변화량이 홀수
                if board[x+i][y+j] == std[0]:
                    change[0] += 1
                else:
                    change[1] += 1

    return min(change)

for i in range(row-7):
    for j in range(col-7):
        result = min(result,isChess(i,j))

print(result)
N = int(input())
chess = [ [0 for i in range(N+1)] for j in range(N+1) ]
count = 0

def sero0(i,j):
    for a in range(i+1,N+1):
        chess[a][j] = 0;

def sero1(i,j):
    for a in range(i+1,N+1):
        chess[a][j] = 1;

def diagonal0(i,j)
    for

def diagonal1(i, j)
    for


def NQuuen(i):
    global count

    if i == N+1:
        count += 1
        return

    for j in range(N+1):
        if chess[i][j] == 0:
            chess[i][j] = 1
            sero1(i,j)
            diagonal1(i,j)
            NQuuen(i+1)
            diagonal0(i, j)
            sero0(i, j)
            chess[i][j] = 0



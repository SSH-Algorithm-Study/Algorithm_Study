import math

def answer(N):
    for i in range(1,N):
        sum = i
        number = str(i)

        for num in number:
            sum += int(num)

        if sum == N:
            return i

    return 0

N = int(input())
print(answer(N))
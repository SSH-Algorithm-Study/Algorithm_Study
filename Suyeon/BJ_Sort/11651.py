import sys

N = int(input())
dots = []

for _ in range(N):
    dots.append(list(map(int, sys.stdin.readline().split())))

dots.sort(key=lambda x: (x[1],x[0]))

for dot in dots:
    print(*dot)

import sys

N = int(input())
dots = []

for _ in range(N):
    dots.append(list(map(int,sys.stdin.readline().split())))

dots.sort()

for dot in dots:
    print(*dot)
import sys

N = int(sys.stdin.readline())
members = []

for _ in range(N):
    member = list(sys.stdin.readline().split())
    members.append([int(member[0]), member[1]])

members.sort(key= lambda x : x[0])

for mem in members:
    print(*mem)
import sys
import heapq

N = int(sys.stdin.readline())
pq = []

for _ in range(N):
    heapq.heappush(pq, int(sys.stdin.readline()))

for _ in range(len(pq)):
    print(heapq.heappop(pq))


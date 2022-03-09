############# heap sort
import sys
import heapq

N = int(sys.stdin.readline())
pq = []

for _ in range(N):
    heapq.heappush(pq, int(sys.stdin.readline()))

for _ in range(len(pq)):
    print(heapq.heappop(pq))



########### sort함수

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

sys.stdout.write('\n'.join(map(str,nums)))
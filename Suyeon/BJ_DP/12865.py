import sys
import heapq

N, maxWeight = map(int,sys.stdin.readline().split())
weights = []
values = []
pq = []

maxValue = -sys.maxsize

### 데이터 넣기 ###
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    weights.append(w)
    values.append(v)

heapq.heappush(pq, [0, 0, 0])

while pq:
    value, weight, level = heapq.heappop(pq)
    value = -value

    if level < N:
        if weight <= maxWeight and value + sum(values[level:]) > maxValue:
            maxValue = max(maxValue, value)
            heapq.heappush(pq, [-value-values[level], weight+weights[level], level+1])
            heapq.heappush(pq, [-value, weight, level+1])
    else:
        if weight <= maxWeight:
            maxValue = max(maxValue, value)

print(maxValue)




import collections
import sys


# ========== 딕셔너리
N = int(input())
freqs = collections.defaultdict(int)

for _ in range(N):
    freqs[int(sys.stdin.readline())] += 1

keys = sorted(list(freqs.keys()))

for key in keys:
    for _ in range(freqs[key]):
        print(key)



########## 배열

cnt = [0 for _ in range(10001)]

for _ in range(N):
    cnt[int(sys.stdin.readline())] += 1

for i in range(1,10001):
    for _ in range(cnt[i]):
        sys.stdout.write(str(i)+"\n")
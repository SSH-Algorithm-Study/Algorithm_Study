import sys
import collections

N = int(input())
nums = []
result = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

if N == 1:
    print(nums[0])
    print(nums[0])
    print(nums[0])
    print(0)

else:
    nums.sort()

    result.append(round(sum(nums)/N)) # 산술평균
    result.append(nums[N // 2])  # 중앙값

    # 최빈값
    freqs = collections.Counter(nums).most_common(2)
    if freqs[0][1] == freqs[1][1]:
        result.append(freqs[1][0])
    else:
        result.append(freqs[0][0])
    result.append(nums[-1] - nums[0])  # 범위

    sys.stdout.write("\n".join(map(str, result)))
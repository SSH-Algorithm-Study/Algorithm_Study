import collections


## 시도 
class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:

        def maxInterval(alpa, head, tail, count):
            # 처음 연속되는 문자 뛰기
            while tail < len(s) and s[tail] == alpa:
                tail += 1

            # 다른 것들 최대한 바꾸기
            while tail < len(s) and count:
                if s[tail] != alpa:
                    count -= 1
                tail += 1

            # 마지막 연속되는 문자 뛰기
            while tail < len(s) and s[tail] == alpa:
                tail += 1

            if count:
                while head >= 0:
                    head += 1
                    count -= 1

            # 첫 원소기준 가장 큰 window길이
            return tail - head

        max = maxInterval(s[0],0,0,k)

        head = 1

        while head + max -1 < len(s):
            freq = collections.Counter(s[head:head+max]).most_common(1)
            count = max-freq[0][1]
            if count <= k: # 최대길이가 같거나 길 가능성이 있을 때
                max = maxInterval(freq[0][0], head, head+max, k-count)

            head += 1


        return max


# sol = Solution()
# print(sol.characterReplacement(s = "AABABBA", k = 1))

print(collections.Counter([1,1,1,2,2,2,3,3]).most_common(1))



## 풀이
class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = collections.defaultdict(int)
        left, right = 0, 0
        result = 0

        while right < len(s): # 끝에 다다르면 끝
            freqs[s[right]] += 1

            diff = right - left + 1 - max(freqs.values()) # 최대빈도와 다른 문자수
            if diff > k: # 가능성 아예 없는 경우
                left += 1
                right += 1
            else: # 가능성 있는 경우
                right += 1
                result = right - left  # right 옮긴곳이 알파벳 모르기 때문에 하나 적게

        return result


sol = Solution2()
print(sol.characterReplacement(s = "ABAB", k = 2))
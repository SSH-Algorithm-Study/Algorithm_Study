import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0

        freqs = collections.Counter(t)
        substr = collections.defaultdict(int)

        result = ""

        def check(substr): # substring 판단
            for key in freqs.keys():
                if substr[key] < freqs[key]:
                    return False
            return True


        while right < len(s) : # 가장왼쪽기준으로 substring찾기

            substr[s[right]] += 1
            if not check(substr):
                right += 1
            else:
                result = s[left:right+1]
                break

        while right < len(s)-1 :
            if check(substr): # substring 맞으면 왼쪽 쭉 땡기기
                result = s[left:right + 1] # 매번 최신 window 갱신
                substr[s[left]] -= 1
                left += 1
            else: # substring깨지면 그 윈도우 크기로 슬라이딩 하면서 다음 구간 찾기
                substr[s[left]] -= 1
                left += 1
                right += 1
                substr[s[right]] += 1

        # right가 끝에 도달했을 때
        if check(substr): # substring 있다면  pass
            while left <= right: # 마지막으로 왼쪽 쭉 땡기기

                if check(substr):

                    substr[s[left]] -= 1
                    left += 1
                else:
                    break
            result = s[left - 1:right + 1] # substring깨진 직후니까 바로 전값으로 반환


        return result


sol = Solution()
print(sol.minWindow(s = "AAA", t = "AA"))







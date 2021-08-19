
# two for loops
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 0

        for i in range(len(s)):
            state = 0   # 중복발견여부
            for j in range(len(s) - i - 1):
                if s[i + j + 1] in s[i:j + i + 1]: #다음 문자가 중복이었다면
                    max_len = max(j + 1, max_len)
                    state = 1
                    break
            if not state: # 중복문자가 끝까지 없었다면
                max_len = max(max_len, len(s) - i)

        return max_len


    


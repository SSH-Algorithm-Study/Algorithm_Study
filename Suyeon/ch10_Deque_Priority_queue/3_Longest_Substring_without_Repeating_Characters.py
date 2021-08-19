import collections
# two for loops
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 0
        chars = collections.defaultdict(int)

        for i in range(len(s)):
            chars[s[i]] = 1
            for j in range(len(s) - i - 1):
                if chars[s[i + j + 1]] > 0:
                    max_len = max(j + 1, max_len)
                    chars.clear()
                    break
                else:
                    chars[s[i+j+1]] = 1
            if chars:  # chars가 차있다면
                max_len = max(max_len, len(chars))

        return max_len





import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 0
        chars = collections.defaultdict(int)

        for i in range(len(s)):
            chars[s[i]] = 1
            for j in range(len(s) - i - 1):  # 전체길이에서 i까지의 길이 빼기
                if chars[s[i + 1 + j]] > 0: # 추가할 문자가 이미 있었다면
                    max_len = max(j + 1, max_len)   # 거기까지 길이
                    chars.clear()
                    break
                else:
                    chars[s[i+j+1]] = 1  # 추가할 문자가 없었다면
            if chars:  # chars가 차있다면
                max_len = max(max_len, len(chars))

        return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: # 한글자 이하일때
            return len(s)
        max_len = 0
        chars = collections.defaultdict(int)

        front = 0
        rear = 1
        chars[s[front]] = front
        while front < len(s) and rear < len(s):
            if chars[s[rear]] in chars: # 중복이 있는경우
                max_len = max(max_len,len(chars)) #이제까지 길이저장
                chars.clear() # 비우고
                chars[s[rear]] = rear
                front = rear     # 중복이 나온부분부터 시작
                rear = front+1
            else:
                chars[s[rear]] = rear
                rear = rear + 1
        if len(chars) > 1: # 마지막에 중복으로 끊나지 않은경우
            max_len = max(max_len, len(chars))

        return max_len










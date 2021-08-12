class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(' : ')',
            "[" : ']',
            '{' : '}',
        }

        stack = []

        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            elif not stack or char != stack.pop():  # stack이 비었거나 짝이 안 맞는경우
                return False

        return len(stack) == 0   # 맞지 않은 짝이 남은경우 False








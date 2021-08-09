class Solution:
    def reverseString(self, s) -> None:
        repeat = len(s) // 2
        for i in range(repeat):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]

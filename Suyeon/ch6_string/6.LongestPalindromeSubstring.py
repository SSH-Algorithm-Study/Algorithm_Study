# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         result = ""
#
#
#         # 홀수단어검사
#         for i in range(len(s) - 2):
#             if s[i:i + 3] == ''.join(reversed(s[i:i + 3])):
#                 left = i - 1
#                 right = i + 3
#
#                 while left >= 0 and right <= len(s) - 1:  # left, right 제한걸어두기
#                     if s[left] == s[right]:  # 하나씩 늘려가며 같은지 비교
#                         left -= 1
#                         right += 1
#                     else:
#                         break    # 양옆이 다른순간 끝냄
#                 if len(result) < len(s[left + 1:right]):  # 범위오버든 양옆이 달랐던 둘다 그 전까지가 정답
#                     result = s[left + 1: right]  # result에는 항상 최대길이만 저장
#
#
#        # 홀수단어검사
#         for i in range(len(s) - 1):
#
#             if s[i:i + 2] == ''.join(reversed(s[i:i + 2])):
#                 left = i - 1
#                 right = i + 2
#                 while left >= 0 and right <= len(s) - 1:
#                     if s[left] == s[right]:
#                         left -= 1
#                         right += 1
#                     else:
#                         break
#
#                 if len(result) < len(s[left + 1:right]):
#                     result = s[left + 1: right]
#
#        # 여러가지 예외로 2글자이상의 단어가 없었다면 첫단어로 반환
#         if result == "":
#             result = s[0]
#
#         return result

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:  # 양옆이 같다면 늘려가기
                left -= 1
                right += 1
            return s[left + 1: right]  # 범위를 넘던 양옆이 아니든 바로 전까지 출력

        # 예외적인 부분들 빨리 처리해서 시간 아끼기
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        for i in range(len(s) - 1):  # 범위는 짝수(2)에 맞춘다
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),  # 마지막에 i+2가 범위넘어도 expand에서 if문에서 걸러짐
                         key=len
                         )

        return result

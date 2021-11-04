class Solution:
    def is_palindrome(self, word):
        if word == word[::-1]:
            return True
        else :
            return False

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    new_word = words[i] + words[j]
                    if self.is_palindrome(new_word):
                        result.append([i,j])

        return result





import collections

class Solution:
    def mostCommonWord(self, paragraph, banned) -> str:
        paragraph = paragraph.lower()  # 소문자로 바꾸기
        for i in paragraph:
            if not (i.isalpha() or i.isspace()):
                paragraph = paragraph.replace(i, " ")

        word_list = paragraph.split(" ")  # 공백으로 단어 나누기
        banned.append("") # banned에 "" 추가
        word_list = [i for i in word_list if i not in banned]  # 금지된 용어들 제거
        count_dict = collections.Counter(word_list)  # 빈도수로 나타내기
        letter, count = count_dict.most_common(1)[0]  # 그것 중 가장 빈도수 높은 것

        return letter

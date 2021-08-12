import collections

class Solution:
    def groupAnagrams(self, strs):
        sorted_list = ["".join(sorted(list(str), reverse= False)) for str in strs ] # 각 문자열을 정렬해서 리스트만들기
        keys = list(dict(collections.Counter(sorted_list)).keys())  # key리스트로 빼내기
        result = [] # 결과리스트
        for i in range(len(keys)):
            gruop = [ strs[j] for j in range(len(sorted_list)) if sorted_list[j] == keys[i]] # key의 원소와 같은 것들끼리 group화 하기
            result.append(gruop)

        return result




#맨처음 풀이한 방법
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc","3":"def","4":"ghi","5":"jkl",
                "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"} #딕셔너리 key로 mapping하도록(+파이썬의 str은 시퀀스라 문자만 있을때 반복문이 필요하면 문자열로 묶어도됨)
        
        ans=[]
        for digit in digits:
            if ans==[]: #맨 처음 digit일때
                for dig in dic[digit]:
                    ans.append(dig)
            else: #기존의 수들이 있을때
                new_ans=[]
                for existing_ans in ans: #!이 for문 안에서 ans에 append를 하면 무한반복문으로 time out난다
                    for dig in dic[digit]:
                        new_ans.append(existing_ans+dig)
                ans = new_ans
                
        return ans
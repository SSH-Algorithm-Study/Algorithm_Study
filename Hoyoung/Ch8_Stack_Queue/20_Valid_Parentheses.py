#처음 푼 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        stack =[] #스택으로 사용
        match ={')':'(','}':'{',']':'[' }
        
        for now_char in s:
            if now_char in {'(', '{','['}:
                stack.append(now_char) #스택에 push
            else:
                if not stack or stack.pop() != match[now_char]:
                    return False
        
        if stack: #다 끝났는데 스택이 차있는경우
            return False
        else:
            return True

#다듬어진 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        match ={')':'(','}':'{',']':'[' }
        
        for now_char in s:
            if now_char in match: #matching 테이블 이용하면 됨
                stack.append(now_char)
            elif not stack or stack.pop() != match[now_char]: #else안에 if 하나 elif로 정리
                    return False
        
        return len(stack)==0 #스택이 비어있는걸 len으로 확인
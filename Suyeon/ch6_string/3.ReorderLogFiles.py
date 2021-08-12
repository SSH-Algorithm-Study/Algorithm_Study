class Solution:
    def reorderLogFiles(self, logs) :
        dig = []
        let = []
        for i in logs : # logs를 숫자, 문자 로그로 나누기
            sep = i.find(" ") # 식별자 분리

            if i[sep+1:].replace(" ", "").isalpha(): # 식별자 분리 후 뒤가 문자일때
                let.append(i)
            else:                                    # 숫자일때
                dig.append(i)

        let = sorted(let, key=lambda let : (let[let.find(" ")+1:], let[:let.find(" ")])) # 정렬 다중조건
        let = let+dig
        return let

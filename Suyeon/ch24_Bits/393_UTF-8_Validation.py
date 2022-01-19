class Solution:
    def validUtf8(self, data) -> bool:

        first = bin(data[0])[2:].zfill(8)
        count = 0
        print(first)
        # 몇글자 문자인지 구하기
        for bit in first:
            if bit == "0":
                break
            count += 1


        if count == 0:
            return True
        if count == 2:
            return False

        # 문자길이 짧은 경우
        if len(data) < count:
            return False

        for num in data[1:count]:
            print(bin(num)[2:].zfill(8)[:2])
            if bin(num)[2:].zfill(8)[:2] !="10":
                return False

        return True

sol = Solution()
print(sol.validUtf8(([240,162,138,147,145])))







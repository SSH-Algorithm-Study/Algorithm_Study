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
        if count == 1:
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



class Solution:
    def validUtf8(self, data) -> bool:
        start = 0



        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6 != 0b10): # size만큼 있어야하고 앞에 10이어야함
                    return False
            return True

        while start < len(data):
            first = data[start]

            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0b0:
                start += 1
            else: # check가 false거나 1-4바이트 해당안되는 문자들
                return False

        return True




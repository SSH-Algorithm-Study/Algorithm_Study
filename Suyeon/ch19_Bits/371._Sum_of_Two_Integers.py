class Solution:
    def getSum(self, a: int, b: int) -> int:

        # 2의 보수처리
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        a_bi = bin(a & MASK)[2:].zfill(32)
        b_bi = bin(b & MASK)[2:].zfill(32)

        result = []
        sum, carry = 0, 0

        for i in range(32):
            A = int(a_bi[31-i])
            B = int(b_bi[31-i])

            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(str(sum))


        if carry == 1:
            result.append("1")

        result = int("".join(result[::-1]), 2) & MASK

        # 음수처리
        if result > INT_MAX:
            result = ~(result ^ MASK)


        return result



sol = Solution()
print(sol.getSum(20,30))
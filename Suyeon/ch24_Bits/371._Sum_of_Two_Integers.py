class Solution:
    def getSum(self, a: int, b: int) -> int:
        a_bi = bin(a)
        b_bi = bin(b)
        print(a_bi + " "+b_bi)
        i = len(a_bi) - 1
        j = len(b_bi) - 1

        result = ""
        sum, carry = 0, 0

        for _ in range(max(i,j)):
            sum ^= carry
            print(sum, carry)

            if i > 1:
                sum ^= int(a_bi[i])
                carry = int(a_bi[i])
                i -= 1
                print(sum, carry)

            if j > 1:
                sum ^= int(b_bi[j])
                carry &= int(b_bi[j])
                j -= 1
                print(sum, carry)


            result = str(sum) + result
            sum = 0

            print("------------------")


        return int(result, 2)



sol = Solution()
print(sol.getSum(20,30))
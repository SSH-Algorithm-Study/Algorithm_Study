class Solution:
    def calculate(self,left,right,opt):
        result = []
        for l in left:
            for r in right:
                result.append(eval(str(l) + opt + str(r)))
        return result

    def diffWaysToCompute(self, expression: str):
        answer = []
        if expression.isdigit():
            return [expression]

        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])

                answer.extend(self.calculate(left,right,expression[i]))

        return answer

